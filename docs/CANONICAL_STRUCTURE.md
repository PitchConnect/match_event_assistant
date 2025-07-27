# CANONICAL_STRUCTURE.md

## Canonical Project Structure

This document defines the canonical directory and file structure for the Match Event Assistant project. All modules, documentation, and onboarding materials must reference and conform to this structure.

### Project Root

- PROJECT_OVERVIEW.md
- CONTRIBUTING.md
- README.md
- LOG.md
- ONBOARDING.md
- ARCHITECTURE.md
- CODE_OF_CONDUCT.md
- docker-compose.yaml
- Dockerfile
- .env.example
- /src/ (core source code modules)
- /tests/ (unit and integration tests)
- /docs/ (project documentation, API docs, architecture, standards)
- /.github/ (workflows, issue/PR templates)
- /data/ (persistent data volumes)

### /src/ Modules
- event_logger.py
- match_state.py
- api_client.py
- tts_client.py
- models.py
- __init__.py

### /docs/ Documentation
- CANONICAL_STRUCTURE.md (this file)
- ARCHITECTURE.md
- LOG.md
- ONBOARDING.md
- APIClient.md
- LLMClient.md
- INTEGRATION_PLAN.md
- VOICE_NLP_AND_CONTEXT.md
- CI_CD_PIPELINE.md

### /tests/
- Unit and integration test scaffolding for all modules

### /.github/
- workflows/ci.yml (CI/CD pipeline)
- workflows/docs.yml (documentation build/test)
- issue and PR templates

## Standards
- All documentation and onboarding must reference this structure.
- Any changes to the canonical structure must be logged in LOG.md and reviewed by coordinators.
- All subordinates must propagate this context downstream and escalate ambiguities.

_Last updated: 2025-07-27 12:12 UTC by Agent Zero_
