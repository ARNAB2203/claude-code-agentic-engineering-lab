# Claude Code Agentic Engineering Lab

An honest, spec-driven learning platform for controlled AI-assisted engineering workflows. The first runnable slice uses a deterministic **mock** agent provider; it never presents mock output as genuine Claude execution.

## Run the backend

```bash
python3 -m venv .venv
. .venv/bin/activate
pip install -e "apps/backend[test]"
uvicorn app.main:app --app-dir apps/backend --reload
```

Open `http://127.0.0.1:8000/docs`. Run `pytest apps/backend/tests` for the tested workflow.

See [docs/PROJECT_STATE.md](docs/PROJECT_STATE.md) for scope and current blockers.
