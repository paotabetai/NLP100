import sys
import CaboCha
from graphviz import Graph
from graphviz import Digraph

from model import Morph

from read_dependency import read_dependency

c = CaboCha.Parser()
dg = Digraph(format='png')


def draw(chunks: list) -> dict:
    chunk_dict = {}
    for chunk in chunks:
        chunk_dict[chunk.srcs] = ''.join([morph.surface for morph in chunk.morphs])
    for chunk in chunks:
        chunk_surface = ''.join([morph.surface for morph in chunk.morphs])
        if chunk.dst != -1:
            dg.edge(chunk_surface, chunk_dict[chunk.dst])
    dg.view()

if __name__ == "__main__":
    filepath: str = sys.argv[1]
    result = read_dependency(filepath)
    draw(result[2])  # 44
