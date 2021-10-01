import random
import enum

class ThrowTypes(enum.Enum):
    summ = 0,
    advantage = 1,
    hindrance = 2,
    withoutMin = 3,
    withoutMax = 4


def throw(edges, modifically, characteristic):
    return random.randint(1, edges) + modifically + characteristic

def throwMany(count, edges, type, modifically, characteristic):
    throws = [throw(edges, modifically, characteristic) for i in range(0, count)]
    if(type is ThrowTypes.summ):
        return sum(throws)
    elif(type is ThrowTypes.advantage):
        return max(throws)
    elif(type is ThrowTypes.hindrance):
        return min(throws)
    elif(type is ThrowTypes.withoutMin):
        throws.remove(min(throws))
        return sum(throws)
    elif(type is ThrowTypes.withoutMax):
        throws.remove(max(throws))
        return sum(throws)
