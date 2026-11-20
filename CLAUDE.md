# Claude Code Agentic Engineering Lab

## Working agreement

- Treat requirements, specs, and acceptance criteria as the source of truth. Do not begin a material feature without a spec in `specs/`.
- Make the smallest coherent change; inspect relevant files before editing.
- Run `pytest apps/backend/tests` after backend changes. Report commands not run and failures honestly.
- The default provider is `mock`. Never describe a mock proposal, metric, or result as a real Claude execution.
- Do not add credentials, `.env`, database files, or generated dependency output to Git.
- Use existing checkouts; do not create a Git worktree unless the task explicitly needs one.

## Layout

- `apps/backend/`: FastAPI + SQLAlchemy API.
- `specs/`: requirements and acceptance criteria.
- `docs/`: decisions, state, learning material, and traceability.
- `.claude/`: project-local workflows, agents, and skills; validate syntax against the installed Claude Code release before relying on discovery.

## Common checks

```bash
pytest apps/backend/tests
uvicorn app.main:app --app-dir apps/backend --reload
git diff --check
```
