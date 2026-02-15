def is_armstrong_number(number):
    digits = str(number)           # turn number into string to loop over digits
    power = len(digits)            # number of digits
    total = 0

    for d in digits:
        total += int(d) ** power  # raise each digit to the power

    return total == number

