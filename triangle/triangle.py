def is_violation(sides):
    sides = sorted(sides)
    return not sum(sides[:2]) > sides[2] and len(sides) < 4

def equilateral(sides):
    return not is_violation(sides) and len(set(sides)) == 1

def isosceles(sides):
    return not is_violation(sides) and len(set(sides)) <= 2

def scalene(sides):
    return not is_violation(sides) and len(set(sides)) == 3