---
name: sdlc-plan
description: Break an approved specification into small, ordered, verifiable implementation tasks and high-level architecture notes. Use after a PRD exists, when user asks for plan, task breakdown, architecture, or 拆分任务. Produce plan.md before coding.
---

# SDLC Plan

## Overview

Transform an approved PRD into an actionable implementation plan consisting of thin vertical slices, risk-ordered tasks, and lightweight architecture decisions. Enables incremental delivery and clear progress tracking.

## Prerequisites

- An approved or user-confirmed PRD/spec must exist (from sdlc-spec or equivalent).

## Instructions

1. **Read the PRD thoroughly**  
   Extract all functional requirements, acceptance criteria, and non-functional constraints.

2. **Identify architecture and tech decisions**  
   Propose the minimal viable stack if not already constrained. Record major decisions as short ADRs (Architecture Decision Records) in `docs/adr/` or inline in `plan.md`. Prefer boring, well-supported technology unless the PRD demands otherwise.

3. **Decompose into vertical slices**  
   Prefer end-to-end thin slices (UI + API + data + test) over horizontal layers. Each slice should deliver observable value and be independently testable.

4. **Produce `docs/plan.md` (or `.specs/plan.md`)** with:
   - **Summary** — one paragraph of the approach
   - **Architecture Overview** — components, data flow, key interfaces (use simple Mermaid or ASCII if helpful)
   - **Tech Stack** — languages, frameworks, major libraries with versions if known
   - **Task Breakdown** — ordered list of tasks, each with:
     - ID (e.g. T1, T2)
     - Description
     - Acceptance / Definition of Done
     - Estimated complexity (S/M/L)
     - Dependencies
   - **Risks & Mitigations**
   - **Testing Strategy** — unit, integration, e2e focus areas
   - **Milestones** — logical checkpoints

5. **Ordering rules**
   - Highest risk / highest learning value first
   - Infrastructure and contracts (API schemas, data models) early
   - Core happy path before edge cases
   - Keep tasks small enough to finish in one focused session when possible

6. **Handoff**  
   Present the plan, ask user to confirm or adjust priorities, then proceed only after acknowledgment. Commit the plan file.

## Task Quality Checklist

- [ ] Each task has a clear, testable Definition of Done
- [ ] No task is a pure "research" without a concrete output
- [ ] Vertical slices preferred over pure frontend or pure backend tasks
- [ ] Dependencies are explicit

## Anti-patterns

- Giant "implement everything" tasks
- Detailed class diagrams or low-level design before any code exists
- Choosing exotic technology without strong justification from the PRD
