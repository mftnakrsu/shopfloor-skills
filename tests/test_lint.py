import contextlib
import io
import sys
import tempfile
import unittest
from unittest import mock
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

import lint  # noqa: E402

SKILL = """---
name: {name}
description: >-
  Runs a test procedure on a production line. Use when testing the linter.
license: MIT
metadata:
  version: "1.0.0"
  category: {stage}
  standards: ""
---
# Test skill

## Conventions
- Times are in minutes.

## Inputs
- Shift length.

## Procedure
1. Follow [the guide](references/guide.md).

## Validation
- Check the total.

## Output
- One table.

## Pitfalls
1. Skipping the check.

## Hand-offs
- Cause unknown: `{handoff}`
"""

REFERENCE = "# Guide\n\nShort guide.\n\n## Sources\n\n- A public book.\n"

AGENT = """---
name: {name}
description: >-
  Coaches a test team. Use when testing the linter.
model: inherit
skills: [{skills}]
---
## Role
Uses `{body_skill}` when needed.
"""

README = "# Test\n"


def skill_text(replace=(), name="solve-8d", handoff="solve-8d"):
    text = SKILL.format(name=name, stage=name.split("-")[0], handoff=handoff)
    for old, new in replace:
        assert old in text, old
        text = text.replace(old, new)
    return text


class Repo:
    def __init__(self, root):
        self.root = Path(root)
        self.write("README.md", README)

    def write(self, relpath, text):
        path = self.root / relpath
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
        return path

    def skill(self, name="solve-8d", text=None, cases=("normal", "missing-data", "trap")):
        self.write(f"skills/{name}/SKILL.md", text or skill_text(name=name, handoff=name))
        self.write(f"skills/{name}/references/guide.md", REFERENCE)
        self.cases(name, cases)

    def agent(self, name="8d-moderator", skills="solve-8d", body_skill="solve-8d", text=None):
        self.write(f"agents/{name}.md", text or AGENT.format(name=name, skills=skills, body_skill=body_skill))
        self.cases(name, ("scenario",))

    def cases(self, owner, kinds):
        for kind in kinds:
            self.write(f"evals/{owner}--{kind}/prompt.md", "---\nmax_turns: 5\n---\nDo it.\n")
            self.write(f"evals/{owner}--{kind}/graders/criteria.md", "---\ntype: llm\n---\nIt worked.\n")


