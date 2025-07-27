import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class TTSClient:
    def __init__(self, *args, **kwargs):
        logger.info(f"TTSClient initialized with args={args}, kwargs={kwargs}")

    def synthesize(self, text, **kwargs):
        logger.info(f"TTSClient.synthesize called with text: {text}, kwargs: {kwargs}")
        mock_audio_path = "/tmp/mock_tts_output.wav"
        return f"[MOCK TTS OUTPUT] Audio synthesized and saved to {mock_audio_path}"
