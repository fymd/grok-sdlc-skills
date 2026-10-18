# Grok SDLC Skills

A complete, production-oriented **Software Development Lifecycle (SDLC)** skill suite for AI coding agents (Grok, Claude Code, Cursor, and compatible systems).

These skills enforce a disciplined, standards-based process from raw idea → requirements → plan → implementation → verification → review → ship.

**Repository**: https://github.com/fymd/grok-sdlc-skills  
**License**: MIT (feel free to use, fork, and adapt)

---

## Skills Included

| Skill | Purpose |
|-------|---------|
| `sdlc-orchestrator` | Entry point. Guides the full lifecycle and enforces phase gates. |
| `sdlc-spec` | Spec-Driven Development — turn ideas into clear, testable PRDs. |
| `sdlc-plan` | Break PRD into vertical slices, architecture notes, and ordered tasks. |
| `sdlc-build` | Incremental implementation + TDD + clean commits. |
| `sdlc-verify` | Systematic testing, debugging, and acceptance proof. |
| `sdlc-review` | Multi-axis code review (correctness, security, simplicity, performance, maintainability). |
| `sdlc-ship` | Git hygiene, CI/CD generation, docs, release notes, launch checklist. |

---

## Quick Start for Other Agents / Programs

### 1. Copy the skills into your agent’s skills directory

```bash
git clone https://github.com/fymd/grok-sdlc-skills.git
cp -r grok-sdlc-skills/skills/*  <your-agent-skills-dir>/
```

Typical locations:
- Grok / Grok Build: `~/.grok/skills/` or project-level `.grok/skills/`
- Claude Code: `.claude/skills/`
- Cursor / other: follow the agent’s skill discovery path

### 2. Trigger the full flow

Just say one of:

- “用完整 SDLC 流程帮我做一个 XXX 项目”
- “从需求到上线，按规范做”
- “Start with sdlc-orchestrator”
- “Full SDLC for this feature”

The orchestrator will activate the phase skills in order and pause for human approval at key gates (spec approval, plan confirmation, final ship).

### 3. Individual phase usage

You can also call any skill directly, e.g.:

- “Use sdlc-spec to write the PRD”
- “Run sdlc-review on the latest changes”
- “Prepare for ship with sdlc-ship”

---

## Example Walkthrough

See [`examples/todo-cli`](examples/todo-cli) for a complete, runnable demo of the
full flow on a tiny Python CLI:

- `docs/prd.md` (sdlc-spec) · `docs/plan.md` + `docs/adr/0001-storage-format.md` (sdlc-plan)
- `src/todo.py` (sdlc-build) · `tests/test_todo.py` + `docs/verify-report.md` (sdlc-verify)
- `docs/review.md` (sdlc-review)

The 6 unit tests pass and the CLI is scriptable — proof that “spec before code”
and “tests are proof” actually hold end to end.

---

## Core Principles Encoded

1. **Spec before code** — no implementation without an approved artifact
2. **Vertical slices** — deliver thin end-to-end increments
3. **Tests are proof** — every behavior change must be covered
4. **GitHub is source of truth** — all work lives in a clean repository
5. **Human gates** — requirements, architecture, and final release require explicit confirmation

---

## Directory Structure

```
skills/
├── sdlc-orchestrator/
│   └── SKILL.md
├── sdlc-spec/
│   ├── SKILL.md
│   └── references/prd-template.md
├── sdlc-plan/
│   ├── SKILL.md
│   └── references/{plan-template.md, adr-template.md}
├── sdlc-build/
│   └── SKILL.md
├── sdlc-verify/
│   └── SKILL.md
├── sdlc-review/
│   ├── SKILL.md
│   └── references/review-checklist.md
└── sdlc-ship/
    └── SKILL.md

examples/
└── todo-cli/        # end-to-end reference walkthrough
    ├── README.md
    ├── src/todo.py
    ├── tests/test_todo.py
    └── docs/{prd.md, plan.md, adr/0001-storage-format.md, verify-report.md, review.md}
```

Each `SKILL.md` follows the standard Agent Skills format (YAML frontmatter + imperative instructions).
Templates used by a skill live in that skill’s `references/` folder so the skill
stays self-contained after installation.

---

## Compatibility

- Designed for Grok (with GitHub connector + sandbox)
- Compatible with any agent that supports the common `SKILL.md` skill format
- Works especially well when the agent has GitHub / git tools available

## Validation

A CI workflow (`.github/workflows/ci.yml`) validates every `SKILL.md` frontmatter
on push/PR using `.github/scripts/validate_skills.py`.

## Contributing / Customization

Feel free to fork and adapt the skills to your organization’s standards (add company-specific security rules, preferred tech stacks, ADR templates, etc.).

Created with the Grok skill-creator and aligned with modern agentic SDLC practices (AgentPatterns.ai taxonomy, Spec-Driven Development, Google-style engineering discipline).

---

**Author**: fymd (via Grok)  
**Last updated**: 2026-10-18
