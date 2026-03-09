def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        # FIX: Hard was incorrectly set to 1-50, which is easier than Normal's 1-100.
        # Refactored into logic_utils.py using AI assistance. Fixed range to 1-200.
        return 1, 200
    return 1, 100


def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    # FIX: Refactored from app.py into logic_utils.py using AI assistance.
    if raw is None:
        return False, None, "Enter a guess."

    if raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    return True, value, None


def check_guess(guess, secret):
    """
    Compare guess to secret and return the outcome string.

    outcome: "Win", "Too High", or "Too Low"
    """
    # FIX: Original had hints backwards — showed "Go HIGHER!" when guess was too high
    # and "Go LOWER!" when guess was too low. Fixed by correcting the comparison logic.
    # Refactored into logic_utils.py using AI assistance.
    if guess == secret:
        return "Win"
    if guess > secret:
        return "Too High"
    return "Too Low"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    # FIX: Original gave +5 bonus points for "Too High" on even-numbered attempts,
    # rewarding wrong guesses. Also had an unnecessary +1 offset in the win formula.
    # Fixed to always subtract 5 for any wrong guess. Refactored using AI assistance.
    if outcome == "Win":
        points = 100 - 10 * attempt_number
        if points < 10:
            points = 10
        return current_score + points

    # Wrong guess: always subtract 5 regardless of attempt parity
    return current_score - 5
