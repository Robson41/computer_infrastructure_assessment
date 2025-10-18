<!--
Purpose: concise, actionable instructions to help AI coding agents be immediately productive in this repository.
Keep this file short (20–50 lines) and repository-specific. Update when the repo acquires source code or CI.
-->
# Copilot / AI agent instructions — computer_infrastructure_assessment

Summary
- This repository currently contains only a top-level `README.md` with the project title.
- Default branch: `main`. There are no source files, package manifests (no `package.json`, `pyproject.toml`, or `requirements.txt`), and no CI workflows under `.github/workflows/`.

What this means for an AI agent
- There is no established language, build, or test system to infer. Any code or scaffolding you add should include a manifest and README updates describing how to build and test it.
- When making non-trivial changes, create a feature branch off `main`, include a short PR description, and update `README.md` to document commands you introduce.

Quick actionable checklist for first contributions
1. Confirm the user's desired language/stack (ask if unspecified). Possible low-friction defaults: Python (minimal `pyproject.toml` or `requirements.txt`) or Node (minimal `package.json`).
2. Add a small, focused scaffold (single responsibility): source directory (`src/` or `app/`), a manifest, a tiny README section with build/test commands, and one smoke test.
3. Keep commits atomic and include a brief test that can be run locally (unit test or simple script).

Project-specific patterns discovered
- Files to inspect: `README.md` (currently only contains the project title). Use this as the single source of truth until more files are added.
- Branching: repository default is `main` (use it as the base branch).

Examples (how to document changes you introduce)
- If you add a Python script, update `README.md` with:
  - how to create a virtualenv
  - how to install (`pip install -r requirements.txt`) or `pip install .`
  - how to run the smoke test (e.g., `python -m pytest tests/test_smoke.py`)

When you are unsure
- Ask the repository owner what the intended stack, CI, and deployment targets are before making broad architectural changes.

What NOT to do
- Do not assume an existing build/test/CI system. Avoid changing unrelated files or adding large frameworks without confirmation.

Where to update this file
- After adding source code or CI, extend this document with concrete commands (build, test, lint), important directories, and representative file examples.

Feedback
- If any section is unclear or you want the agent to follow non-default conventions (branch names, commit message style, or a preferred stack), add that detail here or tell me and I will update this file.
