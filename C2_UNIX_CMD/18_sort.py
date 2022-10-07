import sys


def csu(filepath: str) -> None:
    with open(filepath) as f:
        lines = [line.split("\t") for line in f.readlines()]
    sorted_lines = sorted(lines, key=lambda line: line[2], reverse=True)
    print(''.join(['\t'.join(line) for line in sorted_lines]))


if __name__ == "__main__":
    filepath = sys.argv[1]
    csu(filepath)