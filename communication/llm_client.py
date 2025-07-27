import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class LLMClient:
    def __init__(self, *args, **kwargs):
        logger.info(f"LLMClient initialized with args={args}, kwargs={kwargs}")

    def send_message(self, message, **kwargs):
        logger.info(
            f"LLMClient.send_message called with message: {message}, kwargs: {kwargs}"
        )
        return "[MOCK LLM RESPONSE] This is a mock response from the LLMClient."
