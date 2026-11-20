# Topic coverage matrix

Status values: **Planned** = designed but not implemented; **Blocked** = awaiting source/version/access prerequisite; **Verified** = implemented and tested. No item is marked verified at this documentation-only milestone.

| Topic ID | Source Section/Page | Topic | Difficulty | Implementation File | Exercise | Verification | Status |
|---|---|---|---|---|---|---|---|
| FND-01 | §6 Module 1 | Fundamentals | Beginner | `labs/beginner/01-cli-fundamentals.md` | Explore a repository safely | CLI/version check | Planned |
| PRM-01 | §6 Module 2 | Prompt engineering | Beginner | `prompts/`, `labs/beginner/` | Refine a requirement prompt | Structured-output contract test | Planned |
| CTX-01 | §6 Module 3 | Context engineering | Intermediate | `labs/intermediate/`, `docs/evaluations/` | Compare contextual approaches | Reliable usage data or protocol | Blocked |
| MEM-01 | PDF Ch. 6, pp. 38–46; §6 Module 4 | Instructions and memory | Intermediate | `CLAUDE.md` | Apply project rules | `CLAUDE.md` review | Implemented |
| SDD-01 | §6 Module 5 | Spec-driven development | Intermediate | `specs/` | Trace a feature end to end | Traceability review | Planned |
| CMD-01 | PDF Ch. 3, pp. 15–21; Ch. 9, pp. 64–71; §6 Module 6 | Custom commands | Intermediate | `.claude/commands/` | Create spec, test, review | Installed CLI discovery | Implemented—unverified activation |
| AGT-01 | PDF Ch. 11, pp. 82–87; Ch. 12, pp. 88–98; §6 Module 7 | Subagents | Intermediate | `.claude/agents/test-writer.md` | Generate isolated tests | Filesystem/tool-scope review | Implemented—unverified activation |
| SKL-01 | PDF Ch. 10, pp. 73–81; §6 Module 8 | Skills | Intermediate | `.claude/skills/spec-author/SKILL.md` | Draft a feature spec | Installed CLI discovery | Implemented—unverified activation |
| HOK-01 | §6 Module 9 | Hooks | Advanced | `.claude/hooks/` | Block secret modification | Positive/negative hook tests | Blocked |
| MCP-01 | §6 Module 10 | MCP server | Advanced | `mcp-servers/` | Query requirements/status | MCP tool tests | Planned |
| ORC-01 | §6 Module 11 | Orchestration | Advanced | `agents/orchestrator/` | Approval-gated workflow | Contract/recovery tests | Planned |
| PLG-01 | §6 Module 12 | Plugin | Advanced | `plugins/` | Package a reusable skill | Install/layout validation | Planned |
| GIT-01 | §6 Module 13 | Git/GitHub | Intermediate | `.github/`, `labs/` | Feature branch/PR flow | Git + authenticated API checks | Blocked |
| SDK-01 | §6 Module 14 | Agent SDK | Advanced | `agents/`, `apps/backend/` | Mock streamed run | Unit/integration tests | Planned |
| SEC-01 | §6 Module 15 | Security/governance | Advanced | `docs/security/`, tests | Reject unsafe input | Security tests | Planned |
| TST-01 | §6 Module 16 | Testing/evaluation | Advanced | `tests/`, `docs/evaluations/` | Evaluate task set | Test/evaluation report | Planned |
| ADV-01 | §6 Module 17 | Advanced capabilities | Expert | `labs/advanced/`, `labs/expert/` | Capability-specific lab | Version/platform matrix | Blocked |
| APP-01 | §4, §7, §10 | Platform/UI | Advanced | `apps/frontend/`, `apps/backend/` | Submit-to-approval flow | E2E test | Planned |
| DOC-01 | §9, §12, §13 | Labs and evidence | Intermediate | `docs/`, `labs/` | Complete learning path | Documentation review | Planned |
