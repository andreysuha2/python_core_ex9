import json
from pathlib import Path

DICTIONARY_PATH = Path("dictionary.json")
print(DICTIONARY_PATH.parent)

def main():
    with open(Path(DICTIONARY_PATH)) as dictionary_file:
        dictionary = json.load(dictionary_file)
        print(dictionary)


if __name__ == "__main__":
    main()