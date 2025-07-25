"""
Event logging module: handles creation, storage, and retrieval of match events.
"""
from .models import MatchEvent
from typing import List

def log_event(event: MatchEvent) -> None:
    """Log a new match event."""
    pass

def get_events(match_id: str) -> List[MatchEvent]:
    """Retrieve all events for a given match."""
    pass
