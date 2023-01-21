import sys

import CaboCha

c = CaboCha.Parser()

if __name__ == "__main__":
    filepath: str = sys.argv[1]
    with open(filepath) as f:
        line = f.readline()
        while line:
            caboched_line = c.parse(line).toString(CaboCha.FORMAT_LATTICE)
            print(caboched_line)
            line = f.readline()