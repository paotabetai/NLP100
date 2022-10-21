import sys

import read


def retrieve_n_phrase(filepath: str) -> list:
    result = []
    posses = read.read(filepath)
    for i in range(len(posses)):
        if posses[i]['base'] == "の"\
            and posses[i - 1]['pos'] == "名詞"\
            and posses[i + 1]['pos'] == "名詞":
            result.append(posses[i - 1]['surface'] + "の" + posses[i + 1]['surface'])
    return result

if __name__ == "__main__":
    filepath: str = sys.argv[1]
    print(retrieve_n_phrase(filepath))