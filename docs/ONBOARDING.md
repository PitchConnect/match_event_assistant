# Onboarding: Communication Modules

Welcome! This guide will help you get started contributing to the communication modules (LLMClient, APIClient).

## 1. Environment Setup
- Clone the repository and navigate to the project root.
- Install dependencies:
  ```bash
  pip install -r requirements.txt
  ```

## 2. Understanding the Modules
- **LLMClient**: Handles language model API interactions.
- **APIClient**: Standardizes HTTP API calls to external services.
- See [LLMClient.md](LLMClient.md) and [APIClient.md](APIClient.md) for details.

## 3. Running Tests
- Tests are located in `tests/comms/`.
- Run all tests:
  ```bash
  pytest tests/comms/
  ```

## 4. Extending the Modules
- To add a new LLM provider, subclass `LLMClient` and override `send_prompt`.
- To add a new API endpoint or auth scheme, subclass `APIClient` and override `request`.

## 5. Contribution Guidelines
- Follow PEP8 and project code style.
- Write clear docstrings and comments.
- Add/Update tests for new features.
- Submit pull requests with a clear description.

## 6. Common Pitfalls
- Ensure API keys and secrets are not hardcoded.
- Mock external calls in tests for reliability.

For questions, contact the module maintainer or open an issue.



## Documentation & Output Protocols
- All code, documentation, and logs must be saved in their canonical, version-controlled locations as defined in docs/CANONICAL_STRUCTURE.md.
- When delegating tasks, always provide explicit context: file paths, content summaries, and relevant links.
- Use the delegation checklist in docs/DELEGATION_TEMPLATE.md.
