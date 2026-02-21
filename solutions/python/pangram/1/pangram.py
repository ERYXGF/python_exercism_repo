def is_pangram(sentence):
    sentence = sentence.lower()
    letters = {ch for ch in sentence if "a" <= ch <= "z"}
    if len(letters) == 26:
        return True
    else:
        return False

