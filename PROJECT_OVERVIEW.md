# PROJECT_OVERVIEW.md (Reconstructed Draft)

## Project Title: Match Event Assistant

### Purpose & Objectives
- Build a real-time match event logging and analytics system for referees and analysts.
- Enable voice-driven, timestamped event capture, match state management, and post-match analysis.
- Support modular, agentic workflows for automation, extensibility, and collaboration.

### Problem Statement
- Manual event logging is error-prone and distracts from officiating.
- Existing tools lack real-time, context-aware analytics and integration with physiological data.
- Need for a robust, extensible system that supports both live and post-match workflows.

### High-Level Architecture
- **Voice Interface:** Hot word detection, speech-to-text (STT), text-to-speech (TTS).
- **Event Logging Module:** Structured event capture, timestamping, and local persistence.
- **Match State Management:** Voice or manual control of match phases (start, stop, pause, resume).
- **API Integration:** REST client for FOGIS API (match data, rosters, events).
- **Data Models:** Pydantic-based schemas for events, matches, teams, and players.
- **Analytics & Reporting:** Timeline generation, physiological data alignment, and export.
- **Containerization:** Docker, devcontainer, and docker-compose for reproducible environments.

### Directory Structure (Monorepo)
```
match_event_assistant/
├── src/                  # Source code modules
├── tests/                # Unit and integration tests
├── docs/                 # High-level guides, API docs, architecture
├── .devcontainer/        # Dev container config (Dockerfile, devcontainer.json)
├── .github/              # Issue/PR templates, workflows
├── data/                 # Persistent data (volumes)
├── Dockerfile            # Base image for deployment
├── docker-compose.yaml   # Orchestrates dev, API client, etc.
├── .env.example          # Template for environment variables
├── README.md             # Project intro, badges, onboarding
├── PROJECT_OVERVIEW.md   # This file
├── CONTRIBUTING.md       # Contribution guidelines
├── CODE_OF_CONDUCT.md    # Code of conduct
```

### Key Workflows
- **Match State Control:** Voice or manual commands to manage match clock and phases.
- **Event Logging:** Voice-triggered or manual event capture, with second-level precision.
- **Querying:** Voice or text queries for player info, match stats, or event review.
- **Data Persistence:** All events and session data stored locally for review/export.
- **API Integration:** RESTful communication with FOGIS API client (containerized).
- **Analytics:** Align physiological data (e.g., HR from GPX) with match events for reporting.

### Standards & Best Practices
- **Module Interfaces:** Use Pydantic models, type hints, and clear function/class contracts.
- **Naming & Style:** PEP8, descriptive names, robust error handling.
- **Documentation:** In-code docstrings, Markdown guides, auto-generated API docs (MkDocs).
- **Contribution:** PRs, code reviews, branching, onboarding checklist, issue/PR templates.
- **Containerization:** All development in Docker/devcontainer, persistent data via volumes.

### Onboarding & Development
- Clone repo, open in VS Code (or compatible editor) with devcontainer support.
- Build and start all services via `docker-compose up`.
- Install dependencies, run pre-commit hooks, and follow onboarding checklist in README.
- Use `.env` for secrets and environment variables (never commit real secrets).

### Documentation Strategy
- All modules and APIs documented with docstrings and Markdown.
- MkDocs for building browsable documentation from `/docs` and codebase.
- Badges in README for CI, coverage, Python version, etc.

- Begin implementation of core modules and tests.
- Expand documentation and onboarding as features are added.

### Next Steps & Roadmap

The following planning and project management tasks have been created as actionable GitHub issues. Please refer to each for detailed steps, goals, and references.

