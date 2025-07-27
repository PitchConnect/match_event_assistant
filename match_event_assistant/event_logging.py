"""
Event Logging core module for match_event_assistant.
Provides EventLogger class and event data models.
"""

from dataclasses import dataclass, asdict
from datetime import datetime
from typing import List, Optional
import logging


@dataclass
class MatchEvent:
    """Data model for a match event."""

    timestamp: datetime
    event_type: str
    description: Optional[str] = None
    player_id: Optional[int] = None
    team_id: Optional[int] = None


class EventLogger:
    """
    Core event logger for match events.
    Stores events in memory and provides logging functionality.
    """

    def __init__(self):
        self.events: List[MatchEvent] = []
        self.logger = logging.getLogger("EventLogger")

    def log_event(self, event: MatchEvent) -> None:
        """Log a new match event."""
        self.events.append(event)
        self.logger.info(f"Event logged: {asdict(event)}")

    def get_events(self) -> List[MatchEvent]:
        """Return all logged events."""
        return self.events
