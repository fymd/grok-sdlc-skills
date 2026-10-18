# ADR-001: Local Storage Format

## Status
Accepted

## Context
The CLI must persist tasks between runs. Options: a single JSON file, a SQLite
database, or an OS keychain/plist. The tool targets zero-dependency portability
and a single local user.

## Decision
Store tasks as a JSON array in `~/.todo-cli.json`, read/written by pure functions
in `src/todo.py`. IDs are sequential integers assigned at write time.

## Consequences
- Positive: no dependencies, human-readable, trivial to back up or script.
- Negative: no concurrent multi-process safety; not suitable for sync.
- Neutral: acceptable for the single-user, single-machine scope.

## Alternatives Considered
- SQLite: rejected — adds a dependency and complexity unjustified by scope.
- OS-native store (plist/registry): rejected — hurts cross-platform portability.
