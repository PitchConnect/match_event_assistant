# Onboarding Instructions

## Pre-commit Hooks
- Ensure .pre-commit-config.yaml is present in the project root.
- Run Requirement already satisfied: pre-commit in /opt/venv/lib/python3.12/site-packages (4.2.0)
Requirement already satisfied: cfgv>=2.0.0 in /opt/venv/lib/python3.12/site-packages (from pre-commit) (3.4.0)
Requirement already satisfied: identify>=1.0.0 in /opt/venv/lib/python3.12/site-packages (from pre-commit) (2.6.12)
Requirement already satisfied: nodeenv>=0.11.1 in /opt/venv/lib/python3.12/site-packages (from pre-commit) (1.9.1)
Requirement already satisfied: pyyaml>=5.1 in /opt/venv/lib/python3.12/site-packages (from pre-commit) (6.0.2)
Requirement already satisfied: virtualenv>=20.10.0 in /opt/venv/lib/python3.12/site-packages (from pre-commit) (20.32.0)
Requirement already satisfied: distlib<1,>=0.3.7 in /opt/venv/lib/python3.12/site-packages (from virtualenv>=20.10.0->pre-commit) (0.4.0)
Requirement already satisfied: filelock<4,>=3.12.2 in /opt/venv/lib/python3.12/site-packages (from virtualenv>=20.10.0->pre-commit) (3.13.1)
Requirement already satisfied: platformdirs<5,>=3.9.1 in /opt/venv/lib/python3.12/site-packages (from virtualenv>=20.10.0->pre-commit) (4.3.8) if not already installed.
- Run pre-commit installed at .git/hooks/pre-commit in the project root to activate git hooks.
- Hooks will run automatically on each commit to enforce code standards (black, flake8, hygiene).

## Devcontainer Setup
- The .devcontainer/ directory contains Dockerfile and devcontainer.json for VS Code Remote Containers or compatible environments.
- The devcontainer installs pre-commit, black, and flake8 automatically.

## Documentation
- LOG.md, ONBOARDING.md, and ARCHITECTURE.md are maintained in the project root.
- For extended documentation, see the docs/ directory.

## Troubleshooting
- If pre-commit fails to install, ensure you are in a git repository (Reinitialized existing Git repository in /a0/dev/match_event_assistant/.git/ if needed).
- For further help, consult LOG.md for recent actions and milestones.
