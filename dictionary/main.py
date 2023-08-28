import json
import os
from pathlib import Path

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
DICTIONARY_PATH = Path(os.path.join(__location__, "data.json"))

dictionary = None

try:
    with open(DICTIONARY_PATH, 'r', encoding='utf-8') as dictionary_file:
        dictionary = json.load(dictionary_file)
except FileNotFoundError:
    print('Dictionary file not found, file will be create when you finishing your work!')
    dictionary = {}

def save_dictionary():
    with open(DICTIONARY_PATH, "w") as dictionary_file:
        json.dump(dictionary, dictionary_file)