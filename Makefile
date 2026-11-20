.PHONY: test run

test:
	pytest apps/backend/tests

run:
	uvicorn app.main:app --app-dir apps/backend --reload
