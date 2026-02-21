def translate(text):
    vowels = "aeiou"

    def translate_word(word):
        # Rule 1
        if word.startswith(("xr", "yt")) or word[0] in vowels:
            return word + "ay"

        leading_consonants = ""

        # Rule 2 + Rule 3 + Rule 4
        while word and word[0] not in vowels:
            # Rule 4: 'y' acts like a vowel after initial consonant(s)
            if word[0] == "y" and leading_consonants:
                break

            leading_consonants += word[0]
            word = word[1:]

            # Rule 3: move 'qu' together
            if leading_consonants.endswith("q") and word.startswith("u"):
                leading_consonants += "u"
                word = word[1:]

        return word + leading_consonants + "ay"

    return " ".join(translate_word(w) for w in text.split())

        


    