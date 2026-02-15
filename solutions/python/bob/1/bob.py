def response(hey_bob):
#If theres a silence.
    hey_bob = hey_bob.strip()
    if len(hey_bob) == 0:
        return "Fine. Be that way!"
#If its a yelled and a question.
    elif  hey_bob.isupper() and hey_bob[-1]=="?" and any(char.isalpha() for char in hey_bob):
        return "Calm down, I know what I'm doing!"
#If its yelled.
    elif hey_bob.isupper() and any(char.isalpha() for char in hey_bob):
        return "Whoa, chill out!"
#If its a question.
    elif hey_bob[-1]=="?":
        return "Sure."
#If its something else.
    else:
        return "Whatever."
