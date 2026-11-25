# shopfloor-skills

Agent Skills and subagents for people who run production lines: manufacturing and process engineers, shift and area leaders, and continuous-improvement coaches. They cover productivity and flow (OEE, throughput time, line balancing, SMED, TPM, kanban), daily shopfloor leadership (tier meetings, gemba walks), and the documents that keep a line stable (control plan, station instructions, SPC, 8D, process audits).

**Status:** in development. Skills arrive in batches; see [CHANGELOG.md](CHANGELOG.md).

## Install

**Claude Code**

```
/plugin marketplace add mftnakrsu/shopfloor-skills
/plugin install shopfloor-skills@shopfloor-skills
```

**OpenCode, Qwen Code or Cursor**

```
git clone https://github.com/mftnakrsu/shopfloor-skills
cd your-project
python3 ../shopfloor-skills/scripts/install.py --tool opencode
```

Use `--tool qwen`, `--tool cursor` or `--tool all` for the other tools. Add `--scope user` to install for your user account instead of one project, and `--dry-run` to see every file it would write. It needs Python 3.10 or newer and nothing else.

**Skills only, in any Agent Skills tool**

```
npx skills add mftnakrsu/shopfloor-skills
```

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

## Standards and license

ISO, IATF, VDA and AIAG publications are copyrighted by their publishers. Clause numbers in this project are pointers, and every summary is written in our own words. Use the official documents for the binding text.

MIT License. See [LICENSE](LICENSE).
