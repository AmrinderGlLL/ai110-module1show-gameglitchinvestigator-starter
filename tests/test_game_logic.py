from logic_utils import check_guess, update_score, get_range_for_difficulty


def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"


def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"


def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"


def test_score_decreases_for_too_high():
    # FIX verified: Score should always decrease for wrong guesses, never increase.
    # Original bug gave +5 on even attempts for "Too High".
    score = update_score(50, "Too High", 2)
    assert score == 45


def test_score_decreases_for_too_low():
    # Wrong guess (Too Low) should always subtract 5 from score.
    score = update_score(50, "Too Low", 3)
    assert score == 45


def test_hard_difficulty_harder_than_normal():
    # FIX verified: Hard difficulty was set to range 1-50, easier than Normal's 1-100.
    # Fixed to 1-200 so Hard is actually harder.
    _, normal_high = get_range_for_difficulty("Normal")
    _, hard_high = get_range_for_difficulty("Hard")
    assert hard_high > normal_high
