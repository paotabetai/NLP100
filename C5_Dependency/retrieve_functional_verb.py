import sys

from model import Chunk
from read_dependency import read_dependency


def retrieve_functional_verb(path: str) -> None:
    dependencies = read_dependency(path)
    result = ""
    for sentence in dependencies:
        for chunk in sentence:
            v = ""
            base_v = ""
            for morph in chunk.morphs:
                if morph.pos == "動詞":
                    base_v = morph.base
                    break
            v_srcs = chunk.srcs
            if base_v:
                for chunk in sentence:
                    if chunk.dst == v_srcs and len(chunk.morphs) == 2:
                        if chunk.morphs[1].pos == "助詞" and chunk.morphs[1].base == "を" and chunk.morphs[0].pos1 == "サ変接続":
                            v = chunk.morphs[0].surface + chunk.morphs[-1].surface + base_v
                        v_srcs = chunk.srcs
            if v:
                particles = []
                for chunk in sentence:
                    if chunk.dst == v_srcs:
                        morph = chunk.morphs[-1]
                        if morph.pos == "助詞":
                            particles.append([morph.base, ''.join([morph.surface for morph in chunk.morphs if morph.pos != "記号"])])
                if particles:
                    particles = sorted(particles, key=lambda x: x[0])
                    result += v + " " + " ".join([particle[0] for particle in particles])+ " " + " ".join([particle[1] for particle in particles]) + "\n"
    return result


if __name__ == "__main__":
    filepath: str = sys.argv[1]
    print(retrieve_functional_verb(filepath))  # 47