import pytest
import os
import subprocess
import sys

sys.path.insert(0, "/a0/dev/match_event_assistant")


def run_cli(args, env=None):
    cmd = [sys.executable, "/a0/dev/match_event_assistant/cli.py"] + args
    result = subprocess.run(cmd, capture_output=True, text=True, env=env)
    return result


@pytest.mark.parametrize(
    "command,match_id",
    [
        ("get-match", "12345"),
        ("get-events", "12345"),
        ("get-roster", "12345"),
        ("get-officials", "12345"),
    ],
)
def test_cli_success(command, match_id):
    result = run_cli([command, match_id, "--output", "json"])
    assert result.returncode == 0
    assert "mock_key" in result.stdout or "success" in result.stdout


@pytest.mark.parametrize(
    "command",
    [
        "get-match",
        "get-events",
        "get-roster",
        "get-officials",
    ],
)
def test_cli_error_missing_id(command):
    result = run_cli([command], env=os.environ.copy())
    assert result.returncode != 0
    assert "usage:" in result.stderr or "error" in result.stderr or result.stdout


def test_cli_invalid_command():
    result = run_cli(["invalid-cmd"], env=os.environ.copy())
    assert result.returncode != 0
    assert "usage:" in result.stderr or "error" in result.stderr or result.stdout


# Example of error simulation via env var
def test_cli_api_error():
    env = os.environ.copy()
    env["FOGIS_API_FORCE_ERROR"] = "1"
    result = run_cli(["get-match", "failid", "--output", "json"], env=env)
    assert result.returncode == 2
    assert "Simulated API error" in result.stderr or result.stdout
