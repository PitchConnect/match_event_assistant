# Match Event Assistant

Real-time match event logging and analytics assistant for referees and analysts.

## Development Environment (VS Code DevContainer)

This project uses a [VS Code DevContainer](https://code.visualstudio.com/docs/remote/containers) for a reproducible Python 3.11 development environment with pre-commit, pytest, black, flake8, and mypy.

### Quick Start

1. **Clone the repository**
2. **Open in VS Code**
3. **Reopen in Container** (VS Code will prompt you, or use the Command Palette: `Dev Containers: Reopen in Container`)
4. **Install dependencies** (if not already):
```sh
pip install -r requirements.txt
```
5. **Run tests**:
```sh
pytest
```

```sh
docker compose up --build
```

### Code Quality
- [pre-commit](https://pre-commit.com/) hooks are installed automatically.
- Run `black`, `flake8`, and `mypy` manually or via pre-commit.

### Recommended VS Code Extensions
- Python (ms-python.python)
- Docker (ms-azuretools.vscode-docker)
- Dev Containers (ms-vscode-remote.remote-containers)

---

For more details, see [PROJECT_OVERVIEW.md](./PROJECT_OVERVIEW.md).

