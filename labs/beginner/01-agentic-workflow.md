# Lab 01: A safe spec-driven Claude Code workflow

**Objective:** Turn a small request into a reviewable implementation plan without treating the model as an autonomous authority.

**Prerequisites:** Git, Python 3.12, the backend setup from the README, and a Claude Code installation whose local command format you have verified.

## Steps

1. Read `CLAUDE.md` and `specs/requirements/001-platform-foundation.md`.
2. Start a fresh session for one feature; keep unrelated questions out of it.
3. Invoke the project spec workflow with a bounded request, such as “add a project list endpoint.”
4. Review the resulting specification against acceptance criteria before implementation.
5. Implement only after approval, then invoke the test workflow.
6. Run `pytest apps/backend/tests` and `git diff --check`.

## Expected outcome and verification

The work produces a specification, focused tests, and an honest result record. A mock result must visibly say `mock`; it is not evidence of a real model call.

## Common errors

- Starting code before criteria are accepted.
- Using broad context instead of the affected files/specification.
- Assuming a book's command syntax or a project command is supported without checking the installed Claude Code version.
- Reporting a passing test suite when tests were not run.
