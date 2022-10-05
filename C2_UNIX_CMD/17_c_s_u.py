from mimetypes import init
import sys

def csu(filepath: str) -> None:
    initial_set = set()
    with open(filepath) as f:
        line = f.readline()
        while line:
            initial_set.add(line.split("\t")[0][0])
            line = f.readline()
    for character in sorted(list(initial_set)):
        print(character)



if __name__ == "__main__":
    filepath = sys.argv[1]
    csu(filepath)