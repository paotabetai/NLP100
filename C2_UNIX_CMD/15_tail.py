import sys

def tail(filepath: str, n: int) -> None:

    with open(filepath) as f:
        file = f.readlines()
        for i in range(1, n + 1):
            print(file[-i], end="")


if __name__ == "__main__":
    filepath = sys.argv[1]
    n = int(sys.argv[2])
    tail(filepath, n)