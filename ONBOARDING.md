# ONBOARDING.md

This file provides onboarding instructions for new contributors.

> Created as part of Issue #2: Markdown Formatting Test milestone on 2025-07-27.

Please update with project-specific onboarding steps.

---
**Documentation Standards:**
See [/docs/CANONICAL_STRUCTURE.md](docs/CANONICAL_STRUCTURE.md) for canonical file locations and documentation standards. All contributors must follow these guidelines.

---
**Kokoro-FastAPI TTS Backend**
- This project uses Kokoro-FastAPI as the Text-to-Speech (TTS) backend.
- To set up: Follow the instructions in [Kokoro-FastAPI documentation](https://github.com/kokoro-ai/kokoro-fastapi).
- Ensure the TTS backend is running and accessible before starting the main application.
- Rationale: Kokoro-FastAPI was chosen for its performance, API clarity, and ease of integration.

---
## Mandatory Devcontainer Usage

All contributors are required to use the provided devcontainer for development and testing. This ensures a consistent, reproducible environment, enforces code quality standards (pre-commit, black, flake8), and simplifies onboarding for all team members.

### Rationale
- Guarantees all contributors use the same Python version and dependencies
- Enforces pre-commit hooks and linting automatically
- Reduces setup errors and environment drift
- Simplifies onboarding for new contributors

### Setup Instructions
1. Install [Docker](https://docs.docker.com/get-docker/) and [Visual Studio Code](https://code.visualstudio.com/).
2. Install the [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) for VS Code.
3. Open the project folder in VS Code.
4. When prompted, reopen in the devcontainer. Alternatively, use the Command Palette (Ctrl+Shift+P) and select "Dev Containers: Reopen in Container".
5. Wait for the container to build and initialize. All dependencies and tools will be installed automatically.
6. Run tests and development commands inside the devcontainer terminal.

> Direct local development outside the devcontainer is not supported and may result in failed tests or inconsistent environments.

