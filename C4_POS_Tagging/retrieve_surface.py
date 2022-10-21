import sys

import read


def retrieve_surface(filepath: str) -> list:
    result = [poss['surface'] for poss in read.read(filepath) if poss['pos'] == '動詞']
    return result

if __name__ == "__main__":
    filepath: str = sys.argv[1]
    print(retrieve_surface(filepath))