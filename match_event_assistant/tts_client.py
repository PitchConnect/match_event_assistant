import requests


class TTSClient:
    def __init__(self, base_url="http://localhost:8880/v1/audio/speech"):
        self.base_url = base_url

    def synthesize(self, text, voice="en", output_path=None):
        payload = {"input": text, "voice": voice}
        response = requests.post(self.base_url, json=payload)
        response.raise_for_status()
        if output_path:
            with open(output_path, "wb") as f:
                f.write(response.content)
        return response.content
