import math


def cart_to_polar(x, y):

    return (math.sqrt(x**2 + y**2), math.atan(y / x))
