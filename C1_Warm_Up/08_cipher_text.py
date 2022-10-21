def cipher(sentence: str) -> str:
    result = ""
    for c in sentence:
        if c.islower():
            c = chr(216 - ord(c))
        result += c

    return result


sentence = "AbCdEfG12345,./;"

print(cipher(sentence))