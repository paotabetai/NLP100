import sys

from read import read
from model import Chunk, Morph


def read_dependency(filepath: str) -> list:
    result = []
    with open(filepath) as f:
        line = f.readline()
        chunks = []
        chunk = Chunk([], 0, 0)
        while line:
            if line[0] == "*":
                if chunk.morphs:
                    chunks.append(chunk)
                    chunk = Chunk([], 0, 0)
                splitted_c_word = line.split()
                chunk.srcs, chunk.dst = int(splitted_c_word[1]), int(splitted_c_word[2][:-1])
            elif line == "EOS\n":
                if chunk.morphs:
                    chunks.append(chunk)
                if chunks:
                    result.append(chunks)
                    chunks = []
                    chunk = Chunk([], 0, 0)
            else:
                morph = read(line)
                if morph is not None:
                    chunk.morphs.append(morph)
            line = f.readline()
        if chunk.morphs:
            chunks.append(chunk)
        if chunks:
            result.append(chunks)
    return result


if __name__ == "__main__":
    filepath: str = sys.argv[1]
    result = read_dependency(filepath)
    chunk_list = []
    for chunk in result[2]:
        surfaces = ''.join([morph.surface for morph in chunk.morphs])
        for target in result:
            if chunk.dst == target.srcs:
                target_surfaces = ''.join([morph.surface for morph in target.morphs])
                chunk_list.append(surfaces + " -> " + target_surfaces)
                break
        if chunk.dst == -1:
            chunk_list.append(surfaces + ": 係り先なし")
    print(chunk_list)  # 41