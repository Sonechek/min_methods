import cmath
import math
import random

import sympy as sp

def fprime(x):
    return 2 + x**2 + x ** (2/3) - cmath.phase(sp.log(1 + x ** (2/3))) - 2 * x * cmath.phase(sp.atan(x ** (1/3)))


def fsecond(x):
    return 2 * x - 2 * cmath.phase(sp.atan(x ** (1/3)))

def ymin(xmin, xmin1):
    return (fprime(xmin)+(fsecond(xmin)*(xmin1 - xmin)))


def kas(a, b, eps):
    xmin1 = random.uniform(a, b)
    acc = 0
    while True:
        xmin = (fprime(b) - fprime(a) + fsecond(a) * a - fsecond(b) * b) / (fsecond(a) - fsecond(b))
        t = abs(fprime(xmin)-ymin(xmin, xmin1))
        acc += 1
        if isinstance(xmin, complex) == True:
            xmin = cmath.phase(xmin)
        if fsecond(xmin) < 0:
            xmin1 = xmin
            a = xmin
            b = b
        if fsecond(xmin) > 0:
            xmin1 = xmin
            b = xmin
            a = a
        if t < eps:
            break
        print(acc)
        print(xmin)
        print(xmin1)
    print(acc)

a = 0.5
b = 1
eps = math.pow(10, -6)
kas(a, b, eps)
