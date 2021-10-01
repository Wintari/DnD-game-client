import json
import codecs

__items = {}

def get(name: str):
    return __items.get(name)

def getNames():
    return list(__items)


with open("./data/items.json", encoding="utf_8_sig") as file:
    jsonStr = file.read()
    __items = json.loads(jsonStr)
