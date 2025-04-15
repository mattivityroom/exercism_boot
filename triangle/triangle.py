def is_violation(sides):
    return False if sides[0] + sides[1] > sides[2] and \
            sides[0] + sides[2] > sides[1] and \
            sides[1] + sides[2] > sides[0] \
        else True

def equilateral(sides):
    if 0 in sides: return False
    return True if (sides[0] == sides[1] == sides[2]) else False


def isosceles(sides):
    if not is_violation(sides):
        return (sides[0] == sides[1] or sides[0] == sides[2] or sides[1] == sides[2])
    else:
        return False

def scalene(sides):
    # return not isosceles(sides) and not equilateral(sides)
    if not is_violation(sides):
        return not isosceles(sides) and not equilateral(sides)
    else:
        return False