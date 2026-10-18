# Todo CLI — Implementation Plan

> Generated with `sdlc-plan` from `skills/sdlc-plan/references/plan-template.md`.

## Summary
A single-file, stdlib-only Python CLI that stores tasks as a JSON array in a local
file. Four subcommands cover the full lifecycle. No external dependencies keeps it
portable and trivial to ship.

## Architecture Overview
```
CLI (argparse)
   |
   v
store module --(json)--> ~/.todo-cli.json
```
Pure functions: load / save / add / list_items / complete / remove. No global state.

## Tech Stack
- Python 3.9+ (stdlib: argparse, json, pathlib)
- No third-party packages

## Task Breakdown
| ID | Description | Definition of Done | Complexity | Dependencies |
|----|-------------|--------------------|------------|--------------|
| T1 | Storage layer (load/save JSON) | round-trip read/write verified by test | S | - |
| T2 | `add` + `list` commands | tasks persist and list correctly | S | T1 |
| T3 | `done` + `rm` commands | toggling/removal works; bad id handled | S | T1 |
| T4 | Test suite + verify report | all FR covered; green in CI | S | T2,T3 |

## ADRs
See `docs/adr/0001-storage-format.md`. Major decision: JSON file over SQLite for simplicity.

## Risks & Mitigations
- Risk: corrupted store file → Mitigation: `load` falls back to `[]` on parse error.
- Risk: id collision after manual edits → Mitigation: ids are max+1 on write (kept simple; acceptable for single-user).

## Testing Strategy
- Unit: each function in `tests/test_todo.py` (add/list/done/rm/persistence/empty).
- No integration/e2e needed (CLI is the integration surface); smoke-tested manually.

## Milestones
- M1: storage + add/list (T1,T2)
- M2: done/rm + tests + verify (T3,T4)
