# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

When I first ran the game it looked fine but the hints were totally backwards. If I guessed too high it said "Go HIGHER!" which made no sense. The Hard difficulty was also set to 1-50 which is actually easier than Normal (1-100), so the diffculty levels were wrong. The score would also randomly go up when I guessed wrong which was really confusing.

---

## 2. How did you use AI as a teammate?

I used Claude to help me find and fix the bugs in the code. A correct suggestion was when I asked about the hints being wrong — it pointed me straight to the `check_guess` function and explained the messages were swapped, which I verified by reading the code myself. A misleading suggestion was when AI told me the secret number issue was a session state problem at the top of the file, but the real bug was actually the even/odd attempt block that was converting the secret to a string mid-game. I had to read the code more carefully to find the actual line causing it.

---

## 3. Debugging and testing your fixes

I knew a bug was fixed when the game behaved correctly AND a pytest test confirmed it. I wrote a test called `test_guess_too_high` that checks `check_guess(60, 50)` returns `"Too High"` — before the fix it would have returned the wrong thing. Running `pytest` showed all 6 tests passing after my fixes. AI helped me think of what edge cases to test, like making sure the score never increases on a wrong guess.

---

## 4. What did you learn about Streamlit and state?

Streamlit reruns the entire script every time you click something, so normal variables reset to their starting values on each click. `st.session_state` is how you keep data alive between reruns — like the secret number, score, and attempt count. Without it, the game would pick a new secret number every time you hit submit which is what was happening. Its kind of like a dictionary that persists while the app is running.

---

## 5. Looking ahead: your developer habits

One habit I want to keep is writing a test right after fixing a bug so the fix is verified and stays protected. I would do things differently next time by reading the full function before asking AI to fix it, instead of just describing the symptom — that way I dont get sent down the wrong path. This project made me realize AI can write code that runs fine but has logic mistakes hidden inside, so I need to actually read and understand it rather than just trusting it works.
