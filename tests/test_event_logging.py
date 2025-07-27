from match_event_assistant.event_logging import EventLogger, MatchEvent
from match_event_assistant.event_type_loader import EventTypeLoader
from datetime import datetime
import pytest

event_type_loader = EventTypeLoader()

def test_log_valid_event():
    logger = EventLogger(event_type_loader)
    event = MatchEvent(
        timestamp=datetime.utcnow(),
        event_type="regular_goal",
        event_type_id=6,
        description="Test regular goal",
        player_id=10,
        team_id=1,
    )
    logger.log_event(event)
    events = logger.get_events()
    assert len(events) == 1
    assert events[0].event_type == "regular_goal"
    assert events[0].event_type_id == 6

def test_log_event_invalid_type():
    logger = EventLogger(event_type_loader)
    event = MatchEvent(
        timestamp=datetime.utcnow(),
        event_type="invalid_type",
        event_type_id=999,
        description="Invalid event type",
        player_id=10,
        team_id=1,
    )
    with pytest.raises(ValueError, match="Invalid event_type"):
        logger.log_event(event)

def test_log_event_mismatched_id():
    logger = EventLogger(event_type_loader)
    event = MatchEvent(
        timestamp=datetime.utcnow(),
        event_type="regular_goal",
        event_type_id=999,
        description="Mismatched event_type_id",
        player_id=10,
        team_id=1,
    )
    with pytest.raises(ValueError, match="does not match event_type"):
        logger.log_event(event)
