import random

sentence = "I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind"
result = []
for word in sentence.split():
    n = len(word)
    if n <= 4:
        result.append(word)
    else:
        result.append(word[0] + ''.join(random.sample(word[1:-1], n - 2)) + word[-1])

print(' '.join(result))


