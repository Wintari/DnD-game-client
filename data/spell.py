import json
import codecs

__spells = {}

def get(name: str):
    return __spells.get(name)

def getNames():
    return list(__spells)


with open("./data/spells.json", encoding="utf_8_sig") as file:
    jsonStr = file.read()
    __spells = json.loads(jsonStr)
