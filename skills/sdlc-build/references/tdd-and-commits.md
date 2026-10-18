# Build Playbook: TDD & Commits

## TDD cycle (for non-trivial logic)
1. Write a failing test describing the desired behavior.
2. Implement the minimal code to make it pass.
3. Refactor while tests stay green.
4. Commit.

Example:
```python
# test_cart.py (red)
def test_empty_cart_total():
    assert Cart().total() == 0

# cart.py (green)
class Cart:
    def total(self): return 0
```

## Commit conventions (Conventional Commits)
| Type       | When |
|------------|------|
| `feat:`    | new feature |
| `fix:`     | bug fix |
| `test:`    | add/adjust tests |
| `refactor:`| restructure without behavior change |
| `docs:`    | documentation |
| `chore:`   | build / tooling |

Examples:
- `feat(auth): add email login`
- `fix(api): handle empty payload`
- `test(cart): cover discount edge cases`

## Build checklist
- [ ] Change on a feature branch (`feat/<name>`)
- [ ] Tests written / updated alongside code
- [ ] Suite green in sandbox
- [ ] Public interface change reflected in docs
- [ ] Task marked done in `plan.md`
- [ ] One logical change per commit
