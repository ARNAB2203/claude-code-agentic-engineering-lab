# Decisions

## ADR-001: Treat the supplied file as a project brief

**Decision:** Do not represent the pasted master prompt as the missing reference document it describes.

**Rationale:** It has no source-specific pages or material to extract. This preserves truthful coverage and allows later source-specific supplementation.

## ADR-002: Start with a mock agent provider

**Decision:** The first runnable workflow will use a visibly labelled mock provider behind a provider interface.

**Rationale:** No provider credentials are present, and simulated runs must never be displayed as genuine Claude execution.

## ADR-003: Keep publication private by default

**Decision:** Do not create, push to, or make public a repository until GitHub authentication works and publication is explicitly verified.

**Rationale:** The existing named remote must not be overwritten; `gh` authentication is currently invalid.
