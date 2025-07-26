
## Voice & NLP Integration Pipeline (as of 2025-07-26)

The Match Event Assistant integrates advanced voice and language technologies to enable hands-free, context-aware event logging and interaction:

- **Hot Word Detection**: (e.g., Porcupine) Listens for a trigger phrase to activate the system.
- **Speech-to-Text (STT)**: Whisper is used for robust, high-quality transcription of spoken commands and event logs. Can run locally or on a server for privacy and reliability.
- **Natural Language Processing (NLP)**: OpenRouter provides access to large language models (LLMs) for understanding, query handling, and advanced conversational features.
- **Text-to-Speech (TTS)**: Kokoro generates natural-sounding audio feedback, confirmations, and responses, allowing the user to interact without looking at a screen.

These components are orchestrated in a modular pipeline:
1. Hot word triggers recording.
2. Whisper transcribes audio to text.
3. OpenRouter processes the text for intent, queries, or actions.
4. Kokoro provides spoken feedback or confirmation.

This architecture supports both local and hybrid (local + cloud) processing for reliability, privacy, and flexibility.

---

## Agentic Context Propagation Principle

Every agent or subordinate is treated as if it is new and has no prior context. When delegating a task, the orchestrator (or any superior agent) must:
- Provide all relevant context, background, and requirements explicitly in the task prompt.
- Pass references to any required files, secrets, or data via shared volumes or explicit arguments.
- Avoid assuming any prior knowledge or state in the subordinate.
- Log all context passed for traceability and reproducibility.

This ensures robust, reproducible, and reliable workflows, especially in multi-agent, parallel, or asynchronous development environments.

For more details, see the [Orchestrator Persona Documentation](/a0/prompts/orchestrator/orchestrator.md).
