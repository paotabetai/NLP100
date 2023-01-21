import sys

from model import Chunk
from read_dependency import read_dependency


def retrieve_connection(path: str) -> None:
    dependencies = read_dependency(path)
    for sentence in dependencies:
        for chunk in sentence:
            if "名詞" in [morph.pos for morph in chunk.morphs]:
                dst = chunk_search(sentence, chunk.dst)
                str_chunk = ''.join([morph.surface for morph in chunk.morphs if morph.pos != "記号"])
                dst_chunk = ''
                if dst:
                    dst_chunk = ''.join([morph.surface for morph in dst.morphs if morph.pos != "記号"])
                    if "動詞" in [morph.pos for morph in dst.morphs]:
                        print(str_chunk + '\t' + dst_chunk)  # 43


def chunk_search(sentence: list, index: int) -> Chunk:
    if index == -1:
        return None
    for chunk in sentence:
        if chunk.srcs == index:
            return chunk


if __name__ == "__main__":
    filepath: str = sys.argv[1]
    retrieve_connection(filepath)