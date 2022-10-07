import sys
import re
import read


def extract_template_refined(filepath: str) -> str:
    readjson: str = read.read_json(filepath)
    template_dict: dict = {}
    index = readjson.find("{{基礎情報 ")
    start_prefix = "{{"
    end_prefix = "}}"
    outer_flg = False
    inner_flg = False
    target = ""
    if index != -1:
        # for i in range(index, index+10):
        for i in range(index, len(readjson) - 1):
            if readjson[i:i + 2] == start_prefix:
                target += readjson[i]
                if outer_flg:
                    inner_flg = True
                outer_flg = True
            elif readjson[i:i + 2] == end_prefix:
                target += readjson[i]
                if not inner_flg:
                    outer_flg = False
                    break
                elif inner_flg:
                    inner_flg = False
            else:
                target += readjson[i]

    pattern_1 = re.compile("\[\[.+?#.+?\|(.+?)\]\]")
    pattern_2 = re.compile("\[\[.+?\|(.+?)\]\]")
    pattern_3 = re.compile("\[\[(.+?)\]\]")

    for key in [key.split(" =") for key in target.split("\n|")][1:]:
        value = key[1].strip().replace("'''''", "", 100000).\
            replace("'''", "", 100000).replace("''", "", 100000)
        if pattern_1.match(value):
            value = ' '.join(pattern_1.findall(value))
        elif pattern_2.match(value):
            value = ' '.join(pattern_2.findall(value))
        elif pattern_3.match(value):
            value = ' '.join(pattern_3.findall(value))
        template_dict[key[0].strip()] = value
    return template_dict


if __name__ == "__main__":
    filepath: str = sys.argv[1]
    print(extract_template_refined(filepath))