import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class APIClient:
    def __init__(self, *args, **kwargs):
        logger.info(f"APIClient initialized with args={args}, kwargs={kwargs}")

    def get_match(self, match_id, **kwargs):
        import os

        if os.environ.get("FOGIS_API_FORCE_ERROR") == "1":
            raise Exception("Simulated API error (FOGIS_API_FORCE_ERROR)")
        """Fetch match metadata by match_id"""
        endpoint = f"/matches/{match_id}"
        return self.query(endpoint, **kwargs)

    def get_events(self, match_id, **kwargs):
        import os

        if os.environ.get("FOGIS_API_FORCE_ERROR") == "1":
            raise Exception("Simulated API error (FOGIS_API_FORCE_ERROR)")
        """Fetch event timeline for a match"""
        endpoint = f"/matches/{match_id}/events"
        return self.query(endpoint, **kwargs)

    def get_roster(self, match_id, **kwargs):
        import os

        if os.environ.get("FOGIS_API_FORCE_ERROR") == "1":
            raise Exception("Simulated API error (FOGIS_API_FORCE_ERROR)")
        """Fetch team rosters for a match"""
        endpoint = f"/matches/{match_id}/roster"
        return self.query(endpoint, **kwargs)

    def get_officials(self, match_id, **kwargs):
        import os

        if os.environ.get("FOGIS_API_FORCE_ERROR") == "1":
            raise Exception("Simulated API error (FOGIS_API_FORCE_ERROR)")
        """Fetch match officials"""
        endpoint = f"/matches/{match_id}/officials"
        return self.query(endpoint, **kwargs)

    def query(self, endpoint, params=None, **kwargs):
        logger.info(f"Querying endpoint: {endpoint}, params: {params}")
        return {
            "status": "success",
            "data": {"mock_key": "mock_value"},
            "endpoint": endpoint,
            "params": params,
        }
