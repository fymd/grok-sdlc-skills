# Verify Checklist

## Acceptance mapping (fill one row per criterion)
| Acceptance Criterion | Evidence (test / screenshot / log) | Status |
|----------------------|-----------------------------------|--------|
| AC-1 list shows tasks | `tests/test_todo.py::test_add_and_list` | PASS |
| AC-2 done toggles     | `tests/test_todo.py::test_complete`     | PASS |

## Test categories to cover
- [ ] Happy path
- [ ] Edge / boundary conditions
- [ ] Failure / error paths
- [ ] AuthN / AuthZ boundaries (if applicable)

## Debugging protocol
1. Reproduce reliably
2. Localize (which layer / component)
3. Reduce to minimal failing case
4. Fix root cause (not symptom)
5. Add a regression test
6. Re-run the relevant suite

## Done when
- [ ] All automated tests green
- [ ] Critical acceptance criteria have evidence
- [ ] No open high-severity bugs
- [ ] Sandbox demonstrates the main user flows
