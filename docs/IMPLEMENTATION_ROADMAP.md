# Implementation roadmap

## Milestone 1 — Analysis and controls (current)

Deliver source provenance, catalogue, coverage matrix, gaps, state records, and a platform-foundation specification. Gate: no application code before acceptance criteria and architecture decisions exist.

## Milestone 2 — Foundation

Create the documented project structure, reproducible local setup, backend health endpoint, SQLite development database, typed API contracts, frontend shell, lint/test tooling, and CI. Gate: backend and frontend tests pass locally.

## Milestone 3 — Reference workflow

Implement requirements, specifications, tasks, execution records, approvals, and audit-log domain models with a mock, explicitly labelled agent runner. Gate: approval-gated end-to-end flow and contract tests pass.

## Milestone 4 — Claude Code learning assets

Add concise instructions, path rules, commands, agents, skills, and supported hooks with least-privilege contracts. Gate: installed-version validation and negative security tests.

## Milestone 5 — MCP, SDK, orchestration, plugin

Add local MCP server, controlled SDK adapter, supervisor workflow, plugin package, execution budgets, retry policy, and conflict avoidance. Gate: tool, contract, recovery, and mock-stream tests pass.

## Milestone 6 — Operations, learning, and release

Add diagrams, labs, evaluations, benchmark protocol, portfolio case study, security/dependency scanning, Docker, GitHub workflows, and publishing readiness checks. Gate: reproducible setup, CI evidence, secret scan, and human approval for publication.

Each milestone ends by updating `PROJECT_STATE.md`, `PROGRESS_TRACKER.md`, `DECISIONS.md`, `NEXT_STEPS.md`, and `SESSION_HANDOFF.md`; changes are committed only after relevant checks pass.
