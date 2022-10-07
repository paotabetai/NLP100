import sys
import re
import read


def extract_section(filepath: str) -> str:
    readjson: str = read.read_json(filepath)
    result: list = []
    pattern = re.compile("==+.*")
    for line in readjson.split('\n'):
        match = pattern.search(line)
        if match:
            i = 2
            name_pattern = re.compile(r"==+(.+)==+")
            name_match = name_pattern.search(line)
            multi_pattern = re.compile("{}+.*".format("=" * i))
            multi_match = multi_pattern.search(line)
            while multi_match:
                name_pattern = re.compile(
                    r"{}+(.+){}+".format("=" * i, "=" * i)
                )
                name_match = name_pattern.search(line)
                i += 1
                multi_pattern = re.compile("{}+.*".format("=" * i))
                multi_match = multi_pattern.search(line)
            result.append(str(i - 2) + " " + name_match.group(1))
    return '\n'.join(result)


if __name__ == "__main__":
    filepath: str = sys.argv[1]
    print(extract_section(filepath))