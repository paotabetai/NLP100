import sys

from model import Chunk
from read_dependency import read_dependency


def retrieve_v_pattern(path: str) -> str:
    dependencies = read_dependency(path)
    result = ""
    for sentence in dependencies:
        for chunk in sentence:
            v = ""
            for morph in chunk.morphs:
                if morph.pos == "動詞":
                    v = morph.base
                    break
            v_srcs = chunk.srcs
            if v:
                pos_particles = []
                for chunk in sentence:
                    if chunk.dst == v_srcs:
                        for morph in chunk.morphs:
                            if morph.pos == "助詞":
                                pos_particles.append(morph.base)
                                break
                if pos_particles:
                    result += v + " " + " ".join(sorted(pos_particles))+ "\n"
    return result


if __name__ == "__main__":
    filepath: str = sys.argv[1]
    print(retrieve_v_pattern(filepath))  # 45