from collections import ChainMap
import json

with open('zoo.json', encoding='UTF-8') as file:
    dicts = ChainMap(*json.load(file))

print(sum(dicts.values()))