import json
import dice

baseValue = 20

def toStr(values: dict[int, int, int, int, int, int]):
    return json.dumps(values)

def fromStr(value: str):
    return json.loads(value)

def getBaseStats():
    return {"сила": baseValue,
            "ловкость": baseValue,
            "телосложение": baseValue,
            "интеллект": baseValue,
            "мудрость": baseValue,
            "харизма": baseValue}

def getRandomStats():
    return {"сила": dice.throwMany(6,6,dice.ThrowTypes.withoutExtreme),
            "ловкость": dice.throwMany(6,6,dice.ThrowTypes.withoutExtreme),
            "телосложение": dice.throwMany(6,6,dice.ThrowTypes.withoutExtreme),
            "интеллект": dice.throwMany(6,6,dice.ThrowTypes.withoutExtreme),
            "мудрость": dice.throwMany(6,6,dice.ThrowTypes.withoutExtreme),
            "харизма": dice.throwMany(6,6,dice.ThrowTypes.withoutExtreme)}