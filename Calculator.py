class Calculator(object):
"""docstring for ClassName"""


def __init__(self, arg):
    super(ClassName, self).__init__()
    self.arg = arg


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2, roundDivision):
    if roundDivision is True:
        return n1 // n2
    else:
        return n1 / n2


def power(n1, n2):
    return n1 ** n2


def squareArea(side):
    return side * side


def circleArea(radius):
    return 3.14 * (radius ** 2)


def rectangleArea(side1, side2):
    return side1 * side2


def trapezoidArea(base1, base2, height):
    return ((base1 + base2) * height) / 2


def cubeVolume(side):
    return side ** 3


def boxVolume(length, width, height):
    return length * width * side


def sphereVolume(radius):
    return (4 / 3) * 3.14 * (r**3)


def cylinderVolume(radius, height):
    return self.circleArea(radius) * height


def baskaraFormula():


def timeDifferenceBetweenDates():


def howLongUntilTime():
