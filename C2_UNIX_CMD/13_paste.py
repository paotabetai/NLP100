import sys


def paste(input_1: str, input_2: str, output: str) -> None:

    with open(input_1) as f:
        input_1_list = f.readlines()

    with open(input_2) as f:
        input_2_list = f.readlines()

    with open(output, mode="w") as f:
        f.write(
            '\n'.join(
                [col1.strip() + "\t" + col2.strip()
                    for col1, col2 in zip(input_1_list, input_2_list)]
                )
            )


if __name__ == "__main__":
    input_1 = sys.argv[1]
    input_2 = sys.argv[2]
    output_1 = sys.argv[3]
    paste(input_1, input_2, output_1)