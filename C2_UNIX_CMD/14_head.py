import sys

def head(filepath: str, n: int) -> None:

    with open(filepath) as f:
        for i in range(n):
            print(f.readline(), end="")


if __name__ == "__main__":
    filepath = sys.argv[1]
    n = int(sys.argv[2])
    head(filepath, n)