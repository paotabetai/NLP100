import json
import sys


def read_json(filepath: str) -> str:
    decoder = json.JSONDecoder()
    with open(filepath) as f:
        line = f.readline()
        while line:
            article = decoder.raw_decode(line)[0]
            if article['title'] == "イギリス":
                return article['text']
            line = f.readline()


if __name__ == "__main__":
    filepath = sys.argv[1]
    print(read_json(filepath))