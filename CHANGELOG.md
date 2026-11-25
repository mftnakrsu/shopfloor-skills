# Changelog

All notable changes to this project are documented in this file. The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project uses [Semantic Versioning](https://semver.org/).

## [Unreleased]

### Added

- Repository skeleton: plugin manifests, linter, installer for OpenCode, Qwen Code and Cursor, CI, and the `skill-reviewer` agent.
- Brand kit in `assets/brand/`: the Yamazumi logo (lockups, symbol, small-size cut, wordmark, icon tile), the favicon set, animated hero banners and icon tile with GIF and PNG fallbacks, the social preview and `BRAND.md`. The tools in `design/brand/tools/` generate it.
- Plugin directory icon at `.claude-plugin/icon.png`.
- Documentation site in `docs-site/` (Astro Starlight) with the skills catalogue, agents, the hand-off loop and a Türkçe page, and the `docs` workflow that deploys it to GitHub Pages from main once the repository is public.

### Changed

- README: brand header with badges and a nav row, a "What's inside" table of stages that marks each skill available, coming soon or planned, a Use section and a Türkçe section.
