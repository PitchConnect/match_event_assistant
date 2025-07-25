# Project Overview: Match Event Assistant DevContainer Setup

## Architecture
- **DevContainer**: Python 3.11, pre-commit, pytest, black, flake8, mypy, project dependencies from requirements.txt
- **fogis-api-client**: Runs as a separate service (not included in the devcontainer image)
## DevContainer Details
- Located in `.devcontainer/` directory
- Uses a custom Dockerfile based on the official Python 3.11 devcontainer image
- Installs all required Python tools and project dependencies
- VS Code extensions are recommended for best experience

## Onboarding Steps
1. Clone the repository
2. Open in VS Code and reopen in container
3. Use `docker compose up --build` to start all services
4. Develop and test as usual; code quality tools are pre-installed

## Updating the DevContainer
- Edit `.devcontainer/Dockerfile` or `devcontainer.json` as needed
- Update `requirements.txt` for Python dependencies
- Rebuild the container via VS Code or `docker compose build`
- Communicate changes to your team

## Service Customization
- Update `docker-compose.yaml` to change service images, ports, or environment variables
This setup ensures a consistent, high-quality development environment for all contributors.
