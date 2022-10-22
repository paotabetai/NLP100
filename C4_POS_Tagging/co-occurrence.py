import collections
import itertools
import sys

import numpy as np
import matplotlib.pyplot as plt

import read


plt.rcParams["font.family"] = "Hiragino Sans"

def calculate_frequency(filepath: str) -> None:
    bases = [(posses['base'], posses['pos']) for posses in read.read(filepath)]
    sentence_list = []
    tmp_list = []
    for base in bases:
        if base[1] == 'BOS/EOS':
            if len(tmp_list) != 0:
                sentence_list.append(tmp_list)
            tmp_list = []
        elif base[1] == "名詞":
            tmp_list.append(base[0])
    sentences_combs = [list(itertools.combinations(sentence, 2)) for sentence in sentence_list]
    words_combs = [
            [tuple(sorted(words)) for words in sentence
                if words[0] and
                words[1] and
                words[0] != words[1] and
                (words[0] == "猫" or words[1] == "猫")]
            for sentence in sentences_combs
        ]
    target_combs = []
    for words_comb in words_combs:
        target_combs.extend(words_comb)
    ct = collections.Counter(target_combs)
    cat_sum = sum([1 for base in bases if base[0] == "猫"])
    top_10 = ct.most_common()[:10]
    left = np.array([','.join(tuple[0]) for tuple in top_10])
    height = np.array([tuple[1] / cat_sum for tuple in top_10])
    plt.bar(left, height)
    plt.show()



if __name__ == "__main__":
    filepath: str = sys.argv[1]
    calculate_frequency(filepath)