class LintTestCase(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.repo = Repo(self._tmp.name)
        self.repo.skill()
        self.repo.agent()

    def tearDown(self):
        self._tmp.cleanup()

    def errors(self, private_terms=()):
        return lint.lint(self.repo.root, private_terms)

    def assertError(self, fragment, private_terms=()):
        errors = self.errors(private_terms)
        self.assertTrue(any(fragment in e for e in errors), f"no error containing {fragment!r} in {errors}")

    def assertClean(self):
        self.assertEqual(self.errors(), [])


class SkillFrontmatterTest(LintTestCase):
    def test_valid_repo_is_clean(self):
        self.assertClean()

    def test_name_must_match_folder(self):
        self.repo.skill(text=skill_text([("name: solve-8d", "name: solve-9d")]))
        self.assertError("name 'solve-9d' must match 'solve-8d'")

    def test_name_needs_a_stage_prefix(self):
        self.repo.skill(name="fix-8d")
        self.assertError("must start with a stage prefix")

    def test_unknown_key_is_rejected(self):
        self.repo.skill(text=skill_text([("license: MIT\n", "license: MIT\nauthor: me\n")]))
        self.assertError("frontmatter key 'author' is not allowed")

    def test_missing_key_is_reported(self):
        self.repo.skill(text=skill_text([("license: MIT\n", "")]))
        self.assertError("frontmatter key 'license' is missing")

    def test_description_needs_use_when(self):
        self.repo.skill(text=skill_text([("Use when testing the linter.", "For tests.")]))
        self.assertError("description must contain 'Use when'")

    def test_description_length_limit(self):
        self.repo.skill(text=skill_text([("Runs a test procedure on a production line.", "x" * 1100)]))
        self.assertError("characters (max 1024)")

    def test_metadata_values_must_be_strings(self):
        self.repo.skill(text=skill_text([('version: "1.0.0"', "version: 1.0")]))
        self.assertError("metadata 'version' must be a quoted string")

    def test_metadata_version_format(self):
        self.repo.skill(text=skill_text([('"1.0.0"', '"1.0"')]))
        self.assertError("must look like 1.0.0")

    def test_category_must_equal_prefix(self):
        self.repo.skill(text=skill_text([("category: solve", "category: plan")]))
        self.assertError("must equal the name prefix 'solve'")

    def test_frontmatter_syntax_error(self):
        self.repo.skill(text=skill_text([("license: MIT", "license: MIT: yes")]))
        self.assertError("frontmatter: line")


class SkillBodyTest(LintTestCase):
    def test_sections_must_be_complete_and_in_order(self):
        self.repo.skill(text=skill_text([("## Conventions", "## Intro"), ("## Inputs", "## Conventions")]))
        self.assertError("sections must be, in order")

    def test_extra_section_is_rejected(self):
        self.repo.skill(text=skill_text([("## Hand-offs", "## Notes\n- x\n\n## Hand-offs")]))
        self.assertError("(found: Conventions, Inputs, Procedure, Validation, Output, Pitfalls, Notes, Hand-offs)")

    def test_needs_one_title(self):
        self.repo.skill(text=skill_text([("# Test skill\n", "")]))
        self.assertError("exactly one '# ' title")

    def test_headings_inside_code_blocks_are_ignored(self):
        self.repo.skill(text=skill_text([("## Validation", "```\n## Not a section\n```\n\n## Validation")]))
        self.assertClean()

    def test_pitfall_limit(self):
        pitfalls = "".join(f"{i}. Pitfall {i}.\n" for i in range(1, 9))
        self.repo.skill(text=skill_text([("1. Skipping the check.\n", pitfalls)]))
        self.assertError("Pitfalls has 8 items (max 7)")

    def test_line_limit(self):
        self.repo.skill(text=skill_text([("## Validation", "filler\n" * 500 + "\n## Validation")]))
        self.assertError("lines (max 500)")

    def test_token_limit(self):
        self.repo.skill(text=skill_text([("- Shift length.", "- " + "x" * 20100)]))
        self.assertError("tokens (max 5000")

    def test_handoff_to_unknown_skill(self):
        self.repo.skill(text=skill_text(handoff="solve-5why"))
        self.assertError("Hand-offs names unknown skill 'solve-5why'")

    def test_handoff_wildcard_is_not_checked(self):
        self.repo.skill(text=skill_text(handoff="solve-*"))
        self.assertClean()


class ReferenceTest(LintTestCase):
    def test_broken_link(self):
        self.repo.skill(text=skill_text([("references/guide.md", "references/missing.md")]))
        self.assertError("broken link 'references/missing.md'")

    def test_external_links_are_not_checked(self):
        self.repo.skill(text=skill_text([("- One table.", "- See [site](https://example.com/x).")]))
        self.assertClean()

    def test_every_reference_is_linked_from_skill(self):
        self.repo.write("skills/solve-8d/references/extra.md", REFERENCE)
        self.assertError("references/extra.md: not linked from SKILL.md")

    def test_references_stay_flat(self):
        self.repo.write("skills/solve-8d/references/deep/x.md", REFERENCE)
        self.assertError("references must be files directly inside references/")

    def test_reference_ends_with_sources(self):
        self.repo.write("skills/solve-8d/references/guide.md", "# Guide\n\nNo sources.\n")
        self.assertError("must end with a '## Sources' section")

    def test_long_reference_needs_contents(self):
        body = "# Guide\n\n" + "line\n" * 120 + "\n## Sources\n\n- Book.\n"
        self.repo.write("skills/solve-8d/references/guide.md", body)
        self.assertError("must start with a '## Contents' section")
        self.repo.write("skills/solve-8d/references/guide.md", "# Guide\n\n## Contents\n\n- x\n\n" + body[9:])
        self.assertClean()

    def test_reference_must_not_link_another_reference(self):
        self.repo.write("skills/solve-8d/references/other.md", REFERENCE)
        self.repo.write("skills/solve-8d/references/guide.md", "# Guide\n\nSee [other](other.md).\n\n## Sources\n\n- Book.\n")
        self.assertError("links to another reference 'other.md'")


class AgentTest(LintTestCase):
    def test_unsupported_key(self):
        self.repo.agent(text=AGENT.format(name="8d-moderator", skills="solve-8d", body_skill="solve-8d").replace(
            "model: inherit", "model: inherit\npermissionMode: plan"))
        self.assertError("frontmatter key 'permissionMode' is not supported for plugin agents")

    def test_name_must_match_file(self):
        self.repo.agent(text=AGENT.format(name="other", skills="solve-8d", body_skill="solve-8d"))
        self.assertError("name 'other' must match '8d-moderator'")

    def test_unknown_preload(self):
        self.repo.agent(skills="solve-5why")
        self.assertError("skills: unknown skill 'solve-5why'")

    def test_prefixed_preload_is_accepted(self):
        self.repo.agent(skills="shopfloor-skills:solve-8d")
        self.assertClean()

    def test_preload_limit(self):
        self.repo.agent(skills="solve-8d, solve-8d, solve-8d, solve-8d")
        self.assertError("preloads 4 skills (max 3)")

    def test_tools_must_be_the_read_only_set(self):
        text = AGENT.format(name="8d-moderator", skills="solve-8d", body_skill="solve-8d")
        self.repo.agent(text=text.replace("model: inherit", "model: inherit\ntools: Read, Write"))
        self.assertError("tools must be omitted or exactly: Read, Grep, Glob, Skill")
        self.repo.agent(text=text.replace("model: inherit", "model: inherit\ntools: Read, Grep, Glob, Skill"))
        self.assertClean()

    def test_unknown_skill_in_body(self):
        self.repo.agent(body_skill="solve-5why")
        self.assertError("body names unknown skill 'solve-5why'")


class EvalTest(LintTestCase):
    def test_skill_needs_all_three_cases(self):
        self.repo.skill(cases=("normal", "trap"))
        (self.repo.root / "evals/solve-8d--missing-data/prompt.md").unlink()
        (self.repo.root / "evals/solve-8d--missing-data/graders/criteria.md").unlink()
        (self.repo.root / "evals/solve-8d--missing-data/graders").rmdir()
        (self.repo.root / "evals/solve-8d--missing-data").rmdir()
        self.assertError("skill 'solve-8d' needs exactly solve-8d--normal, solve-8d--missing-data, solve-8d--trap")

    def test_case_for_unknown_owner(self):
        self.repo.cases("solve-9d", ("normal",))
        self.assertError("cases for unknown skill or agent 'solve-9d'")

    def test_case_needs_a_grader(self):
        (self.repo.root / "evals/solve-8d--trap/graders/criteria.md").unlink()
        self.assertError("evals/solve-8d--trap: needs at least one graders/*.md file")

    def test_case_folder_name_format(self):
        self.repo.write("evals/oops/prompt.md", "x")
        self.assertError("case folders are named '<skill-or-agent>--<kind>'")

    def test_results_folder_is_ignored(self):
        self.repo.write("evals/results/run/aggregate-result.json", "{}")
        self.assertClean()


class TermTest(LintTestCase):
    def test_readme_is_required(self):
        (self.repo.root / "README.md").unlink()
        self.assertError("README.md: missing")

    def test_public_term_in_skill(self):
        with mock.patch.object(lint, "PUBLIC_TERMS", ("examplecorp", "examplecorp production system")):
            self.repo.skill(text=skill_text([("- Shift length.", "- Examplecorp shift length.")]))
            self.assertError("skills/solve-8d/SKILL.md:17: contains public term 'examplecorp'")

    def test_public_term_is_matched_as_a_whole_word(self):
        with mock.patch.object(lint, "PUBLIC_TERMS", ("examplecorp", "examplecorp production system")):
            self.repo.skill(text=skill_text([("- Shift length.", "- Link speed 10 kbps.")]))
            self.assertClean()

    def test_public_term_anywhere_in_readme_fails(self):
        with mock.patch.object(lint, "PUBLIC_TERMS", ("examplecorp", "examplecorp production system")):
            self.repo.write("README.md", "# Test\n\nBuilt at Examplecorp.\n")
            self.assertError("README.md:3: contains public term 'examplecorp'")

    def test_multi_word_public_term(self):
        with mock.patch.object(lint, "PUBLIC_TERMS", ("examplecorp", "examplecorp production system")):
            self.repo.write("CHANGELOG.md", "Inspired by the examplecorp  production system.\n")
            self.assertError("contains public term 'examplecorp production system'")

    def test_scratch_folders_are_skipped(self):
        self.repo.write(".superpowers/sdd/x/notes.md", "Zeta Works 417\n")
        self.repo.write(".claude/worktrees/w/README.md", "Zeta Works 417\n")
        self.assertEqual(self.errors(private_terms=["zeta works 417"]), [])

    def test_build_folders_are_skipped(self):
        self.repo.write("docs-site/node_modules/x.js", "Zeta Works 417\n")
        self.repo.write("docs-site/dist/index.html", "Zeta Works 417\n")
        self.assertEqual(self.errors(private_terms=["zeta works 417"]), [])

    def test_private_terms_are_checked_everywhere_except_private(self):
        self.repo.write("docs/notes.md", "Visit Zeta Works 417 today.\n")
        self.repo.write("private/research.md", "Zeta Works 417\n")
        errors = self.errors(private_terms=["zeta works 417"])
        self.assertEqual(errors, ["docs/notes.md:1: contains private term 'zeta works 417'"])


class MainTest(LintTestCase):
    def run_main(self, *args):
        with contextlib.redirect_stdout(io.StringIO()) as out:
            code = lint.main(["--root", str(self.repo.root), *args])
        return code, out.getvalue()

    def test_exit_codes(self):
        self.assertEqual(self.run_main()[0], 0)
        self.repo.skill(text=skill_text([("license: MIT\n", "")]))
        code, out = self.run_main()
        self.assertEqual(code, 1)
        self.assertIn("lint: 1 problem(s)", out)

    def test_reads_the_default_private_term_file(self):
        self.repo.write("private/private-terms.txt", "# comment\n\nzetaworks\n")
        self.repo.write("docs/x.md", "ZETAWORKS\n")
        code, out = self.run_main()
        self.assertEqual(code, 1)
        self.assertIn("contains private term 'zetaworks'", out)
        self.assertIn("private terms on", out)


if __name__ == "__main__":
    unittest.main()
