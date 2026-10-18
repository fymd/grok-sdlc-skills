---
name: sdlc-ship
description: Prepare a project for release — Git hygiene, CI/CD generation, documentation, release notes, and launch checklist. Use when ready to ship, create PR, set up pipeline, write docs, or user says 上线, 发布, CI/CD, release, 部署准备. Final production readiness.
---

# SDLC Ship

## Overview

Move verified, reviewed code into a releasable state. Focus on reproducibility, automation, clear history, and operator-friendly documentation. Actual production deployment to external cloud remains user-controlled.

## Instructions

### 1. Git Hygiene
- Ensure working tree is clean or only intentional changes remain.
- Prefer linear history on main (rebase or squash as appropriate for the project convention).
- Use conventional commits.
- Tag releases with semver when appropriate (`v1.0.0`).
- Create a pull request if working on a branch; fill a clear PR description (what, why, how to test).

### 2. CI/CD Pipeline
Generate (or update) a GitHub Actions workflow that at minimum:
- Runs on push/PR to main
- Installs dependencies
- Runs lint (if configured)
- Runs the test suite
- (Optional) builds artifacts / Docker image
Keep the workflow simple and readable. Place it at `.github/workflows/ci.yml`.

### 3. Containerization (when relevant)
If the project benefits from containers, produce a multi-stage `Dockerfile` that:
- Uses official base images
- Runs as non-root where practical
- Has a clear ENTRYPOINT/CMD
- Minimizes final image size

### 4. Documentation
Ensure the repository contains:
- `README.md` — what it is, quick start, how to run tests, how to deploy (high level)
- Any operator / runbook notes needed for the current scope
- Updated `docs/` or ADRs reflecting final decisions
Use existing documentation skills only if the user requests formal Word/PDF output; otherwise stay in Markdown.

### 5. Release Notes
Draft a short changelog or release notes covering:
- New features
- Bug fixes
- Breaking changes
- Migration steps (if any)
Use [`references/release-notes-template.md`](references/release-notes-template.md).

### 6. Launch Checklist (present to user)
Use [`references/launch-checklist.md`](references/launch-checklist.md) — covers CI green, secrets documentation, README runnability, monitoring, rollback, and explicit user confirmation of the deploy target.

### 7. Final Handoff
Push all changes, open or update the PR if needed, and give the user a clear summary of what is ready and what remains for them (e.g., cloud credentials, domain, final deploy command).

## Anti-patterns

- Claiming the service is live on the public internet without user confirmation
- Committing secrets or `.env` files
- Over-engineering CI for a simple script
- Leaving the README as a placeholder

## Integration with GitHub

Use the connected GitHub tools for:
- Creating/updating files and committing
- Opening pull requests
- Managing branches and tags
- Checking workflow status when available
