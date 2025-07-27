import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class APIClient:
    def __init__(self, *args, **kwargs):
        logger.info(f"APIClient initialized with args={args}, kwargs={kwargs}")

    def query(self, endpoint, params=None, **kwargs):
        logger.info()
        return {
            "status": "success",
            "data": {"mock_key": "mock_value"},
            "endpoint": endpoint,
            "params": params,
        }
