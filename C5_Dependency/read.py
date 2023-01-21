import sys

import CaboCha

from model import Morph

c = CaboCha.Parser()


def read(line: str) -> Morph:
    splitted_c_word = line.split("\t")
    if len(splitted_c_word) > 1:
        poss = splitted_c_word[1].split(",")
        surface = splitted_c_word[0]
        base = poss[6]
        pos = poss[0]
        pos1 = poss[1]
        morph = Morph(surface, base, pos, pos1)
        return morph
    else:
        return None


if __name__ == "__main__":
    filepath: str = sys.argv[1]
    result = []
    with open(filepath) as f:
        line = f.readline()
        sentence = []
        line = f.readline()
        while line:
            if line != "EOS\n":
                morph = read(line)
                if morph is not None:
                    sentence.append(morph)
            else:
                result.append(sentence)
                sentence = []
            line = f.readline()
    print([morph.base for morph in result[2]])  # 40


