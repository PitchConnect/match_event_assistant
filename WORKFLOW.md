
# Project Workflow (auto-generated 2025-07-27)

This project enforces the following development workflow:

- All code changes must be submitted via Pull Requests (PRs) targeting the main branch.
- Every PR must be reviewed and approved by at least one reviewer before merging.
- Pre-commit hooks (black, flake8, hygiene) must pass before commits are accepted.
- Continuous Integration (CI) checks (lint, test) must pass before merging.
- All contributors must use the provided development container for consistency.
- The workflow is subject to change; see CONTRIBUTING.md for details.

## Issue and Milestone Management

- Regularly review all open issues (at least at the end of each milestone or sprint).
- Close issues that are resolved, obsolete, or no longer relevant.
- Update issue comments with a summary of actions taken before closing.
- Ensure milestones reflect current project priorities and are updated or closed as needed.
- All contributors and agents are responsible for maintaining issue hygiene as part of the workflow.


## ⚠️ Workflow Enforcement Status (as of 2025-07-27)

- The following workflow is documented and strongly recommended for all contributors:
    - All changes should be submitted via Pull Requests (PRs).
    - Every PR must be reviewed and approved by at least one other contributor before merging.
    - Pre-commit hooks and CI checks should pass before merging.
    - Issues and milestones should be used to track progress and context.
- **Technical enforcement (branch protection, mandatory reviewer assignment) is NOT currently active.**
- Until branch protection is enabled, we trust contributors to follow this process by convention.
- Repository admins will enable technical enforcement in the near future. This section will be updated accordingly.


## 🚦 Branch Protection Enforcement (as of 2025-07-27)
- Direct pushes to the `main` branch are now **blocked** by GitHub branch protection rules. All changes must go through Pull Requests (PRs).
- **Mandatory reviewer assignment is not enforced** due to the use of a shared Personal Access Token (PAT) for all agents and the user.
- Contributors are still expected to follow the documented workflow: PRs, reviews (where possible), pre-commit and CI checks, and issue/milestone management.
- This enforcement will be reviewed if/when individual credentials are introduced.
