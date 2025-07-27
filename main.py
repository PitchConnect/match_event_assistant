import logging
import os
import sys

sys.path.insert(0, "/a0/dev")

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
"""
main.py - Entry point for Match Event Assistant

- Loads environment variables from .env (using python-dotenv if available)





- Logs all progress and errors
- Provides main() and CLI entry point
- Fully documented and ready for extension
"""

# Load environment variables from .env if python-dotenv is available
try:
    from dotenv import load_dotenv

    load_dotenv()
    logging.info("Loaded environment variables from .env")
except ImportError:
    logging.warning("python-dotenv not installed; skipping .env loading.")

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)],
)
logger = logging.getLogger("match_event_assistant.main")

# Import communication clients
try:
    from match_event_assistant.communication.llm_client import LLMClient
    from match_event_assistant.communication.api_client import APIClient
    from match_event_assistant.communication.tts_client import TTSClient
except ImportError as e:
    logger.error(f"Failed to import communication clients: {e}")
    sys.exit(1)


def main():
    """
    Main workflow for Match Event Assistant.
    Demonstrates basic data flow between LLM, API, and TTS clients.
    """
    logger.info("Starting Match Event Assistant main workflow.")
    try:
        # Instantiate clients (replace with actual config as needed)
        llm_client = LLMClient()
        api_client = APIClient()
        tts_client = TTSClient()

        # Example prompt and data flow
        prompt = "What is the next match event?"
        logger.info(f"Sending prompt to LLMClient: {prompt}")
        llm_response = llm_client.send_message(prompt)
        logger.info(f"LLMClient response: {llm_response}")

        logger.info("Fetching event data from APIClient.")
        api_data = api_client.query("test-endpoint")
        logger.info(f"APIClient data: {api_data}")

        response_text = f"LLM says: {llm_response}. Event data: {api_data}"
        logger.info(f"Synthesizing response with TTSClient: {response_text}")
        tts_client.synthesize(response_text)
        logger.info("Workflow completed successfully.")
    except Exception as e:
        logger.error(f"Error in main workflow: {e}", exc_info=True)
        sys.exit(1)


if __name__ == "__main__":
    main()

from match_event_assistant.event_type_loader import EventTypeLoader

event_type_loader = EventTypeLoader()
