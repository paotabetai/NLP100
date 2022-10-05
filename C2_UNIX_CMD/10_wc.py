import sys

def wc(filepath: str) -> int:
    with open(filepath) as f:
        l = f.readlines()
        length = len(l)
    return length

if __name__ == "__main__":
    filepath = sys.argv[1]
    print(wc(filepath))