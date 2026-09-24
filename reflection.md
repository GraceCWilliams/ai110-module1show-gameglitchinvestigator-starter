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

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion you did not accept as written (including what the AI suggested, why you rejected or changed it, and how you verified your version). It does not have to be a suggestion that was wrong: over-engineered, out of scope, harder to read, or a poor fit for this codebase all count.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
