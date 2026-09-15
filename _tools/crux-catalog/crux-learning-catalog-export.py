# /// script
# requires-python = ">=3.10"
# dependencies = ["PyYAML>=6"]
# ///
"""Export the blog's teaching catalog. Reads source; writes JSON to stdout only."""
import argparse
import hashlib
import json
import re
import subprocess
from pathlib import Path
import yaml


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def frontmatter(path):
    raw = path.read_bytes()
    parts = raw.decode("utf-8").split("---", 2)
    if len(parts) != 3 or parts[0].strip():
        raise ValueError(f"Missing frontmatter: {path}")
    data = yaml.safe_load(parts[1])
    if not isinstance(data, dict):
        raise ValueError(f"Invalid frontmatter: {path}")
    return data, digest(raw)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--plugin-root", required=True, type=Path)
    parser.add_argument("--guide", type=Path, default=Path(__file__).with_name("crux-learning-catalog-guide.json"))
    parser.add_argument("--check", type=Path, help="Compare an existing catalog without writing it")
    args = parser.parse_args()
    root = args.plugin_root.resolve()
    guide = json.loads(args.guide.read_text())
    manifest = json.loads((root / "plugin.json").read_text())
    if manifest["version"] != guide["reviewed_plugin_version"]:
        raise ValueError("Plugin version changed: review editorial guidance before updating reviewed_plugin_version")
    skills = sorted((root / "skills").glob("*/SKILL.md"))
    agents = sorted((root / "agents").glob("*.md"))
    if {str(p.relative_to(root)) for p in skills} != set(manifest["skills"]):
        raise ValueError("Manifest and skill directory disagree")
    if {str(p.relative_to(root)) for p in agents} != set(manifest["agents"]):
        raise ValueError("Manifest and agent directory disagree")
    grouped = [s for names in guide["categories"].values() for s in names]
    if len(grouped) != len(set(grouped)) or set(grouped) != {p.parent.name for p in skills}:
        raise ValueError("Editorial categories must cover every skill exactly once")
    if set(guide["roles"]) != {p.stem for p in agents}:
        raise ValueError("Editorial role guidance must cover every agent")
    for field in ("skill_notes", "skill_audience_overrides"):
        if not set(guide[field]).issubset(set(grouped)):
            raise ValueError(f"Unknown skill in {field}")
    category = {s: k for k, names in guide["categories"].items() for s in names}
    try:
        revision = subprocess.check_output(["git", "-C", str(root), "rev-parse", "HEAD"], text=True).strip()
        dirty = subprocess.check_output(["git", "-C", str(root), "status", "--porcelain", "--", "."], text=True)
    except subprocess.CalledProcessError:
        revision, dirty = None, None
    if dirty:
        raise ValueError("Plugin source has uncommitted changes; export an identifiable clean source")
    result = {
        "format_version": "1",
        "title": guide["title"],
        "editorial_status": guide["editorial_status"],
        "source": {
            "plugin_version": manifest["version"],
            "skill_contract_schema_version": manifest["schema_version"],
            "revision": revision,
            "git_state": "clean_plugin_subtree" if dirty == "" else "not_available",
            "manifest_sha256": digest((root / "plugin.json").read_bytes()),
            "guide_sha256": digest(args.guide.read_bytes()),
            "exporter_sha256": digest(Path(__file__).read_bytes()),
            "release_channel": "not_verified_by_exporter",
            "path_base": "plugin root; source paths are relative to the plugin, not the blog"
        },
        "counts": {"agents": len(agents), "skills": len(skills)},
        "teaching_model": guide["teaching_model"],
        "audience_definitions": guide["audience_definitions"],
        "journeys": guide["journeys"],
        "handoff_template": guide["handoff_template"],
        "publication_notes": guide["publication_notes"],
        "agents": [],
        "skills": []
    }
    skill_ids = {p.parent.name for p in skills}
    agent_ids = {p.stem for p in agents}
    associations = {s: [] for s in skill_ids}
    for path in agents:
        fm, sha = frontmatter(path)
        name = path.stem
        if fm["name"] != name:
            raise ValueError(f"Agent name mismatch: {path}")
        declared = fm.get("skills", [])
        if not set(declared).issubset(skill_ids):
            raise ValueError(f"Unknown declared skill: {path}")
        for skill in declared:
            associations[skill].append(name)
        delegates = re.findall(r"Agent[(]([^)]+)[)]", fm.get("tools", ""))
        if not set(delegates).issubset(agent_ids):
            raise ValueError(f"Unknown delegate: {path}")
        result["agents"].append({
            "id": name,
            "source": {"path": str(path.relative_to(root)), "sha256": sha},
            "declared": {
                "description": fm["description"],
                "tools": fm.get("tools"),
                "skills": declared,
                "delegate_targets": delegates,
                "model_alias": fm.get("model"),
                "risk_level": fm.get("metadata", {}).get("risk_level")
            },
            "runtime_names": {
                "claude_code": "crux:" + name,
                "codex": "crux_" + name.replace("-", "_"),
                "opencode": name
            },
            "learning": guide["roles"][name]
        })
    for path in skills:
        fm, sha = frontmatter(path)
        name = path.parent.name
        if fm["name"] != name:
            raise ValueError(f"Skill name mismatch: {path}")
        metadata = fm.get("metadata", {})
        triggers = metadata.get("triggers", "")
        if not isinstance(triggers, str):
            raise ValueError(f"Non-string triggers: {path}")
        phrases = [p.strip() for p in triggers.split("|") if p.strip()]
        explicit = fm.get("disable-model-invocation") is True
        hidden = fm.get("user-invocable") is False
        audience = "agent_internal" if hidden else ("explicit_human" if explicit else "human_request")
        audience = guide["skill_audience_overrides"].get(name, audience)
        result["skills"].append({
            "id": name,
            "source": {"path": str(path.relative_to(root)), "sha256": sha},
            "description": fm["description"],
            "category": category[name],
            "triggers": phrases,
            "declared_invocation": {
                "user_invocable": fm.get("user-invocable"),
                "disable_model_invocation": fm.get("disable-model-invocation"),
                "note": "Null means undeclared, not forbidden. These flags originate in Claude Code; do not assume identical enforcement elsewhere."
            },
            "risk_level": metadata.get("risk_level"),
            "declared_by_agents": sorted(associations[name]),
            "learning": {
                "audience": audience,
                "example_requests": phrases[:2] if audience in ("human_request", "explicit_human") else [],
                "example_status": "Source-declared phrases, not observed routing guarantees or universal command syntax.",
                "note": guide["skill_notes"].get(name, guide["audience_definitions"][audience])
            }
        })
    rendered = json.dumps(result, ensure_ascii=False, indent=2) + "\n"
    if args.check:
        if args.check.read_text() != rendered:
            raise ValueError("Catalog differs from source or editorial guidance; regenerate and review")
        print(json.dumps({"matches": True, "counts": result["counts"]}))
    else:
        print(rendered, end="")


if __name__ == "__main__":
    main()
