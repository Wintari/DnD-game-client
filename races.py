import json
import codecs

__races = {}

def get(name: str):
    return __races.get(name)

def getNames():
    return list(__races)


with open("./data/races.json", encoding="utf_8_sig") as file:
    jsonStr = file.read()
    __races = json.loads(jsonStr)
