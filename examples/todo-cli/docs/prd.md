# Todo CLI — Product Requirements

> Generated with `sdlc-spec` from `skills/sdlc-spec/references/prd-template.md`.

## Problem / Opportunity
Developers and power users often need to capture quick tasks without leaving the
terminal. Existing heavyweight task managers require accounts or GUIs. A tiny,
scriptable CLI todo list removes friction for command-line workflows.

## Goals
- [ ] Add, list, complete, and remove tasks from the terminal
- [ ] Persist tasks between sessions with zero setup
- [ ] Be scriptable / automatable (exit codes, plain output)

## Non-goals
- [ ] No sync across devices
- [ ] No multi-user / sharing
- [ ] No rich scheduling or reminders

## Users & Personas
- Primary: command-line developer who wants fast task capture
- Secondary: automation scripts that append/inspect tasks

## User Stories (Jobs-to-be-done)
1. As a developer I want to add a task from the shell so that I don't context-switch.
   - Acceptance: `todo add "fix bug"` prints `added #1: fix bug`; subsequent `todo list` shows it.
2. As a developer I want to mark a task done so that I track progress.
   - Acceptance: `todo done 1` marks it; `todo list` shows `[x] 1: ...`.
3. As a developer I want to remove a task so that I can correct mistakes.
   - Acceptance: `todo rm 1` removes it; list no longer shows it.

## Functional Requirements
1. The tool MUST support four commands: `add <title>`, `list`, `done <id>`, `rm <id>`.
2. Tasks MUST persist to a local file between invocations.
3. Each task MUST have a stable numeric id, title, and done flag.
4. Unknown or missing ids MUST be handled gracefully (no crash, clear message).

## Acceptance Criteria
- FR1: all four subcommands reachable via argparse.
- FR2: tasks survive process exit (reload from disk returns same data).
- FR3: ids auto-increment; done flag toggles correctly.
- FR4: operating on a non-existent id prints `no such id N` and exits 0.

## Non-functional Requirements
- Performance: sub-100ms for any command on up to 1000 tasks.
- Security: stores only user-provided titles locally; no network, no eval.
- Simplicity: zero third-party dependencies (Python stdlib only).
- Portability: runs on any Python 3.9+ environment.

## Constraints & Assumptions
- Single local machine; single user. Store path defaults to `~/.todo-cli.json`.

## Out of Scope
- Cloud sync, reminders, labels, due dates.

## Success Metrics
- A new user can install and run all four commands within one minute.
- 100% of functional requirements covered by automated tests.

## Open Questions
- Should `list` support filtering by done state? (Deferred.)
