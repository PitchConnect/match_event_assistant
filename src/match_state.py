"""
Match state management: handles match start, stop, pause, and resume.
"""

from typing import Optional


def start_match(match_id: str) -> None:
    """Record the start of a match."""
    pass


def stop_match(match_id: str) -> None:
    """Record the end of a match."""
    pass


def pause_match(match_id: str) -> None:
    """Pause the match timer."""
    pass


def resume_match(match_id: str) -> None:
    """Resume the match timer."""
    pass


def get_match_time(match_id: str) -> Optional[int]:
    """Get the current match time in seconds."""
    pass
