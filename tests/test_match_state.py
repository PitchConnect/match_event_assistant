from match_event_assistant.match_state import MatchStateManager


def test_match_state_manager():
    manager = MatchStateManager()
    manager.start_match()
    manager.update_score(team_id=1, increment=2)
    manager.stop_match()
    state = manager.get_state()
    assert state.is_running is False
    assert state.teams[1].score == 2
