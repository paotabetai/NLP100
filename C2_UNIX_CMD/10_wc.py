import sys


def wc(filepath: str) -> int:
    with open(filepath) as f:
        r_l = f.readlines()
        length = len(r_l)
    return length


if __name__ == "__main__":
    filepath = sys.argv[1]
    print(wc(filepath))