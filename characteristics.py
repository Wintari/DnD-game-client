import json
import dice

baseValue = 20

def toStr(values: dict[int, int, int, int, int, int]):
    return json.dumps(values)

def fromStr(value: str):
    return json.loads(value)

def getBaseStats():
    return {"strength": baseValue,
            "agility": baseValue,
            "constitution": baseValue,
            "intelligence": baseValue,
            "wisdom": baseValue,
            "charisma": baseValue}

def getRandomStats():
    return {"strength": dice.throwMany(6,6,dice.ThrowTypes.withoutExtreme),
            "agility": dice.throwMany(6,6,dice.ThrowTypes.withoutExtreme),
            "constitution": dice.throwMany(6,6,dice.ThrowTypes.withoutExtreme),
            "intelligence": dice.throwMany(6,6,dice.ThrowTypes.withoutExtreme),
            "wisdom": dice.throwMany(6,6,dice.ThrowTypes.withoutExtreme),
            "charisma": dice.throwMany(6,6,dice.ThrowTypes.withoutExtreme)}