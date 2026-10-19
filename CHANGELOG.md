# Changelog

All notable changes to this project are documented in this file.
The format is based on [Keep a Changelog](https://keepachangelog.com/).

## [Unreleased]

### Added
- `examples/todo-cli/` — a complete, runnable end-to-end walkthrough of the full SDLC flow (PRD, plan, ADR, source, tests, verify report, review). 6 unit tests pass.
- `examples/todo-miniprogram/` — a WeChat mini-program version of the todo app (same add / complete / delete flow, data persisted in local `Storage`, no backend). Ships with `touristappid` so it compiles locally without a WeChat account.
- `examples/todo-miniprogram/tests/store.test.js` — zero-dependency Node logic tests for the data layer (10 cases, runs with `node tests/store.test.js`).
- `examples/todo-miniprogram/LAUNCH.md` — end-to-end launch guide: local verify → real AppID → upload → submit review → publish.
- `README.md` now links to the example walkthrough and documents the `references/` layout.
- Content enhancement (D): self-contained reference files for the remaining skills:
  - `sdlc-orchestrator/references/kickoff-checklist.md`
  - `sdlc-build/references/tdd-and-commits.md`
  - `sdlc-verify/references/verify-checklist.md`
  - `sdlc-ship/references/launch-checklist.md`
  - `sdlc-ship/references/release-notes-template.md`

### Changed
- Updated `sdlc-orchestrator`, `sdlc-build`, `sdlc-verify`, `sdlc-ship` SKILL.md to reference the new checklists/examples instead of inline prose.
- Extracted inline templates out of SKILL.md into portable `references/` files so each skill stays self-contained after install:
  - `sdlc-spec/references/prd-template.md`
  - `sdlc-plan/references/plan-template.md`
  - `sdlc-plan/references/adr-template.md`
  - `sdlc-review/references/review-checklist.md`
- `sdlc-spec`, `sdlc-plan`, `sdlc-review` SKILL.md now reference these templates instead of duplicating them.
- `todo-miniprogram`: `project.config.json` sets an explicit `miniprogramRoot: "./"`; `utils/store.js` `add()` now guards empty / whitespace / undefined titles (returns `null`, no empty todo); `pages/index/index.js` coerces `dataset.id` via `Number()` to avoid string/number mismatch on toggle/remove.

## [0.1.0] - 2026-10-18

### Added
- Initial SDLC skill suite: `orchestrator`, `spec`, `plan`, `build`, `verify`, `review`, `ship`.
- `README.md` with quick-start and cross-agent (Grok / Claude Code / Cursor) compatibility notes.
- MIT `LICENSE`.
- `install.sh` — one-click installer that copies `skills/` into any agent's skills directory.
- `.github/workflows/ci.yml` + `.github/scripts/validate_skills.py` — lints every `SKILL.md` frontmatter on push/PR.

### Notes
- Tag this release locally once merged:
  `git tag v0.1.0 && git push origin v0.1.0`
