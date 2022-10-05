sentence = "I am an NLPer"

words = [word.strip('!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~') for word in sentence.split()]

letter_bi_grams = [sentence[i] + " " + sentence[i + 1] for i in range(len(sentence) - 1)]

word_bi_grams = [words[i] + words[i + 1] for i in range(len(words) - 1)]

print(letter_bi_grams, word_bi_grams)
