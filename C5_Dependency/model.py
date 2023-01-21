class Morph:

    def __init__(self, surface: str, base: str, pos: str, pos1: str):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1


class Chunk:

    def __init__(self, morphs, dst: int, srcs: int):
        self.morphs = morphs
        self.dst = dst
        self.srcs = srcs