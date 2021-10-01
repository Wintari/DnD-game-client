import json
import codecs

__backgrounds = {}

def get(name: str):
    return __backgrounds.get(name)

def getNames():
    return list(__backgrounds)

with open("./data/backgrounds.json", encoding="utf_8_sig") as file:
    jsonStr = file.read()
    __backgrounds = json.loads(jsonStr)