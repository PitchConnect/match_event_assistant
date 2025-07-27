# LLMClient Onboarding Guide

## Overview
LLMClient is responsible for interfacing with language model APIs. It provides a unified interface for sending prompts and receiving responses.

## Subclassing
- Inherit from `LLMClient` to implement support for new LLM providers.
- Override the `send_prompt` method for custom API logic.

## Usage Example
```python
from comms.llm_client import LLMClient
client = LLMClient(api_key='YOUR_KEY')
response = client.send_prompt('Hello!')
```

## Integration Points
- Used in the main event processing pipeline for NLP tasks.
- Can be injected into workflow components for modularity.

## Extension
- Add new providers by subclassing and registering in the factory.
