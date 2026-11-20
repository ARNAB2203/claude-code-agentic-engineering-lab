import pytest
from fastapi.testclient import TestClient

from app.main import Base, app, engine


@pytest.fixture(autouse=True)
def clean_database():
    """Keep contract tests independent of the local development database."""
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    yield
    Base.metadata.drop_all(engine)


def test_mock_requirement_to_approval_flow():
    client = TestClient(app)
    with client:
        project = client.post("/projects", json={"name": "Issue tracker"}).json()
        requirement = client.post("/requirements", json={"project_id": project["id"], "title": "Create issue", "description": "Users can submit a project issue."}).json()
        execution = client.post(f"/requirements/{requirement['id']}/executions").json()
        assert execution["provider"] == "mock"
        assert "no Claude model was invoked" in execution["proposal"]
        rejected = client.post(f"/executions/{execution['id']}/approval", json={"decision": "rejected"})
        assert rejected.status_code == 422
        approved = client.post(f"/executions/{execution['id']}/approval", json={"decision": "approved"})
        assert approved.status_code == 201


def test_requirement_requires_existing_project():
    client = TestClient(app)
    with client:
        response = client.post("/requirements", json={"project_id": "missing", "title": "Missing project", "description": "This should be rejected."})
    assert response.status_code == 404
