import sys
import re
import read


def extract_file(filepath: str) -> str:
    readjson: str = read.read_json(filepath)
    result: list = []
    pattern = re.compile("ファイル:(.+?.jpg)")
    for line in readjson.split('\n'):
        match = pattern.findall(line)
        if match:
            for m in match:
                result.append(m)
    return '\n'.join(result)


if __name__ == "__main__":
    filepath: str = sys.argv[1]
    print(extract_file(filepath))