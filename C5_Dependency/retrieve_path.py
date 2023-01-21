import sys

from model import Chunk
from read_dependency import read_dependency


def retrieve_path(path: str):
    dependencies = read_dependency(path)
    result = ""
    for sentence in dependencies:
        paths = []
        for chunk in sentence:
            if "名詞" in [morph.pos for morph in chunk.morphs]:
                path = [chunk]
                target = chunk_search(sentence, chunk.dst)
                while target:
                    path.append(target)
                    target = chunk_search(sentence, target.dst)
                paths.append(path)
        for i in range(len(paths)):
            min_path = ""
            for j in range(i, len(paths)):
                if i != j:
                    if paths[j][0] in paths[i]:
                        for chunk in paths[i]:
                            if chunk != paths[j][0]:
                                if chunk == paths[i][0]:
                                    for morph in paths[i][0].morphs:
                                        if morph.pos != "記号":
                                            if morph.pos != "名詞":
                                                min_path += morph.surface
                                            elif len(min_path) == 0 or min_path[-1] != "X":
                                                min_path += "X"
                                    min_path += " -> "
                                else:
                                    min_path += "".join([morph.surface for morph in chunk.morphs if morph.pos != "記号"]) + " -> "
                            else:
                                break
                        for morph in paths[j][0].morphs:
                            if morph.pos != "記号":
                                if morph.pos != "名詞":
                                    min_path += morph.surface
                                else:
                                    min_path += "Y"
                        min_path += "\n"
                    else:
                        for k in range(len(paths[i])):
                            if paths[i][k] in paths[j]:
                                for chunk in paths[i][0:k]:
                                    if chunk == paths[i][0]:
                                        for morph in paths[i][0].morphs:
                                            if morph.pos != "記号":
                                                if morph.pos != "名詞":
                                                    min_path += morph.surface
                                                elif len(min_path) == 0 or min_path[-1] != "X":
                                                    min_path += "X"
                                        min_path += " -> "
                                    else:
                                        min_path += "".join([morph.surface for morph in chunk.morphs if morph.pos != "記号"]) + " -> "
                                min_path += " | "
                                for chunk in paths[j]:
                                    if chunk != paths[i][k]:
                                        if chunk == paths[j][0]:
                                            for morph in chunk.morphs:
                                                if morph.pos != "記号":
                                                    if morph.pos != "名詞":
                                                        min_path += morph.surface
                                                    elif len(min_path) == 0 or min_path[-1] != "Y":
                                                        min_path += "Y"
                                            min_path += " -> "
                                        else:
                                            min_path += "".join([morph.surface for morph in chunk.morphs if morph.pos != "記号"]) + " -> "
                                    else:
                                        break
                                min_path = min_path.rstrip(" -> ")
                                min_path += " | " + "".join([morph.surface for morph in paths[i][k].morphs if morph.pos != "記号"]) + "\n"
            if min_path:
                result += min_path
    return result

def chunk_search(sentence: list, index: int) -> Chunk:
    if index == -1:
        return None
    for chunk in sentence:
        if chunk.srcs == index:
            return chunk


if __name__ == "__main__":
    filepath: str = sys.argv[1]
    print(retrieve_path(filepath))  # 49