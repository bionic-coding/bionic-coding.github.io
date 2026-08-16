---
layout: post
title: "Fixing Claude Code crashing in Zed"
date: 2026-08-15
description: "After upgrading to macOS Golden Gate, gatekeeper kept killing the Claude Code binary."
tags: [claude-code, zed]
---

I run Claude Code as an agent inside Zed through ACP (the Agent Client Protocol). Yesterday the agent thread started failing with:

```
Internal error: {
  "details": "Claude Code process terminated by signal SIGKILL"
}
```

but provided no other details and no hint at how to fix it or what was causing it.

After searching (and failing to find) a solution, I started digging into logs and how Zed manages the Claude Code agent.

## TL;DR - what causes the crash

It turned out to be Gatekeeper killing the process... but I had to go digging to find this out.

`dev: open acp logs` shows the JSON-RPC communication between Zed and the agent.

- `initialize` succeeded
- `session/new` failed (Either the compiled Claude Code binary, or an MCP server it spawns.)

That pointed straight at the binary, not the wrapper. And the lack of details or messages in the logs pointed to Gatekeeper killing the process.

## The fix that worked for me

I deleted Zed's vendored Claude adapter and let Zed re-download a clean copy:

```sh
rm -rf ~/Library/Application\ Support/Zed/external_agents/registry/npx/claude-acp/
```

After a restart, Zed fetches a new copy of the adapter and the fresh copy is authorized by Gatekeeper.

If you're still having issues after this step, keep reading. Otherwise you can stop here, you're done.

## Digging into how Zed's Claude Agent is built

Here's how I traced through things as I tried to figure out what was causing the crash.

Three layers order:

1. A **Node interpreter**. Zed runs whatever `node` it discovers on your PATH.
2. The **ACP adapter**, `@agentclientprotocol/claude-agent-acp`. This is a JavaScript wrapper Zed vendors under `~/Library/Application Support/Zed/external_agents/`.
3. The **Claude Code binary**, a compiled executable the adapter runs when you create a session.

`initialize` exercises layers 1 and 2. `session/new` is the first time layer 3 runs. Map the failing method to the layer, and the layer to the fix.

One consequence surprises people: the `claude` version you see in a terminal is often irrelevant. Zed runs its own vendored adapter and its own binary, not the global install on your PATH — unless you set `CLAUDE_CODE_EXECUTABLE`.

### Cause 1: out of memory (rule this out first)

The usual guess for a SIGKILL is the OOM killer. Check it first, because it's quick:

- Update Claude Code. The memory-leak sweep landed in v2.1.121; anything newer includes it.
- Watch memory during a session. A `claude`/`node` process that climbs to many GB before the kill is the leak.
- On Linux, `dmesg | grep -i oom` shows the kernel kill. On macOS, Console.app shows jetsam events.

I was on a newer version with lots of RAM and a reboot changed nothing. So OOM was out. 

### Cause 2: an unsupported Node version (initialize fails)

Zed runs the adapter on whatever `node` it finds. Homebrew installs the current release by default, which on my machine was Node 26. Users have reported issues with Node 25 and newer so I tried a downgrade to Node 24.

Check which Node Zed uses: in the ACP log, the auth entries carry a `command` field with the full path, e.g. `.../node/26.0.0/bin/node`.

Move to an LTS Node:

```sh
brew install node@24
brew unlink node && brew link --overwrite --force node@24
```

Restart Zed and re-check the log. The path should now read `node@24`.

In my case `initialize` already succeeded on Node 26, so this wasn't my blocker — but if your `initialize` itself fails, an unsupported Node is the first thing to fix.

### Cause 3: macOS Gatekeeper kills the binary (session/new fails)

This was my actual problem. `npx` extracts the compiled Claude Code binary into Zed's adapter folder. macOS tags downloaded and extracted files with a quarantine or provenance attribute, and Gatekeeper can reject the binary on first exec — killing it with signal 9 before it logs anything. I suspect this was triggered when I updated to the latest macOS beta release.

```sh
find ~/Library/Application\ Support/Zed/external_agents/registry/npx/claude-acp \
  -name claude -type f 2>/dev/null
```

```sh
"<path>" --version ; echo "exit=$?"
xattr -l "<path>"
spctl --assess --type execute "<path>"
```

`exit=137` (128 + 9) confirms the kernel killed it. A `com.apple.provenance` line in the `xattr` output, or a `rejected` from `spctl`, names Gatekeeper as the cause.

Three possible fixes are:

1. **Reinstall the adapter** (what I chose as it's the safest). Delete the folder and let Zed re-fetch it: `rm -rf ~/Library/Application\ Support/Zed/external_agents/registry/npx/claude-acp/`.
2. **Clear the quarantine**: `xattr -dr com.apple.quarantine <adapter-folder>`.
3. **Re-sign ad-hoc** if provenance persists: `codesign --force --sign - "<path>"`.
