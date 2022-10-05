import sys

def split(filepath: str, n: int) -> None:

    with open(filepath) as f:
        file = f.readlines()
        f_len = len(file)
        file_n = f_len // n
        tmp_line = []
        file_counter = 0
        tmp_counter = 0
        total_counter = 0
        for line in file:
            tmp_line.append(line)
            tmp_counter += 1
            total_counter += 1
            if tmp_counter == file_n or total_counter == f_len:
                with open("{}".format(filepath + str(file_counter)), "w") as f_r:
                    f_r.writelines(tmp_line)
                tmp_line = []
                tmp_counter = 0
                file_counter += 1


if __name__ == "__main__":
    filepath = sys.argv[1]
    n = int(sys.argv[2])
    split(filepath, n)