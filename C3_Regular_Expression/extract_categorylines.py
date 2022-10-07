import sys
import read


def extract_category(filepath: str) -> str:
    readjson: str = read.read_json(filepath)
    result = []
    for line in readjson.split('\n'):
        if line and line.find("[[Category") != -1:
            result.append(line)
    return '\n'.join(result)


if __name__ == "__main__":
    filepath = sys.argv[1]
    print(extract_category(filepath))