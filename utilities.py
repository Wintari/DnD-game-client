def calculateModifier(NakedValue):
    return int((NakedValue - 10) / 2)


def calculateMaxExp(currentLvl):
    if currentLvl == 1:
        return 1000
    elif currentLvl == 2:
        return 3000
    elif currentLvl == 3:
        return 6000
    elif currentLvl == 4:
        return 10000
    elif currentLvl == 5:
        return 15000
    elif currentLvl == 6:
        return 21000
    elif currentLvl == 7:
        return 28000
    elif currentLvl == 8:
        return 36000
    elif currentLvl == 9:
        return 45000
    elif currentLvl == 10:
        return 55000
    elif currentLvl == 11:
        return 66000
    elif currentLvl == 12:
        return 78000
    elif currentLvl == 13:
        return 91000
    elif currentLvl == 14:
        return 105000
    elif currentLvl == 15:
        return 120000
    elif currentLvl == 16:
        return 136000
    elif currentLvl == 17:
        return 153000
    elif currentLvl == 18:
        return 171000
    elif currentLvl == 19:
        return 190000
    else:
        return 0


def calculateProficiencyBonus(currentLvl):
    if currentLvl <= 4:
        return 2
    elif currentLvl <= 9:
        return 3
    elif currentLvl <= 12:
        return 4
    elif currentLvl <= 17:
        return 5
    elif currentLvl <= 20:
        return 6
    else:
        return 0