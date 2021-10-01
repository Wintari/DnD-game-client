import json
import codecs

__classes = {}

def get(name: str):
    return __classes.get(name)

def getNames():
    return list(__classes)

with open("./data/classes.json", encoding="utf_8_sig") as file:
    jsonStr = file.read()
    __classes = json.loads(jsonStr)
