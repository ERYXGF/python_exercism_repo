def is_valid(isbn):
    # Remove dashes
    cleaned = isbn.replace("-", "")

    # Must be exactly 10 chars
    if len(cleaned) != 10:
        return False

    # First 9 must be digits
    if not cleaned[:9].isdigit():
        return False

    # Last char must be digit or X
    if not (cleaned[9].isdigit() or cleaned[9] == "X"):
        return False

    total = 0
    for i, ch in enumerate(cleaned):
        value = 10 if ch == "X" else int(ch)
        weight = 10 - i
        total += value * weight

    return total % 11 == 0
