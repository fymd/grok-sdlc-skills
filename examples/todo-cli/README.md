# Example: Todo CLI

A complete, runnable walkthrough of the **grok-sdlc-skills** flow on a tiny project.

This example was produced by applying the skills in order. The artifacts live in
`docs/` and the shipped code in `src/` + `tests/`.

## How the skills map to this folder

| Phase (skill) | Artifact in this example |
|---------------|--------------------------|
| `sdlc-spec`   | [`docs/prd.md`](docs/prd.md) |
| `sdlc-plan`   | [`docs/plan.md`](docs/plan.md), [`docs/adr/0001-storage-format.md`](docs/adr/0001-storage-format.md) |
| `sdlc-build`  | [`src/todo.py`](src/todo.py) |
| `sdlc-verify` | [`tests/test_todo.py`](tests/test_todo.py), [`docs/verify-report.md`](docs/verify-report.md) |
| `sdlc-review` | [`docs/review.md`](docs/review.md) |
| `sdlc-ship`   | this README + conventional commits + (in the real repo) CI |

## Run it

```bash
# from this directory
python src/todo.py add "write the docs"
python src/todo.py list
python src/todo.py done 1
python src/todo.py rm 1

# run the test suite (verify phase)
python -m unittest discover -s tests
```

## What this proves
- Spec before code: `prd.md` existed before `src/todo.py`.
- Vertical slice: storage + commands + tests delivered together.
- Tests are proof: 6 unit tests cover every functional requirement.
- Review gate: `review.md` records findings before "ship".
