import sys

import read


def retrieve_base(filepath: str) -> list:
    result = []
    for poss in read.read(filepath):
        if poss['pos'] == '動詞':
            result.append(poss['base'])
    return result

if __name__ == "__main__":
    filepath: str = sys.argv[1]
    print(retrieve_base(filepath))