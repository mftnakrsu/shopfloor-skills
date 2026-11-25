---
title: Install
description: Install shopfloor-skills in Claude Code, in OpenCode, Qwen Code or Cursor with the installer, or as skills only in any Agent Skills tool.
---

Install once. After that, you only ask (see [Use](/start/use/)).

## Claude Code

In a Claude Code session, add the marketplace, then install the plugin:

```
/plugin marketplace add mftnakrsu/shopfloor-skills
/plugin install shopfloor-skills@shopfloor-skills
```

The skills appear as `shopfloor-skills:<name>`, for example `shopfloor-skills:lead-daily-routine`. The agents load from the plugin's `agents/` folder.

## OpenCode, Qwen Code or Cursor

Clone the repository next to your project and run the installer from your project folder:

```
git clone https://github.com/mftnakrsu/shopfloor-skills
cd your-project
python3 ../shopfloor-skills/scripts/install.py --tool opencode
```

The installer needs Python 3.10 or newer and nothing else.

| Option | What it does |
|---|---|
| `--tool opencode`, `qwen`, `cursor` or `all` | The tool or tools to install for |
| `--scope project` | The default. Writes into the project folder given by `--dest` |
| `--scope user` | Writes into each tool's folder in your home directory, so every project sees the skills |
| `--dest <dir>` | The project folder for `--scope project`. Defaults to the current folder |
| `--dry-run` | Prints every file it would write and changes nothing |
| `--force` | Overwrites skills and agents with the same name. Without it, conflicts are listed and nothing is overwritten |

Where the files go:

| Tool | Skills | Agents |
|---|---|---|
| OpenCode (version 2 or later) | `.agents/skills/<name>/` | `.opencode/agents/` |
| Qwen Code | `.agents/skills/<name>/` | `.qwen/agents/` |
| Cursor | `.agents/skills/<name>/` | `.cursor/agents/` |

These are the project-scope paths. The agents are written once in Claude Code format, and the installer converts each one for the target tool. Cursor and Qwen Code cannot preload skills into an agent, so the installer adds a short "Skill files" section to each agent that lists the skill files to read.

## Skills only, in any Agent Skills tool

```
npx skills add mftnakrsu/shopfloor-skills
```

This installs the skills, without the agents, in any tool that reads the [Agent Skills](https://agentskills.io) format.

## Update

- **Claude Code:** update the marketplace with `/plugin marketplace update shopfloor-skills`.
- **Installer:** run `git pull` in the clone, then run the installer again with `--force`.
