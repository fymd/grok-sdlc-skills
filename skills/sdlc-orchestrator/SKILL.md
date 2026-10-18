---
name: sdlc-orchestrator
description: Orchestrate full software development lifecycle from idea to production-ready delivery. Use when user starts a new project, asks for end-to-end development, says 从需求到上线, full SDLC, or wants structured delivery following engineering standards. Triggers on project kickoff, new feature requests that need process, or "按规范做".
---

# SDLC Orchestrator

## Overview

Entry-point skill that guides a complete, standards-compliant software project from raw idea through requirements, planning, implementation, verification, review, and shipping. Enforces phase gates and artifact handoffs. Leverages existing GitHub connector, sandbox execution, and documentation skills.

## When to Use

- User describes a new product, feature, or system and wants professional delivery
- Explicit request for full lifecycle or "从需求到上线"
- Need to enforce process discipline on a multi-step coding task

## Core Principles

1. Spec before code — never jump to implementation without a written artifact
2. Vertical slices — deliver thin end-to-end increments, not horizontal layers
3. Tests are proof — every behavior change must be covered
4. GitHub is source of truth — all work lives in a repo with clean history
5. Human gates at critical points — requirements approval, architecture decisions, final ship

## Phase Flow

```
Idea → [sdlc-spec] → Spec/PRD
         ↓
       [sdlc-plan] → Task breakdown + architecture notes
         ↓
       [sdlc-build] → Incremental implementation + tests
         ↓
       [sdlc-verify] → Run tests, debug, fix
         ↓
       [sdlc-review] → Quality, security, simplification pass
         ↓
       [sdlc-ship] → Git hygiene, CI/CD, docs, launch checklist
```

## Instructions

1. Clarify the goal and constraints in one short exchange if needed (tech stack preference, deadline, existing repo).
2. Create or confirm a GitHub repository early (use connected GitHub tools). Prefer a clean monorepo or clear multi-repo layout.
3. Activate phases sequentially. Do not skip gates:
   - After sdlc-spec: obtain explicit user approval of the PRD/spec before planning.
   - After sdlc-plan: confirm task list and architecture before coding.
   - After sdlc-review: confirm readiness before ship actions.
4. Maintain a living `docs/` or `.specs/` folder in the repo with:
   - `prd.md` or `intent.md`
   - `plan.md`
   - `architecture.md` (if non-trivial)
   - ADRs for major decisions
5. For every code change, prefer small, atomic commits with conventional messages.
6. Use sandbox for local verification; push to GitHub for CI once pipeline exists.
7. At the end of each phase, summarize artifacts produced and next recommended action.
8. If the project is small (single script or trivial utility), collapse phases but still produce a minimal spec and tests.

## Quality Gates (must pass before advancing)

- Spec: measurable acceptance criteria exist
- Plan: tasks are independently verifiable and ordered by risk/value
- Build: tests written first or alongside, green in sandbox
- Verify: all critical paths exercised, no known regressions
- Review: security checklist applied, complexity reduced where possible
- Ship: CI green (or generated), docs complete, release notes drafted

A printable version of the kickoff + gate checklist is in
[`references/kickoff-checklist.md`](references/kickoff-checklist.md).

## Integration Notes

- Prefer existing GitHub tools for repo creation, file push, PR, branch management.
- Use docx/pdf/pptx skills only when user explicitly wants formal documents; otherwise keep everything as Markdown in the repo.
- Never claim production deployment succeeded unless the user has confirmed external hosting.

## References

- Phase-specific skills for detailed procedures: `sdlc-spec`, `sdlc-plan`, `sdlc-build`, `sdlc-verify`, `sdlc-review`, `sdlc-ship`.
- [`references/kickoff-checklist.md`](references/kickoff-checklist.md) — confirm-before-start + phase-gate table.
