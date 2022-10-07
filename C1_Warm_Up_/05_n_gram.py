sentence = "I am an NLPer"
pattern = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
words = [word.strip(pattern) for word in sentence.split()]

letter_bi_grams = []
for i in range(len(sentence) - 1):
    letter_bi_grams.append(sentence[i] + " " + sentence[i + 1])

word_bi_grams = [words[i] + words[i + 1] for i in range(len(words) - 1)]

print(letter_bi_grams, word_bi_grams)
