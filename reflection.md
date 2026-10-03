# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start (for example: "the hints were backwards").

  The first time I ran the game, the secret number was 18, and I tested several guesses, including 13, 2, 1, -100, and -100000000000. The game displayed "Go Lower!" after every guess, including guesses that were already below the secret number, suggesting that the hint logic was not responding correctly to the input. I also noticed that the score became -35 while the Developer Debug Info displayed zero attempts, which suggested a possible issue with the scoring or attempts-tracking logic. I planned to investigate the hint, scoring, and attempts logic in the code to determine the causes of these behaviors.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input / Bug | Expected Behavior | Actual Behavior | Console Output / Error | Suspected Code Location |
|-------------|-------------------|-----------------|------------------------|-------------------------|
| Bug 1: Guess 13 (secret = 18) | Too Low and Go Higher! | Too Low and Go Lower! | None | `app.py`, `check_guess()` |
| Bug 1: Guess 2 (secret = 18) | Too Low and Go Higher! | Too Low and Go Lower! | None | `app.py`, `check_guess()` |
| Bug 1: Guess 1 (secret = 18) | Too Low and Go Higher! | Too Low and Go Lower! | None | `app.py`, `check_guess()` |
| Bug 2: Even-numbered attempt | Numeric comparison with the secret | Secret is converted to a string, which can cause incorrect comparisons | No console error observed | `app.py`, submit logic and `check_guess()` |
| Bug 3: New Game button | Attempts counter should have a consistent starting value | Initial game sets attempts to 1, while New Game resets attempts to 0 | None | `app.py`, session state initialization and New Game logic |
---

## 2. How did you use AI as a teammate?

I used the AI coding assistant in VS Code as a teammate to trace the guess-comparison bug, move the game helpers into `logic_utils.py`, and suggest a regression test. One suggestion I accepted was to keep the guess and secret numeric throughout `check_guess()` rather than converting the secret to a string on alternating attempts; this avoids comparing numbers as text. I verified it with a regression test that checks that guessing `2` against secret `18` returns `"Too Low"`, and it passed with the existing logic tests.

One suggestion I did not keep was adding `pytest.ini` with a `pythonpath` setting so the bare `pytest` command could import the project module. I rejected that configuration because the project can run the tests directly with `python -m pytest tests/test_game_logic.py` from the project root, so an extra pytest configuration file was unnecessary for the workflow I chose. I removed the configuration and verified that the module-invocation command still passed all four tests.

---

## 3. Debugging and testing your fixes

I checked the comparison behavior with the existing tests for a winning, too-high, and too-low guess, and added a regression case for the string-comparison failure: `check_guess(2, 18)` must return `"Too Low"`. I ran `python -m pytest tests/test_game_logic.py` from the project root with the virtual environment active; all four tests passed, including that new case. The tests verify the helper's outcomes; I also checked in `app.py` that `"Too High"` displays “Go LOWER!” and `"Too Low"` displays “Go HIGHER!”.

---

## 4. What did you learn about Streamlit and state?

When someone interacts with a Streamlit widget, Streamlit reruns the app script from the top to redraw the page. Ordinary Python variables are recreated during that rerun, so values that need to persist between interactions, like the secret number and attempt count, belong in `st.session_state`. I would explain session state as a small per-user memory that survives those reruns, until the app explicitly changes or resets it.

---

## 5. Looking ahead: your developer habits

I want to keep writing a small regression test for the exact input that exposed a bug, then run the relevant tests after changing the code. Next time I work with an AI coding assistant, I will state the expected test command and project constraints up front; in this project, I initially followed a pytest configuration suggestion before deciding that `python -m pytest` was the workflow I needed. This project reminded me that AI-generated changes are suggestions, not proof: I should compare them with the existing code and verify them with tests before accepting them.
