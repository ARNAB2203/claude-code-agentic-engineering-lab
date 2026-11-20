from __future__ import annotations

from datetime import datetime, timezone
from enum import Enum
from uuid import uuid4

from fastapi import Depends, FastAPI, HTTPException, status
from pydantic import BaseModel, ConfigDict, Field
from sqlalchemy import DateTime, ForeignKey, String, Text, create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column, relationship, sessionmaker

DATABASE_URL = "sqlite:///./agentic_lab.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine, expire_on_commit=False)


class Base(DeclarativeBase):
    pass


class Project(Base):
    __tablename__ = "projects"
    id: Mapped[str] = mapped_column(String, primary_key=True)
    name: Mapped[str] = mapped_column(String(120), unique=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True))


class Requirement(Base):
    __tablename__ = "requirements"
    id: Mapped[str] = mapped_column(String, primary_key=True)
    project_id: Mapped[str] = mapped_column(ForeignKey("projects.id"))
    title: Mapped[str] = mapped_column(String(200))
    description: Mapped[str] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True))


class Execution(Base):
    __tablename__ = "executions"
    id: Mapped[str] = mapped_column(String, primary_key=True)
    requirement_id: Mapped[str] = mapped_column(ForeignKey("requirements.id"))
    provider: Mapped[str] = mapped_column(String(32))
    state: Mapped[str] = mapped_column(String(32))
    proposal: Mapped[str] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    approval: Mapped["Approval | None"] = relationship(back_populates="execution")


class Approval(Base):
    __tablename__ = "approvals"
    id: Mapped[str] = mapped_column(String, primary_key=True)
    execution_id: Mapped[str] = mapped_column(ForeignKey("executions.id"), unique=True)
    decision: Mapped[str] = mapped_column(String(16))
    reason: Mapped[str | None] = mapped_column(Text, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    execution: Mapped[Execution] = relationship(back_populates="approval")


class ProjectCreate(BaseModel):
    name: str = Field(min_length=2, max_length=120)


class RequirementCreate(BaseModel):
    project_id: str
    title: str = Field(min_length=3, max_length=200)
    description: str = Field(min_length=10, max_length=10000)


class ApprovalCreate(BaseModel):
    decision: str = Field(pattern="^(approved|rejected)$")
    reason: str | None = Field(default=None, max_length=2000)


class Record(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: str
    created_at: datetime


class ProjectOut(Record):
    name: str


class RequirementOut(Record):
    project_id: str
    title: str
    description: str


class ExecutionOut(Record):
    requirement_id: str
    provider: str
    state: str
    proposal: str


class ApprovalOut(Record):
    execution_id: str
    decision: str
    reason: str | None


def now() -> datetime:
    return datetime.now(timezone.utc)


def db_session():
    with SessionLocal() as session:
        yield session


def proposal_for(requirement: Requirement) -> str:
    return (
        "MOCK EXECUTION — no Claude model was invoked.\n\n"
        f"Technical specification proposal for: {requirement.title}\n"
        f"Goal: {requirement.description}\n"
        "Plan: validate acceptance criteria, implement in an isolated branch, test, then request human approval."
    )


app = FastAPI(title="Agentic Engineering Lab API", version="0.1.0")


@app.on_event("startup")
def initialise_database() -> None:
    Base.metadata.create_all(engine)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "provider": "mock"}


@app.post("/projects", response_model=ProjectOut, status_code=status.HTTP_201_CREATED)
def create_project(payload: ProjectCreate, db: Session = Depends(db_session)) -> Project:
    project = Project(id=str(uuid4()), name=payload.name, created_at=now())
    db.add(project)
    db.commit()
    db.refresh(project)
    return project


@app.post("/requirements", response_model=RequirementOut, status_code=status.HTTP_201_CREATED)
def create_requirement(payload: RequirementCreate, db: Session = Depends(db_session)) -> Requirement:
    if not db.get(Project, payload.project_id):
        raise HTTPException(404, "Project not found")
    item = Requirement(id=str(uuid4()), project_id=payload.project_id, title=payload.title, description=payload.description, created_at=now())
    db.add(item)
    db.commit()
    db.refresh(item)
    return item


@app.post("/requirements/{requirement_id}/executions", response_model=ExecutionOut, status_code=status.HTTP_201_CREATED)
def propose_plan(requirement_id: str, db: Session = Depends(db_session)) -> Execution:
    requirement = db.get(Requirement, requirement_id)
    if not requirement:
        raise HTTPException(404, "Requirement not found")
    execution = Execution(id=str(uuid4()), requirement_id=requirement.id, provider="mock", state="proposed", proposal=proposal_for(requirement), created_at=now())
    db.add(execution)
    db.commit()
    db.refresh(execution)
    return execution


@app.post("/executions/{execution_id}/approval", response_model=ApprovalOut, status_code=status.HTTP_201_CREATED)
def decide(execution_id: str, payload: ApprovalCreate, db: Session = Depends(db_session)) -> Approval:
    execution = db.get(Execution, execution_id)
    if not execution:
        raise HTTPException(404, "Execution not found")
    if execution.approval:
        raise HTTPException(409, "Execution already has a decision")
    if payload.decision == "rejected" and not payload.reason:
        raise HTTPException(422, "A rejection reason is required")
    approval = Approval(id=str(uuid4()), execution_id=execution.id, decision=payload.decision, reason=payload.reason, created_at=now())
    db.add(approval)
    db.commit()
    db.refresh(approval)
    return approval
