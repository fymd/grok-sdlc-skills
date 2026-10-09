---
name: sdlc-verify
description: Systematically test, debug, and validate implemented features until acceptance criteria are met. Use after coding, when tests fail, bugs appear, or user asks to verify, test, debug, 测试, 验证, 修bug. Focus on proof that the software works.
---

# SDLC Verify

## Overview

Prove that the implementation satisfies the acceptance criteria and is free of known regressions. Combine automated tests, manual/browser checks, and disciplined debugging.

## Instructions

1. **Run the existing test suite first**  
   Execute unit, integration, and any e2e tests in the sandbox. Fix failures before adding new checks.

2. **Map acceptance criteria to evidence**  
   For every acceptance criterion in the PRD or plan, produce concrete proof (passing test, screenshot description, log output, or API response).

3. **Add missing tests**  
   If a critical path lacks coverage, write the test now (prefer automated). Focus on:
   - Happy path
   - Important edge cases and boundary conditions
   - Failure / error paths
   - Authorization and security boundaries when relevant

4. **Debugging protocol (when something fails)**  
   a. Reproduce reliably  
   b. Localize (which layer / component)  
   c. Reduce to minimal failing case  
   d. Fix root cause (not symptoms)  
   e. Add a regression test that would have caught it  
   f. Re-run full relevant suite

5. **Browser / UI verification** (when frontend exists)  
   Use available browser tools or describe exact steps + expected results. Check responsive behavior, accessibility basics, and console errors.

6. **Performance / resource smoke checks**  
   For non-trivial services, run a quick load or memory observation if feasible in the sandbox.

7. **Report**  
   Produce a short verification summary:
   - What was tested
   - What passed
   - Remaining known issues or risks
   - Recommendation (ready for review / needs more work)

## Definition of Done for this phase

- All automated tests green
- Critical acceptance criteria have evidence
- No open high-severity bugs
- Sandbox can demonstrate the main user flows

## Anti-patterns

- Declaring "it works" without running tests
- Fixing symptoms while leaving the root cause
- Ignoring flaky tests
