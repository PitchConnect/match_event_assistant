from match_event_assistant.event_logging import EventLogger, MatchEvent
from datetime import datetime


def test_log_and_get_events():
    logger = EventLogger()
    event = MatchEvent(
        timestamp=datetime.utcnow(),
        event_type="goal",
        description="Test goal",
        player_id=10,
        team_id=1,
    )
    logger.log_event(event)
    events = logger.get_events()
    assert len(events) == 1
    assert events[0].event_type == "goal"
