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

- The game is a number guessing game where you try to guess a secret number within a set number of attempts. The difficulty setting changes the range and attempt limit.
- Bugs found: hints were backwards (Go HIGHER when guess was too high), secret was cast to a string on even attempts making wins impossible, Hard difficulty had range 1-50 which was easier than Normal's 1-100, score incorrectly gave +5 points on some wrong guesses, and attempts started at 1 instead of 0.
- Fixes applied: moved all game logic into `logic_utils.py`, corrected the hint directions in `check_guess`, removed the even/odd string-casting bug, fixed Hard difficulty range to 1-200, fixed scoring to always subtract 5 on wrong guesses, and initialized attempts to 0.

## 📸 Demo

- [x] Game now runs correctly — hints are accurate, winning is possible, and the score tracks properly.

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]
