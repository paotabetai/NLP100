import collections
import sys

import numpy as np
import matplotlib.pyplot as plt

import read


plt.rcParams["font.family"] = "Hiragino Sans"

def calculate_frequency(filepath: str) -> None:
    surfaces = [posses['surface'] for posses in read.read(filepath) if not posses['pos'] in ['補助記号', 'BOS/EOS']]
    sum = len(surfaces)
    countered_dict = collections.Counter(surfaces)
    kv_list = [(key, value/sum) for key, value in countered_dict.items()]
    kv_list.sort(key=lambda x: x[1], reverse=True)
    y = np.array([tuple[1] for tuple in kv_list])
    counter = 1
    x = []
    for _ in y:
        x.append(counter)
        counter += 1
    plt.plot(x, y)
    ax = plt.gca()
    ax.set_xscale('log') 
    ax.set_yscale('log')
    plt.show()


if __name__ == "__main__":
    filepath: str = sys.argv[1]
    calculate_frequency(filepath)