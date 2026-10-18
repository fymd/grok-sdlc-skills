# Code Review Checklist

Walk every change against the axes below. Categorize findings as
**Blocker** (must fix before merge/ship), **Major** (should fix soon), or
**Minor / Nit** (optional).

## Axes (apply all)
- [ ] **Correctness** — meets acceptance criteria; edge cases handled; invariants preserved
- [ ] **Security** — input validation; authN/authZ; no hard-coded secrets; injection risks; dependency vulnerabilities
- [ ] **Simplicity** — a newcomer understands it quickly; no unnecessary abstraction; no dead/commented-out code
- [ ] **Performance** — no N+1 / unbounded loops; no leaks; no blocking calls on critical paths
- [ ] **Maintainability** — clear module boundaries; testable; non-obvious decisions documented
- [ ] **Testing** — adequate coverage of changed behavior; readable tests; missing failure-path tests added

## Security quick checklist
- [ ] No secrets in source
- [ ] All external input validated
- [ ] AuthZ checks on every sensitive operation
- [ ] Dependencies pinned and reasonably up to date
- [ ] Error messages do not leak sensitive information
