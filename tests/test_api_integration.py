from match_event_assistant.api_integration import APIIntegration, APIResponse


def test_api_integration_get(monkeypatch):
    class DummyResp:
        status_code = 200

        def json(self):
            return {"ok": True}

        def raise_for_status(self):
            pass

    def dummy_get(*args, **kwargs):
        return DummyResp()

    monkeypatch.setattr("requests.get", dummy_get)
    api = APIIntegration(base_url="http://localhost")
    resp = api.get("test")
    assert isinstance(resp, APIResponse)
    assert resp.status_code == 200
    assert resp.data == {"ok": True}