- [Module Implementation Roadmaps: Event Logging, Match State, API Integration, Analytics](https://github.com/PitchConnect/match_event_assistant/issues/3)
- [Test Coverage and Quality Assurance Strategy](https://github.com/PitchConnect/match_event_assistant/issues/4)
- [CI/CD Pipeline and Automation Planning](https://github.com/PitchConnect/match_event_assistant/issues/5)
- [Documentation Automation and Standards Enforcement](https://github.com/PitchConnect/match_event_assistant/issues/6)
- [Milestone and Development Roadmap Planning](https://github.com/PitchConnect/match_event_assistant/issues/7)

_Last updated: 2025-07-26 07:49:25_

---

**If you want to restore or refine any specific section, or need a more detailed breakdown (e.g., module APIs, onboarding steps, standards), let me know and I’ll expand or adjust as needed.**

---
_Last reviewed and updated by Agent Zero on 2025-07-26 07:46:20_

See also: docs/VOICE_NLP_AND_CONTEXT.md for details on the voice/NLP pipeline and agentic context propagation standards.


## Milestone and Development Roadmap

This roadmap defines the actionable milestones and development plan for the match_event_assistant project. All contributors must ensure strict context propagation, real-time logging, and continuous documentation updates across all canonical sources: `PROJECT_OVERVIEW.md`, `CONTRIBUTING.md`, `README.md`, `LOG.md`, `ONBOARDING.md`, `ARCHITECTURE.md`, and the issue tracker. All progress, decisions, and changes must be logged in real time in the main chat and reflected in the documentation.

### Milestone Zero: Full Visibility (Due: 2025-08-10)
**Objective:** Launch parallel, autonomous development with full transparency and milestone logs in main chat.

**Epics/Issues:**
- [ ] Establish real-time logging in main chat for all development activities and decisions.
- [ ] Audit and update all documentation files (`PROJECT_OVERVIEW.md`, `CONTRIBUTING.md`, `README.md`, `LOG.md`, `ONBOARDING.md`, `ARCHITECTURE.md`) to ensure they reflect current project state and standards.
- [ ] Set up and document the canonical issue tracker workflow for milestone and issue tracking.
- [ ] Define and enforce context propagation protocols for all contributors and agents.
- [ ] Confirm all contributors understand and follow the context propagation and logging requirements.

### Milestone 1: TTS Client Integration
**Objective:** Integrate the TTS client module with Kokoro-FastAPI and document the process.

**Epics/Issues:**
- [ ] Implement the TTS client module for Kokoro-FastAPI.
- [ ] Write and run integration and unit tests for the TTS client.
- [ ] Update `README.md` and `PROJECT_OVERVIEW.md` with TTS client usage, deployment, and configuration instructions.
- [ ] Add a docker-compose example for Kokoro-FastAPI in documentation.
- [ ] Log all progress and decisions in `LOG.md` and the main chat.

### Milestone 2: Event Logging Core Module
**Objective:** Scaffold and implement the event logging core module with minimal viable functionality.

**Epics/Issues:**
- [ ] Design and scaffold the event logging core module.
- [ ] Implement minimal event logging functionality and tests.
- [ ] Document architecture and usage in `ARCHITECTURE.md` and `README.md`.
- [ ] Update onboarding and contribution guidelines to reflect new module.
- [ ] Ensure all changes are logged in real time and context is propagated.

### Milestone 3: End-to-End Workflow Integration
**Objective:** Integrate TTS and event logging modules into the main match_event_assistant workflow.

**Epics/Issues:**
- [ ] Integrate TTS and event logging modules.
- [ ] Conduct end-to-end tests and document results.
- [ ] Update all relevant documentation and onboarding materials.
- [ ] Log integration process and outcomes in main chat and `LOG.md`.

### Milestone 4: Production Readiness & Continuous Improvement
**Objective:** Achieve production readiness and establish a process for continuous improvement.

**Epics/Issues:**
- [ ] Conduct code review, security audit, and performance testing.
- [ ] Finalize and freeze documentation for initial release.
- [ ] Establish a process for ongoing issue triage, milestone review, and roadmap updates.
- [ ] Ensure all context and logs are up to date and accessible.

---

#### Ongoing Instructions
- **Review and Update:** All milestones, issues, and documentation must be reviewed and updated as the project evolves. Contributors are responsible for propagating context and maintaining real-time logs.
- **Canonical Sources:** All changes must be reflected in `PROJECT_OVERVIEW.md`, `CONTRIBUTING.md`, `README.md`, `LOG.md`, `ONBOARDING.md`, `ARCHITECTURE.md`, and the issue tracker.
- **Context Propagation:** Strictly enforce context propagation and real-time logging for all development activities.

> _This roadmap is a living document. Review and update milestones, issues, and documentation regularly to ensure alignment with project goals and transparency._
