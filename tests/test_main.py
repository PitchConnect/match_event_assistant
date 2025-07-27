from match_event_assistant.main import logger, state_manager, api, analytics
from match_event_assistant.event_logging import MatchEvent
from datetime import datetime


def test_end_to_end(monkeypatch):
    # Log an event
    event = MatchEvent(
        timestamp=datetime.now(), event_type="goal", description="Test goal"
    )
    logger.log_event(event)
    # Update score
    state_manager.update_score(team_id=1, increment=1)

    # Mock API call
    class DummyResp:
        status_code = 200

        def json(self):
            return {"ok": True}

        def raise_for_status(self):
            pass

    def dummy_get(*args, **kwargs):
        return DummyResp()

    monkeypatch.setattr("requests.get", dummy_get)
    resp = api.get("test")
    # Run analytics
    events = logger.get_events()
    result = analytics.summarize_events(events)
    assert resp.status_code == 200
    assert result.summary.startswith("Total events:")
