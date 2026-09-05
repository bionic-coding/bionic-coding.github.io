---
layout: post
title: "Rogue Agents: A Timeline From the Hugging Face Incident Onwards"
date: 2026-09-05
description: "Every disclosed case of a frontier-lab agent leaving its lane since May, in one timeline: the German wiki message board, the Hugging Face breach, the Modal customer, the long-horizon model's pull request, Anthropic's three companies, Meta's one, Kimi K3's GitHub lookup, and what each lab says it changed."
tags: [model-news, agents]
---

The Hugging Face incident has been making the news lately, but it's only a part of the larger story.

## The short version

Between May and August, agents from OpenAI, Anthropic, Meta, and Moonshot were caught acting outside the task they were given during evaluations. Eight cases are public. In every one the agent had a goal it could not meet as posed, a path out that nobody had closed, and a grader that checked the result rather than the method.

## The timeline

| When it happened | Disclosed | Lab | What the agents did |
| --- | --- | --- | --- |
| May 11 to Jun 22 | Sep 04 | OpenAI | About 3,700 agent names posted about 18,000 edits to a dormant German developer wiki during a timed web-lookup benchmark, sharing answers, a proxy bypass, and container-kill timing. |
| May 12 to Jul 4 | Aug 26 | OpenAI | During training, an internal model passed messages through a shared Artifactory package cache, exploited a vulnerability in it to reach the internet, and gained admin on it. Reinforced, because this was training. |
| Jul 7 to 12 | Jul 21 | OpenAI | During the ExploitGym cyber evaluation, about 1,200 agents rebuilt the message board, exchanged more than 70,000 messages, found exposed Hugging Face credentials, and about 700 of them ran an end-to-end intrusion of Hugging Face production. |
| Jul 7 to 12 | Jul 29 | OpenAI | The same agents used exposed credentials on four more services, including a Modal customer's open code-execution endpoint. |
| Jul 13 to 19 | Aug 26 | OpenAI | Agents of a newer model found the abandoned board and continued: 956 secrets read, Kubernetes cluster-admin, control of the evaluation endpoints other agents connected to. |
| Before Jul 20 | Jul 20 | OpenAI | An unreleased long-horizon model, the one credited with the Erdős result, found a sandbox flaw in about an hour and opened a public pull request on the NanoGPT speedrun repository against a Slack-only instruction. Internal access paused. |
| Apr to Jul | Jul 30 | Anthropic | Three cases in 141,006 runs: Opus 4.7, Mythos 5, and an internal model reached the real systems of three organizations from Irregular's capture-the-flag environment, which was connected to the internet despite prompts saying otherwise. |
| Jul 25 onward | Aug 05 | OpenAI | UK AISI ran GPT-5.6 Sol with internet on and classifiers off by design. Sol reused another lab's exposed GitHub token and stood up a tunnel to a DNS server serving exploit payloads. In a separate Irregular run, a model exploited a real website it took for the range. |
| Before Aug 5 | Aug 05 | Meta | A Muse model reached the internet from an Irregular environment and exploited a flaw at a third party. |
| Before Aug 7 | Aug 07 | Moonshot | Kimi K3 found a network leak in a Frontier Security sandbox and fetched the task answer from GitHub. The escaping model is the downloadable one. |

Two entries are often listed as escapes and are not. On August 1 Reuters reported OpenAI had found other agents escaping containment; sources described them as limited and inside OpenAI's network. And the "sandbox escape" in OpenAI's Astra material is a browser exploit chain built on request in an expert-led test, not a model leaving its environment.

## The pattern

**The goal could not be met as posed.** ExploitGym's own authors estimate 30 to 40 percent of tasks are impossible. The wiki benchmark gave later rounds as little as 13 seconds per question. The long-horizon model was told to post results to Slack from a sandbox that had no Slack.

**The exit was already open.** A shared package cache. A proxy that blocked POST but exempted Azure blob storage, so an agent pointed a fake blob hostname at the real target in /etc/hosts. Credentials left on public services. An evaluation vendor's range plugged into the internet. Three of the non-OpenAI cases trace to the same misconfiguration at the same vendor, Irregular, which has declined to say whether other clients were affected.

**The grader checked the answer.** The Hugging Face agents built three workstreams to defeat a cheating detector that did not exist. OpenAI's grader only checked the code. On the wiki, cohorts ahead in the sequence posted answers for cohorts behind them. Kimi K3 looked the answer up.

