import json
import codecs

__character = None

def getDefault():
    return __character

def load(path: str):
    with open(path, encoding="utf_8_sig") as file:
        jsonStr = file.read()
        return json.loads(jsonStr)

def save(path: str, character: dict):
    with open(path, "w", encoding="utf_8_sig") as file:
        file.write(json.dumps(character))

with open("./data/character.json", encoding="utf_8_sig") as file:
    jsonStr = file.read()
    __character = json.loads(jsonStr)




