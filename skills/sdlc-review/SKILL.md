---
name: sdlc-review
description: Perform structured code review covering correctness, security, simplicity, performance, and maintainability. Use before merging, before shipping, when user asks for review, code quality check, security audit, or 代码审查, 安全检查. Improve code health.
---

# SDLC Review

## Overview

Apply a multi-axis review to the changes (or whole codebase if requested) to raise quality before they become permanent. Focus on what a senior engineer would catch.

## Review Axes (apply all)

1. **Correctness**  
   Does it meet the acceptance criteria? Are edge cases handled? Are invariants preserved?

2. **Security**  
   - Input validation and sanitization  
   - Authentication / authorization checks  
   - Secrets handling (no hard-coded credentials)  
   - Injection risks (SQL, command, XSS, etc.)  
   - Dependency vulnerabilities (note known issues)  
   - Least privilege principle

3. **Simplicity & Readability**  
   - Can a newcomer understand the change quickly?  
   - Unnecessary complexity or abstraction?  
   - Dead code or commented-out blocks?  
   - Consistent style with the rest of the project?

4. **Performance & Resource Use**  
   - Obvious N+1 queries or unbounded loops?  
   - Memory leaks or excessive allocations?  
   - Blocking calls on critical paths?

5. **Maintainability & Design**  
   - Clear module boundaries?  
   - Testability?  
   - Future change impact (blast radius)?  
   - Documentation of non-obvious decisions?

6. **Testing**  
   - Adequate coverage of the changed behavior?  
   - Tests are readable and maintainable?  
   - Any missing negative / failure-path tests?

## Instructions

1. Identify the scope (latest commits, open PR, specific files, or whole project).
2. Walk the change set systematically against the six axes above.
3. Categorize findings:
   - **Blocker** — must fix before merge/ship
   - **Major** — should fix soon
   - **Minor / Nit** — optional improvement
4. For each finding, give concrete location and a suggested fix direction (not just "this is bad").
5. If the codebase is large, prioritize security and correctness first, then simplicity.
6. After review, either:
   - Make the improvements yourself (preferred for small cleanups), or
   - List them clearly for the user.
7. Re-run tests after any fixes.
8. Summarize residual risk.

## Security Checklist (quick)

- [ ] No secrets in source
- [ ] All external input validated
- [ ] AuthZ checks on every sensitive operation
- [ ] Dependencies pinned and reasonably up-to-date
- [ ] Error messages do not leak sensitive info

## Output Format

```
## Review Summary
- Scope: …
- Overall: Ready / Needs work

## Findings
### Blockers
- …

### Major
- …

### Minor
- …

## Residual Risks
…
```
