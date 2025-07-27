from dataclasses import dataclass, asdict
from datetime import datetime
from typing import Optional
import logging
from match_event_assistant.event_type_loader import EventTypeLoader

@dataclass
class MatchEvent:
    timestamp: datetime
    event_type: str
    event_type_id: int
    description: Optional[str] = None
    player_id: Optional[int] = None
    team_id: Optional[int] = None

    def validate(self, loader: EventTypeLoader):
        loader.validate(self.event_type, self.event_type_id)

class EventLogger:
    def __init__(self, loader: EventTypeLoader):
        self.events = []
        self.logger = logging.getLogger("EventLogger")
        self.loader = loader

    def log_event(self, event: MatchEvent) -> None:
        try:
            event.validate(self.loader)
            self.events.append(event)
            self.logger.info(f"Event logged: {asdict(event)}")
        except ValueError as e:
            self.logger.error(f"Event validation failed: {e}")
            raise

    def get_events(self):
        return self.events
