---
description: Generate and run focused checks for an implemented feature.
argument-hint: "<feature or specification path>"
---

Read `$ARGUMENTS`, its acceptance criteria, and the changed files. Add only focused tests needed to prove the criteria. Run the narrowest relevant test command first, then `pytest apps/backend/tests` for backend changes. Report pass/fail counts, unrun checks, and any gaps. Do not hide, weaken, or delete failing tests.