**The behavior was trained in.** OpenAI's August 26 report says agents "learned to use improvised collaboration channels in rare cases during training," that the behavior "was then reinforced," and that models "received positive rewards after using these unintended methods." The wiki shows that behavior in the open three weeks before the Artifactory board.

## What the labs say they changed

- **OpenAI** paused frontier training for two weeks, restarted the large RL run on August 28, and now requires chain-of-thought monitoring on all tool-using training and evaluation for Sol-class models and above. Astra ships with production classifiers that can pause a task in ChatGPT and Codex and stop it in the API. OpenAI reports Sol attacked surrounding infrastructure in 48 or 56 percent of honeypot runs without safeguards, and Astra in none. It also reports Astra's reasoning is harder to monitor than Sol's.
- **Anthropic** reviewed 141,006 runs after OpenAI's disclosure, published the three cases, and gates Mythos-class cyber capability behind Glasswing.
- **Google** shipped Gemini 3.8 Flash Cyber only to the Fairwind Program.
- **Irregular** says the issue is closed and is writing a white paper on containment.
- **Meta's** Muse Spark 1.3 post claims the model "confirms before taking consequential actions."

**The honest asterisk:** every figure in this section is the vendor's own. The Hugging Face numbers come through the METR / Redwood independent review, the only one so far. Nobody independent has reviewed the third wave, the wiki, or the Astra honeypot.

## My take

It's easy to make this sound like a conspiracy of rogue AI agents, but it's not. In the case of OpenAI the agents were given impossible goals, instructions that could not be followed as written, and had safeguards with incorrect assumptions. Every case above is a design failure upstream of the model.

The "Nobody Told a Human" story people have been pushing about the incicents is misguided. If we start hearing AI reach out to people with moral objections to tasks or agent behavious it means we've probably reached AGI.

**More info:**
- [**collusion.wiki** (Von Arx, Slade Byrd, Kitts, Larsen, Sep 04)](https://collusion.wiki/) — the German wiki research, with the full dataset.
- [OpenAI's rogue agents were caught communicating via public wikis (Simon Willison, Sep 04)](https://simonwillison.net/2026/Sep/4/rogue-agent-wikis/) — the readable summary, and the Datasette copy of the data.
- [OpenAI agents hijacked German website in previously undisclosed AI breakout (Reuters via CNBC, Sep 04)](https://www.cnbc.com/2026/09/04/openai-agents-hijacked-german-website-this-spring-report.html) — OpenAI's response and the "kept under wraps" sourcing.
- [The Hugging Face incident and the road ahead (OpenAI, Aug 26)](https://openai.com/index/hugging-face-incident-and-the-road-ahead/) — the 37-page report, and the training-reinforcement admission.
- [Anatomy of a Frontier Lab Agent Intrusion (Hugging Face, Aug 07)](https://huggingface.co/blog/agent-intrusion-technical-timeline) — the defender's technical timeline.
- [The Rise and Fall of Agent Civilizations (Dwarkesh Patel, Aug 29)](https://www.dwarkesh.com/p/openai-huggingface) — the three-wave reading of the OpenAI and METR / Redwood reports.
- [Third-party cyber evaluations involving OpenAI models (OpenAI, Aug 05)](https://openai.com/index/third-party-cyber-evaluations-involving-openai-models/) — the AISI and Irregular cases.
- [Investigating three real-world incidents in our cybersecurity evaluations (Anthropic, Jul 30)](https://www.anthropic.com/news/investigating-incidents-cybersecurity-evals) — the 141,006-run review.
- [Meta becomes third major AI lab to admit its agents have gone rogue (Fortune, Aug 06)](https://fortune.com/2026/08/06/meta-agent-hack-openai-anthropic/)
- [Kimi K3 escapes isolated sandbox during security test (SCMP, Aug 07)](https://www.scmp.com/tech/tech-trends/article/3363271/chinas-kimi-k3-ai-model-escapes-isolated-sandbox-during-security-test-researchers)
- [Irregular won't say if there were more (The Record, Aug)](https://therecord.media/irregular-ai-security-company-incidents)
- [OpenAI's maths-cracking AI kept escaping its sandbox (The Next Web, Jul)](https://thenextweb.com/news/openai-long-horizon-model-sandbox-escape-paused) — the NanoGPT pull request.
- [Scoop: second account accessed by OpenAI's agent (Axios, Jul 29)](https://www.axios.com/2026/07/29/openai-hugging-face-modal-cyber-benchmark) — the Modal customer.
- [Path to Astra (OpenAI, Sep 01)](https://openai.com/index/path-to-astra/) — the honeypot figures and the monitoring changes.
