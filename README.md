# Match Event Assistant

A real-time match event logging and analytics system for referees and analysts.

## Quickstart
- Clone the repository and open in VS Code (or compatible editor) with devcontainer support.
- Build and start all services via `docker-compose up`.
- Install dependencies, run pre-commit hooks, and follow onboarding checklist.
- See PROJECT_OVERVIEW.md and CONTRIBUTING.md for standards, architecture, and contribution guidelines.

## Documentation
- All modules and APIs are documented with docstrings and Markdown.
- See /docs and PROJECT_OVERVIEW.md for architecture and workflow details.

## Badges
- [CI Status](#) [Coverage](#) [Python 3.11+](#)

---

For more information, see PROJECT_OVERVIEW.md, CONTRIBUTING.md, and the issue tracker.

## Minimal CLI Test Interface

A minimal, interactive text-based CLI is provided for manual scenario testing of the match_event_assistant system before TTS/STT features are added.

### How to Start

```bash
python cli_test.py
```

### Available Commands

- `simulate_event <event_description>`: Simulate a match event and see the system's (mocked) response.
- `help` or `?`: List available commands.
- `exit` or `Ctrl-D`: Exit the CLI.

### Example Session

```
$ python cli_test.py
Welcome to the Match Event Assistant CLI. Type help or ? to list commands.
(match-event) simulate_event goal by team A
Simulating event: goal by team A
System response: [Mocked response for "goal by team A"]
(match-event) exit
Exiting Match Event Assistant CLI.
```

---

The CLI is designed for easy extension and manual scenario testing.


## PitchConnect match_event_assistant CLI Usage & Integration

### Setup Instructions

1. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
2. **(Optional) Set environment variables:**
   - `FOGIS_API_KEY`: Your API key for the fogis API
   - `FOGIS_API_BASE_URL`: Base URL for the fogis API (if not default)

3. **Run the CLI:**
   ```sh
   python cli.py <command> [options]
   ```

### Available Commands

- `get-match <match_id>`: Fetch match metadata
- `get-events <match_id>`: Fetch event timeline
- `get-roster <match_id>`: Fetch team rosters
- `get-officials <match_id>`: Fetch match officials

### Global Options

- `--output [json|table|yaml]`   Output format (default: json)
- `--api-key <key>`              API key (overrides env var)
- `--base-url <url>`             API base URL (overrides env var)
- `--timeout <seconds>`          API timeout in seconds (default: 10)
- `--debug`                      Show debug info on error

### Command Examples

```sh
python cli.py get-match 12345 --output table
python cli.py get-events 12345 --api-key $FOGIS_API_KEY
python cli.py get-roster 12345 --output yaml
python cli.py get-officials 12345 --timeout 5
```

### Error Handling

- **API/network errors:**
  - User-friendly error message is printed to stderr
  - CLI exits with code 2
- **Invalid arguments:**
  - Usage/help is printed, CLI exits with code 1
- **Debug mode:**
  - Use `--debug` to print stack traces for troubleshooting

### Extension Points

- **Add new commands:**
  - Define a new subcommand in `cli.py` and implement the corresponding method in `communication/api_client.py`
- **Add new output formats:**
  - Extend the `print_output` function in `cli.py`
- **API integration:**
  - Update or extend `APIClient` for new endpoints or authentication methods

### Integration Notes

- The CLI is designed for both end users and developers.
- Can be scripted or integrated into larger workflows.
- All commands and options are documented via `--help`.

---

For more details, see the top of this README or consult module-level documentation.
