# Orchestrator Kickoff & Phase Gates

## Kickoff checklist (confirm before starting)
- [ ] Goal clearly stated (what + why)
- [ ] Constraints known — tech stack, deadline, existing repo, budget
- [ ] Repository decided or created
- [ ] Human gate owners identified (who approves spec / plan / ship)

## Phase gates (do not skip)
| Gate | After phase | Required sign-off |
|------|------------|------------------|
| G1   | sdlc-spec  | PRD approved |
| G2   | sdlc-plan  | Plan + architecture confirmed |
| G3   | sdlc-review| Review cleared (no blockers) |
| G4   | sdlc-ship  | User confirms target env + will perform deploy |

## Collapse rule for tiny tasks
For a single script / trivial utility: still emit a minimal spec and at least one
test, but you may skip separate `plan.md` / ADR docs. Do not skip the spec→test
discipline entirely.

## Example kickoff one-liner
> "用完整 SDLC 流程做一个命令行待办工具，Python、零依赖、要带测试。" →
> orchestrator confirms stack + repo, then hands to sdlc-spec.
