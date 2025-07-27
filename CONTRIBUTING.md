# Contributing Guidelines

Thank you for your interest in contributing! This project values clear communication, code quality, and a welcoming, collaborative environment. Please read these guidelines before making your first contribution.

## How to Contribute
- **Fork the repository** and create a feature branch from `main` (e.g., `feature/your-feature-name`).
- **Write clear, well-documented code** following our code style standards (see below).
- **Add or update tests** for your changes if applicable.
- **Run pre-commit hooks** to check formatting, linting, and type safety before pushing.
- **Open a Pull Request (PR)** to `main` with a clear description of your changes and reference any related issues.
- **Participate in code review**: respond to feedback and make requested changes.

## Branching & PR Process
- Use feature branches for new work (e.g., `feature/voice-logging`), and bugfix branches for fixes (e.g., `bugfix/fix-logging-error`).
- Keep PRs focused and small; large changes should be split into multiple PRs if possible.
- All PRs require at least one review before merging.

## Code Style & Quality
- **Formatting:** Use [Black](https://black.readthedocs.io/) for code formatting.
- **Linting:** Use [Ruff](https://docs.astral.sh/ruff/) or [Flake8](https://flake8.pycqa.org/) for linting.
- **Type Checking:** Use [mypy](http://mypy-lang.org/) or [pyright](https://github.com/microsoft/pyright) for static type checking.
- **Pre-commit:** Install and use pre-commit hooks to automate checks before each commit.
- **Docstrings:** All public classes, functions, and modules must have clear docstrings.
- **Tests:** Add or update tests for new features or bugfixes.

## Development Environment
- **Python version:** 3.11+
- **Virtual environment:** Use `venv` or `virtualenv` for local development.
- **Docker:** Use provided Dockerfiles and `docker-compose.yml` for containerized development and testing.
- **Pre-commit:** Install with `pip install pre-commit` and run `pre-commit install` after cloning.
- See the root README and `/docs` for more setup details.

## Issue & PR Templates
- Use the provided templates for issues and PRs to ensure all relevant information is included.

## Code of Conduct
- All contributors are expected to follow our [Code of Conduct](CODE_OF_CONDUCT.md).

## Need Help?
- If you have questions, open an issue or ask in the project discussions.

---
Thank you for helping make this project better!

For onboarding and environment setup, see the Quickstart section in the [README.md](README.md).
