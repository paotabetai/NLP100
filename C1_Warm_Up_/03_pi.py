import re
import string

sentence = '''Now I need a drink, alcoholic of course,
    after the heavy lectures involving quantum mechanics'''
pattern = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
pi_1 = [len(word.strip(pattern)) for word in sentence.split()]

pi_2 = [len(word.translate(str.maketrans("", "", string.punctuation)))
        for word in sentence.split()]

pi_3 = [len(re.sub(r'\_', '', re.sub(r'[\W]', '', word)))
        for word in sentence.split()]

print(pi_3)