import math


def cart_to_polar(cart):

    x = cart[0]
    y = cart[1]

    return (math.sqrt(x**2 + y**2), math.atan(y / x))
