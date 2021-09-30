import json
import codecs

class Classes:
    __classes = {}
    def get(self, name: str):
        return self.__classes.get(name)
    
    def getAll(self):
        return list(self.__classes)

    def __init__(self):
        with open("./data/classes.json", encoding="utf_8_sig") as file:
            jsonStr = file.read()
            self.__classes = json.loads(jsonStr)


if __name__ == "__main__":
    c = Classes()

    print(c.getAll())
    print(c.get("Воин"))
