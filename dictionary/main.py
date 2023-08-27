import json
from pathlib import Path

DICTIONARY_PATH = Path("data.json")

dictionary = None

try:
    with open(DICTIONARY_PATH) as dictionary_file:
        dictionary = json.load(dictionary_file)
except FileNotFoundError:
    dictionary = {}

def save_dictionary():
    with open(DICTIONARY_PATH, "w") as dictionary_file:
        dictionary_file.write(json.dump(dictionary))