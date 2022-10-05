import sys

def cut(filepath: str, output_1: str, output_2: str) -> None:
    result_1 = []
    result_2 = []

    with open(filepath) as f:
        lines = f.readlines()
        for line in lines:
            splitted_line = line.split('\t')
            result_1.append(splitted_line[0])
            result_2.append(splitted_line[1])

    with open(output_1, mode='w') as f:
        f.write('\n'.join(result_1))

    with open(output_2, mode='w') as f:
        f.write('\n'.join(result_2))

if __name__ == "__main__":
    filepath = sys.argv[1]
    output_1 = sys.argv[2]
    output_2 = sys.argv[3]
    cut(filepath, output_1, output_2)