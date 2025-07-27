# Contributing

This file contains contribution guidelines, code standards, and contact information.


---
**Documentation Standards:**
See [/docs/CANONICAL_STRUCTURE.md](docs/CANONICAL_STRUCTURE.md) for canonical file locations and documentation standards. All contributors must follow these guidelines.
## Testing Standards and Coverage Requirements

- All code must be tested using pytest.
- Tests are located in the `tests/` directory, with `unit/` and `integration/` subdirectories.
- Use `pytest` and `pytest-cov` for running tests and measuring coverage.
- Minimum coverage for all modules: 80%. All public functions/classes must be tested.
- To run tests with coverage: `pytest --cov=match_event_assistant --cov-report=xml --cov-report=term-missing tests/`
- Coverage is enforced in CI. Pull requests must not decrease coverage below the target.
- All changes must go through pull requests with code review and passing CI checks.

---
## Devcontainer Requirement

All code contributions must be developed and tested within the provided devcontainer. This is mandatory for all pull requests.

- The devcontainer enforces code quality and testing standards.
- Pre-commit hooks, black, and flake8 are installed and required.
- Pull requests from outside the devcontainer will not be accepted.

See ONBOARDING.md for setup instructions.
