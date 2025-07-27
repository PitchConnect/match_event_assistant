# Communication Modules: LLMClient & APIClient

This directory contains the core communication modules for the Match Event Assistant project.

## Modules
- **LLMClient**: Unified interface for language model APIs (NLP tasks).
- **APIClient**: Standardized HTTP API client for external services.

## Quickstart

```bash
# Install dependencies
pip install -r requirements.txt
```

### Example Usage

#### APIClient
```python
from comms.api_client import APIClient
client = APIClient(base_url="https://api.example.com")
data = client.request("GET", "/events")
```

#### LLMClient
```python
from comms.llm_client import LLMClient
client = LLMClient(api_key="YOUR_KEY")
response = client.send_prompt("Hello!")
```

## Documentation
- [ONBOARDING.md](ONBOARDING.md): Step-by-step onboarding for contributors
- [ARCHITECTURE.md](ARCHITECTURE.md): Design rationale and integration
- [APIClient.md](APIClient.md), [LLMClient.md](LLMClient.md): Module details
