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
