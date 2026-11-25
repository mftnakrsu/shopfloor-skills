# Contributing

This file holds the project rules for skills, agents and evals.

## Ground rules

1. Write everything yourself from public literature. Do not copy text from other skill packs, books or standards.
2. No employer, brand, plant, customer, product or person names in `skills/`, `agents/` or `evals/`. The linter blocks a public list of brand terms. Maintainers also keep a private list in the git-ignored `private/private-terms.txt`.
3. Every number needs a source in `references/`, or a label: "rule of thumb" or "set by local policy".
4. Standards are pointers: a clause number plus your own summary. Never paste standard text.

ISO, IATF, VDA and AIAG publications are copyrighted by their publishers. Clause numbers in this project are pointers, and every summary is written in our own words. Use the official documents for the binding text.

## Adding a skill

1. Pick the stage prefix: `lead-`, `measure-`, `improve-`, `plan-`, `solve-` or `audit-`.
2. Write the three eval cases first: `evals/<skill>--normal/`, `evals/<skill>--missing-data/` and `evals/<skill>--trap/`, each with a `prompt.md` and at least one `graders/*.md`.
3. Write `skills/<skill>/SKILL.md`: the frontmatter, one `# ` title, then exactly these sections in this order: Conventions, Inputs, Procedure, Validation, Output, Pitfalls (at most 7 items), Hand-offs.
4. In Hand-offs and in agent files, write skill names in backticks, like `solve-8d`, and only for skills that already exist. Backticks around any other word that starts with a stage prefix will fail the linter.
5. Put definitions, formulas and worked examples in `references/`. Link every reference file from SKILL.md. A reference longer than 100 lines starts with `## Contents`, and every reference ends with `## Sources`.
6. Put fill-in templates in `assets/`.

**Limits:** SKILL.md at most 500 lines and about 5,000 tokens (characters ÷ 4). The description is at most 1,024 characters and contains "Use when".

## Checks

```
python3 scripts/lint.py
python3 -m unittest discover -s tests
python3 scripts/install.py --tool all --dest /tmp/try --dry-run
claude plugin validate . --strict
claude plugin eval . --case '<skill>--*' --model sonnet --runs 1 --ablation none --no-publish --trust-plugin
```

Install the pre-commit hook once per clone. It runs the linter, including the private term list:

```
git config core.hooksPath scripts/hooks
```
