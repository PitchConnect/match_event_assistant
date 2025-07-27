# APIClient Onboarding Guide

## Overview
APIClient standardizes HTTP API communication for external services (e.g., sports data, notifications).

## Subclassing
- Inherit from `APIClient` to add new endpoints or authentication schemes.
- Override `request` for custom logic.

## Usage Example
```python
from comms.api_client import APIClient
client = APIClient(base_url='https://api.example.com')
data = client.request('GET', '/events')
```

## Integration Points
- Used for all external API calls in the workflow.
- Designed for easy mocking in tests.

## Extension
- Add retry logic, error handling, or new auth methods as needed.
