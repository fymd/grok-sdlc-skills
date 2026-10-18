# Launch Checklist

Present this to the user before declaring done.

## Pre-flight
- [ ] All tests green in CI
- [ ] Secrets / env vars documented (never committed)
- [ ] README lets a new developer run the project
- [ ] Monitoring / logging approach noted (even if basic)
- [ ] Rollback plan considered
- [ ] User confirmed target environment and will perform the actual deploy

## Git hygiene
- [ ] Working tree clean / only intentional changes
- [ ] Conventional commits; linear history on `main` where convention allows
- [ ] Version tagged (`vX.Y.Z`) when releasing
- [ ] PR description filled (what / why / how to test)

## Never claim
- ❌ The service is live on the public internet without user confirmation
- ❌ Deployment succeeded unless the user verified external hosting
