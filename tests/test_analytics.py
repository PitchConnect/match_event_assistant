from match_event_assistant.analytics import Analytics, AnalyticsResult


def test_summarize_events():
    analytics = Analytics()
    events = [1, 2, 3]
    result = analytics.summarize_events(events)
    assert isinstance(result, AnalyticsResult)
    assert result.summary == "Total events: 3"
