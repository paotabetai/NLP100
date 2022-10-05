import re
import sys

def replace(filepath: str) -> str:
    result = []
    with open(filepath) as f:
        lines = f.readlines()
        for line in lines:
            replaced_line = re.sub(r'\t', " ", line)
            result.append(replaced_line)
    return ''.join(result)

if __name__ == "__main__":
    filepath = sys.argv[1]
    print(replace(filepath))