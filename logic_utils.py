def get_range_for_difficulty(difficulty: str):
    """Return the inclusive guessing range for a difficulty level.

    Args:
        difficulty: The difficulty name. Recognized values are ``"Easy"``,
            ``"Normal"``, and ``"Hard"`` (case-sensitive).

    Returns:
        tuple[int, int]: A ``(low, high)`` pair of inclusive bounds for the
        secret number. Unrecognized difficulties fall back to the
        ``"Normal"`` range of ``(1, 100)``.

    Examples:
        >>> get_range_for_difficulty("Easy")
        (1, 20)
        >>> get_range_for_difficulty("Unknown")
        (1, 100)
    """
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 50
    return 1, 100


def parse_guess(raw: str):
    """Parse raw user input into an integer guess.

    Decimal input is accepted and truncated toward zero (e.g. ``"7.9"``
    becomes ``7``). Input is not range-checked; callers are responsible for
    validating the result against the active difficulty range.

    Args:
        raw: The text entered by the user. May be ``None`` or empty.

    Returns:
        tuple[bool, int | None, str | None]: A three-tuple
        ``(ok, guess, error_message)``. On success, ``ok`` is ``True``,
        ``guess`` is the parsed integer, and ``error_message`` is ``None``.
        On failure, ``ok`` is ``False``, ``guess`` is ``None``, and
        ``error_message`` is a user-facing explanation.

    Examples:
        >>> parse_guess("42")
        (True, 42, None)
        >>> parse_guess("7.9")
        (True, 7, None)
        >>> parse_guess("abc")
        (False, None, 'That is not a number.')
    """
    if raw is None or raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except (ValueError, TypeError):
        return False, None, "That is not a number."

    return True, value, None


def check_guess(guess, secret):
    """Compare a guess against the secret number.

    Both arguments should be numeric. Passing strings would cause
    lexicographic comparison (e.g. ``"9" > "10"``) and produce incorrect
    hints.

    Args:
        guess (int): The player's guess.
        secret (int): The secret number to be guessed.

    Returns:
        str: ``"Win"`` if ``guess`` equals ``secret``, ``"Too High"`` if
        ``guess`` is greater, or ``"Too Low"`` if ``guess`` is smaller.

    Examples:
        >>> check_guess(50, 50)
        'Win'
        >>> check_guess(60, 50)
        'Too High'
    """
    # FIX: Keep comparisons numeric to avoid lexicographic string results.
    if guess == secret:
        return "Win"
    if guess > secret:
        return "Too High"
    return "Too Low"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Compute the player's new score after a guess.

    Scoring rules:
        * ``"Win"``: adds ``100 - 10 * (attempt_number + 1)`` points, with a
          minimum award of 10.
        * ``"Too High"``: adds 5 points when ``attempt_number`` is even and
          subtracts 5 when it is odd.
        * ``"Too Low"``: subtracts 5 points.
        * Any other outcome leaves the score unchanged.

    Args:
        current_score: The player's score before this guess.
        outcome: The result from :func:`check_guess`.
        attempt_number: The attempt count used to scale the win bonus and
            determine the ``"Too High"`` adjustment.

    Returns:
        int: The updated score.

    Examples:
        >>> update_score(0, "Win", 1)
        80
        >>> update_score(10, "Too Low", 3)
        5
    """
    if outcome == "Win":
        points = 100 - 10 * (attempt_number + 1)
        if points < 10:
            points = 10
        return current_score + points

    if outcome == "Too High":
        if attempt_number % 2 == 0:
            return current_score + 5
        return current_score - 5

    if outcome == "Too Low":
        return current_score - 5

    return current_score
