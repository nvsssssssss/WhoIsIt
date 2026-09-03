# ADR 0001: Repository Structure

## Status

Accepted

## Context

WhoIsIt will contain multiple parts of the project, including the backend, frontend, data pipeline, documentation, and tests.

We need a repository structure that keeps these components organized while allowing them to be developed together.

## Decision

WhoIsIt will initially use a single repository (monorepo).

The repository will use separate directories for the major components:

~~~text
WhoIsIt/
├── backend/
├── frontend/
├── data-pipeline/
├── docs/
└── tests/
~~~

## Rationale

A monorepo is appropriate for the current stage because:

- The project is being developed as one system.
- Backend, frontend, data, and tests will evolve together.
- Documentation can be maintained alongside the code.
- Changes across multiple components can be tracked in one repository.
- The current project size does not justify multiple repositories.

## Consequences

### Positive

- Simple project management
- Clear separation between major components
- Easier coordination between components
- One place for project history and documentation

### Negative

- The repository will grow as the project expands.
- Component boundaries need to be maintained carefully.
- Large datasets should not be committed directly to the repository unless appropriate.

## Future Review

This decision can be revisited if the project grows enough that separate repositories provide a clear advantage.