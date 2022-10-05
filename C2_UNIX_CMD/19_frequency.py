from mimetypes import init
import sys

def freqsort(filepath: str) -> None:
    initial_dict = {}
    with open(filepath) as f:
        line = f.readline()
        while line:
            initical_character = line.split("\t")[0][0]
            if not initical_character in initial_dict:
                initial_dict[initical_character] = 0
            initial_dict[initical_character] += 1
            line = f.readline()
    for item in sorted(initial_dict.items(), key=lambda item: item[1], reverse=True):
        print(item[0])



if __name__ == "__main__":
    filepath = sys.argv[1]
    freqsort(filepath)