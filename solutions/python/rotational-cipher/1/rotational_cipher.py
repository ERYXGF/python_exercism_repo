def rotate(text, key):
    out = ""
    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            out += chr((ord(ch) - base + key) % 26 + base)
        else:
            out += ch
    return out
