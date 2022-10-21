import MeCab

tagger = MeCab.Tagger("-Odump")


def read(filepath: str) -> list:
    result = []
    with open(filepath) as f:
        line = f.readline()
        while line:
            mecabbed_line = tagger.parse(line).split("\n")
            for mecabbed_word in mecabbed_line:
                splitted_m_word = mecabbed_word.split()
                if splitted_m_word:
                    poss = splitted_m_word[2].split(",")
                    test_dict = {}
                    test_dict['surface'] = splitted_m_word[1]
                    test_dict['base'] = poss[7] if len(poss) > 7 else ''
                    test_dict['pos'] = poss[0]
                    test_dict['pos1'] = poss[1] if len(poss) > 1 else ''
                    result.append(test_dict)
            line = f.readline()
    return result