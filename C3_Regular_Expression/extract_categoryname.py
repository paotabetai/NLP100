import sys
import re
import read


def extract_categoryname(filepath: str) -> str:
    readjson: str = read.read_json(filepath)
    result: list = []
    pattern = re.compile("Category:(.+)]]")
    for line in readjson.split('\n'):
        match = pattern.search(line)
        if match:
            tmp = match.group(1)
            result.append(re.sub(r'[\|*.*]', '', tmp))
    return '\n'.join(result)


if __name__ == "__main__":
    filepath: str = sys.argv[1]
    print(extract_categoryname(filepath))