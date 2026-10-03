# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [x] Describe the game's purpose.
- [x] Detail which bugs you found.
- [x] Explain what fixes you applied.

The game is a Streamlit number-guessing game: the player chooses a difficulty, makes guesses within its number range, and uses higher/lower hints to find the secret before running out of attempts. I found that the hints pointed in the wrong direction, and that converting the secret to text on alternating attempts could make guesses compare alphabetically instead of numerically. The initial attempt count also started at 1, and starting a new game did not reset every piece of game state.

I moved the game helpers (`get_range_for_difficulty`, `parse_guess`, `check_guess`, and `update_score`) into `logic_utils.py`. Guess comparison now stays numeric, hints tell the player to go in the correct direction, attempts start at 0 so the first guess counts as attempt 1, and New Game resets status, attempts, score, and history while choosing a secret within the selected difficulty range. I added a regression test for guessing 2 when the secret is 18; the focused test suite passes.

## Demo Walkthrough

Sample game on Normal difficulty, with the secret number set to 50:

1. The player starts a new game; attempts and score are reset to 0.
2. The player guesses 40. The game responds “Too Low” and “Go HIGHER!”; the score becomes -5.
3. The player guesses 60. The game responds “Too High” and “Go LOWER!”; this is attempt 2, so the score increases by 5 to 0.
4. The player guesses 50. The game responds “Correct!”, shows the winning message and balloons, and ends the game with a final score of 60.
5. The player selects “New Game” to reset the game state and play again.

## 🧪 Test Results

```
$ source .venv/bin/activate && python -m pytest tests/test_game_logic.py
============================= test session starts ==============================
platform darwin -- Python 3.11.5, pytest-9.1.1, pluggy-1.6.0
rootdir: /Users/grace_computer/Library/Mobile Documents/com~apple~CloudDocs/AI110/ai110-module1show-gameglitchinvestigator-starter
plugins: anyio-4.15.1
collected 4 items

tests/test_game_logic.py ....                                            [100%]

============================== 4 passed in 0.01s ===============================
```

## 🚀 Stretch Features

- [x] **Professional Documentation and Style:** All four functions in `logic_utils.py` (`get_range_for_difficulty`, `parse_guess`, `check_guess`, `update_score`) have Google-style docstrings with Args, Returns, and doctest examples (9 passing via `python -m doctest logic_utils.py`). The code passes `flake8` with `pep8-naming` with no warnings. Fixes included blank-line spacing and line length in `tests/test_game_logic.py` and import grouping in `app.py`. The prompts, linter output, and applied changes are in [ai_interactions.md](ai_interactions.md).
#- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
