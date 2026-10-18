---
name: sdlc-build
description: Implement planned features using incremental vertical slices, test-driven development, and clean engineering practices. Use when coding against an existing plan, implementing tasks, writing features, or user says 实现, 写代码, TDD, incremental. Prefer small commits and tests first.
---

# SDLC Build

## Overview

Execute the implementation plan through small, verified increments. Enforce TDD where practical, maintain clean architecture boundaries, and keep the repository in a releasable state after every meaningful change.

## Prerequisites

- Approved plan (or clear task list) exists.
- GitHub repository is available (create one if missing).

## Core Practices

1. **Test-Driven when logic is non-trivial**  
   Red → Green → Refactor. Write the failing test (or acceptance check) first, then the minimal code to pass it.

2. **Vertical slices**  
   Deliver one complete user-visible or API-visible increment at a time rather than finishing all backend then all frontend.

3. **Contract first for interfaces**  
   Define API schemas, data models, or component props before filling in implementation.

4. **Atomic commits**  
   One logical change per commit. Use conventional commit messages: `feat:`, `fix:`, `test:`, `refactor:`, `docs:`, `chore:`.

5. **Keep main/trunk green**  
   Never leave the default branch in a broken state. Use feature branches for larger work.

The TDD loop, commit conventions, and a build checklist are consolidated in
[`references/tdd-and-commits.md`](references/tdd-and-commits.md).

## Instructions

1. Select the next incomplete task from the plan (highest priority or lowest risk remaining).
2. Create a feature branch if the change is non-trivial: `git checkout -b feat/<short-name>`.
3. For each behavior:
   - Write or update tests that describe the desired behavior.
   - Implement the minimal production code.
   - Run tests in the sandbox until green.
   - Refactor while keeping tests green.
4. Update any related documentation or comments only when the public interface changes.
5. Commit with a clear message and push.
6. Mark the task complete in `plan.md` (checkboxes or status).
7. Repeat until the current milestone is done, then hand off to verify/review.

## Code Quality Rules (enforce while writing)

- Prefer pure functions and explicit dependencies.
- Avoid deep nesting; extract early.
- Handle errors explicitly; never swallow exceptions silently.
- Use meaningful names; avoid abbreviations unless domain-standard.
- Keep files focused; split when a file exceeds ~300-400 lines of logic.
- Follow language/community idioms of the chosen stack.

## Sandbox Usage

- Always run the relevant test suite after changes.
- Install dependencies only inside the project directory.
- Prefer project-local virtualenvs / node_modules over global installs.

## Handoff

After a set of tasks is complete, summarize what was delivered, which tests cover it, and recommend running sdlc-verify next.
