#This function is meant to determine if a given word is an isogram, meaning 
#if it contains each of its letters not more than once
def is_isogram(string):
    string = string.lower().strip()

    for exception in range(len(string)):
        if string[exception] == " " or string[exception] == "-":
            continue

        for letter in range(exception + 1, len(string)):
            if string[letter] == " " or string[letter] == "-":
                continue

            if string[exception] == string[letter]:
                return False

    return True
