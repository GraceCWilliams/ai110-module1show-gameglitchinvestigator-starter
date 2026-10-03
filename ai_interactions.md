# AI Interactions Log

> **Stretch features only.** Only fill in the sections that apply to stretch features you attempted. If you did not attempt a stretch feature, leave its section blank or delete it. This file is not required for the core project.

---

## Agent Workflow (SF8)

> Document your experience using an AI agent (e.g., Cursor Agent, Claude, Copilot) to make multi-step changes autonomously.

**What task did you give the agent?**

<!-- Describe the goal you asked the agent to accomplish -->

**What did the agent do?**

<!-- List the steps the agent took (files edited, commands run, etc.) -->

**What did you have to verify or fix manually?**

<!-- Describe anything the agent got wrong or that required human review -->

---

## Test Generation (SF7)

> Document how you used AI to help generate or improve tests.

| Edge Case | Prompt Used | AI-Suggested Test | Did It Pass? | Your Reasoning |
|-----------|-------------|-------------------|--------------|----------------|
| | | | | |
| | | | | |
| | | | | |

---

## Linting & Style (SF9)

> Document your use of AI for linting or code style improvements.

**Prompt used:**

```
add professional-grade docstrings to every function in `logic_utils.py`
```

```
review my code for PEP 8 style compliance and apply its suggestions to resolve
any formatting or naming issues it identifies.
```

**Linting output before:**

Tool: `flake8` (includes `pycodestyle`) with the `pep8-naming` plugin, run on
`app.py`, `logic_utils.py`, and `tests/`.

```
tests/test_game_logic.py:3:1: E302 expected 2 blank lines, found 1
tests/test_game_logic.py:8:1: E302 expected 2 blank lines, found 1
tests/test_game_logic.py:13:1: E302 expected 2 blank lines, found 1
tests/test_game_logic.py:18:1: E302 expected 2 blank lines, found 1
tests/test_game_logic.py:19:80: E501 line too long (83 > 79 characters)
```

**Linting output after:**

```
$ flake8 app.py logic_utils.py tests/
(no output, 0 issues)

$ pytest -q
4 passed
```

**Changes applied:**

The AI suggested the changes below, and I applied all of them. None of them
change how the code behaves.

- **Blank lines (E302):** added a second blank line before each of the four
  test functions in `tests/test_game_logic.py`.
- **Line length (E501):** split the 83-character `# FIX:` comment in
  `tests/test_game_logic.py` into two lines so it fits within 79 characters.
- **Import grouping:** in `app.py`, separated the imports into standard
  library (`random`), third-party (`streamlit`), and local (`logic_utils`)
  groups with blank lines between them. flake8 doesn't flag this, but PEP 8
  recommends it, and the AI caught it by reading the code.
- **Naming:** `pep8-naming` reported no issues, so no names were changed.
- **Docstrings:** added Google-style docstrings (Args, Returns, Examples) to
  all four functions in `logic_utils.py`. The examples run as doctests
  (9 passed). The docstrings describe the current behavior, including some
  logic the AI flagged as possibly buggy, such as the Hard range being smaller
  than Normal and "Too High" adding points on even attempts. I left those as
  they are for now.

---

## Model Comparison (SF11)

> Compare two AI models on the same task.

**Task given to both models:**

<!-- Describe what you asked each model to do -->

| | Model A | Model B |
|-|---------|---------|
| **Model name** | | |
| **Response summary** | | |
| **More Pythonic?** | | |
| **Clearer explanation?** | | |

**Which did you prefer and why?**

<!-- Your conclusion -->
