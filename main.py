# sin4x shx - arctgx-2=0, (2<=x<=4)
import math
import numpy as np


def f(x):
    return math.sin(4 * x) * math.sinh(x) - math.atan(x) - 2


def derrirative(x):
    return 4 * math.sinh(x) * math.cos(x * 4) + math.sin(4 * x) * math.cosh(x) - (1 / (1 + x ** 2))


# метод Ньютона

def newtonsMethod(f, a, derrirative, eps=1e-6):
    x0 = a
    xn = f(x0)
    xn1 = xn - f(xn) / derrirative(xn)
    while abs(xn1 - xn) > eps:
        xn = xn1
        xn1 = xn - f(xn) / derrirative(xn)
    return xn1


xs = (x * 0.01 for x in range(-70, 70))
for i in xs:
    x = newtonsMethod(f, i, derrirative)
    if 2 <= x <= 4:
        print(x)


