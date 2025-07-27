from match_event_assistant.tts_client import TTSClient


def test_tts_client_init():
    client = TTSClient()
    assert client.base_url.startswith("http")
