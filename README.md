# Match Event Assistant

Real-time match event logging and analytics assistant for referees and analysts.

## Development Environment (VS Code DevContainer)
**All development MUST be performed inside the devcontainer. Pre-commit hooks and CI checks are enforced for every push and pull request.**

- Pre-commit is installed and activated automatically.
- All code must pass pre-commit and tests (see .github/workflows/ci.yml).
- Direct pushes to main are discouraged; use pull requests.


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



## [2025-07-27] Architecture Update: Kokoro-FastAPI TTS Service Integration

We have integrated [Kokoro-FastAPI](https://github.com/remsky/Kokoro-FastAPI) as our text-to-speech (TTS) service. This service runs as a container alongside our main application and exposes OpenAI-compatible endpoints for generating speech audio from text. Key features:
- Multi-language support (English, Japanese, Chinese, more coming)
- Voice mixing, streaming, and real-time playback
- OpenAI-style API for easy integration
- Dockerized for CPU/GPU deployment

**Integration details:**
- The service is defined in our `docker-compose.yaml` as `kokoro-tts` (see below for example).
- Our application communicates with Kokoro-FastAPI via HTTP requests to `/v1/audio/speech`.
- A client module will be developed to handle TTS requests and responses.

**Example docker-compose service:**
```yaml
  kokoro-tts:
    image: ghcr.io/remsky/kokoro-fastapi-cpu:latest
    ports:
      - "8880:8880"
    environment:
      - TZ=Europe/Stockholm
    restart: unless-stopped
```

**Next steps:**
- Implement a TTS client module for seamless integration.
- Document usage and configuration in onboarding materials.
- Optionally, expose the Kokoro web UI for local testing at `http://localhost:8880/web`.

## TTS Client Usage

The `TTSClient` module provides integration with the Kokoro-FastAPI TTS service.

Example usage:
```python
from match_event_assistant.tts_client import TTSClient
client = TTSClient()
audio = client.synthesize("Hello, world!", voice="en", output_path="output.wav")
```

## TTS Client Usage

The `TTSClient` module provides integration with the Kokoro-FastAPI TTS service.

Example usage:
```python
from match_event_assistant.tts_client import TTSClient
client = TTSClient()
audio = client.synthesize("Hello, world!", voice="en", output_path="output.wav")
```

## Event Logging Module Usage

The `EventLogger` class provides in-memory logging of match events.

Example usage:
```python
from match_event_assistant.event_logging import EventLogger, MatchEvent
from datetime import datetime

logger = EventLogger()
event = MatchEvent(timestamp=datetime.now(), event_type="goal", description="Scored by player 10", player_id=10, team_id=1)
logger.log_event(event)
print(logger.get_events())
```

## Match State Management Module Usage

The `MatchStateManager` class manages the current state of the match (score, time, period, teams, players).

Example usage:
```python
from match_event_assistant.match_state import MatchStateManager

manager = MatchStateManager()
manager.start_match()
manager.update_score(team_id=1, increment=2)
manager.stop_match()
state = manager.get_state()
print(state)
```

## API Integration Module Usage

The `APIIntegration` class provides a simple interface for REST API calls.

Example usage:
```python
from match_event_assistant.api_integration import APIIntegration

api = APIIntegration(base_url="http://localhost")
response = api.get("test")
print(response)
```

## Analytics Module Usage

The `Analytics` class provides basic analytics for match events and state.

Example usage:
```python
from match_event_assistant.analytics import Analytics

analytics = Analytics()
events = [1, 2, 3]
result = analytics.summarize_events(events)
print(result)
```
