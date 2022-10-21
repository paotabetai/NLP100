import sys

import read


def retrieve_n_connect(filepath: str) -> list:
    result = []
    posses = read.read(filepath)
    tmp_word = ""
    for i in range(len(posses)):
        if posses[i]['pos'] == "名詞":
            tmp_word += posses[i]['surface']
        else:
            if tmp_word != "":
                result.append(tmp_word)
                tmp_word = ""
    return result

if __name__ == "__main__":
    filepath: str = sys.argv[1]
    print(retrieve_n_connect(filepath))