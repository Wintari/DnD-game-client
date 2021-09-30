import random
import enum

class ThrowTypes(enum.Enum):
    summ = 0,
    advantage = 1,
    hindrance = 2,
    withoutExtreme = 3


def throw(edges):
    return random.randint(1, edges)

def throwMany(count, edges, type):
    throws = [throw(edges) for i in range(0, count)]

    if(type is ThrowTypes.summ):
        return sum(throws)
    elif(type is ThrowTypes.advantage):
        return max(throws)
    elif(type is ThrowTypes.hindrance):
        return min(throws)
    elif(type is ThrowTypes.withoutExtreme):
        throws.remove(min(throws))
        throws.remove(max(throws))

        return sum(throws)