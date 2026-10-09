---
name: sdlc-spec
description: Turn raw ideas into clear, testable product requirements and specifications. Use for new projects, feature requests, PRD writing, intent capture, or when user says 需求, 规格, 写PRD, refine idea, or before any coding starts. Spec before code.
---

# SDLC Spec (Spec-Driven Development)

## Overview

Convert vague product ideas or feature requests into a structured, machine- and human-readable specification that downstream phases can execute against. Produces a PRD / intent document with measurable acceptance criteria.

## Instructions

1. **Interview lightly if needed**  
   Ask only the minimum questions required to remove ambiguity (target users, core problem, must-have vs nice-to-have, constraints on tech/stack/time/budget, success metrics). Prefer one round of clarification.

2. **Produce the artifact**  
   Create or update a Markdown file in the project (preferred locations: `docs/prd.md`, `.specs/prd.md`, or `intent.md`). Use the template structure below.

3. **Required sections in the PRD**  
   - **Problem / Opportunity** — 2-4 sentences  
   - **Goals & Non-goals** — explicit lists  
   - **Users & Personas** — primary and secondary  
   - **User Stories / Jobs-to-be-done** — in "As a … I want … so that …" form, prioritized  
   - **Functional Requirements** — numbered, testable statements  
   - **Acceptance Criteria** — Given/When/Then or checklist per major story (must be verifiable)  
   - **Non-functional Requirements** — performance, security, accessibility, scalability, compliance  
   - **Constraints & Assumptions**  
   - **Out of Scope**  
   - **Success Metrics** — how we will know it worked  
   - **Open Questions** — remaining unknowns

4. **Quality bar**  
   - Every functional requirement must map to at least one acceptance criterion.  
   - Avoid implementation details (no "use React" unless it is a hard constraint).  
   - Keep the document under ~800 lines; link to separate architecture notes if needed.

5. **Handoff**  
   Present the PRD to the user, highlight any remaining open questions, and explicitly ask for approval or changes. Do not proceed to planning until approval is given or the user instructs to continue.

6. **Versioning**  
   If the repo already exists, commit the PRD with message `docs: add/update PRD for <feature>`.

## Template Skeleton (copy and fill)

```markdown
# [Project / Feature Name] — Product Requirements

## Problem
...

## Goals
- [ ]

## Non-goals
- [ ]

## Users
...

## User Stories
1. As a … I want … so that …
   - Acceptance:
     - Given … When … Then …

## Functional Requirements
1. …
2. …

## Non-functional Requirements
- Performance: …
- Security: …
- …

## Constraints & Assumptions
…

## Out of Scope
…

## Success Metrics
…

## Open Questions
- [ ]
```

## Anti-patterns

- Writing code or choosing libraries inside the PRD.
- Vague acceptance criteria ("should be fast", "user-friendly").
- Skipping the approval gate.
