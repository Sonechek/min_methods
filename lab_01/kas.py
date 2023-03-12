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
    xmin = (fprime(b) - fprime(a) + fsecond(a)* a - fsecond(b) * b)/(fsecond(a)-fsecond(b))
    while(abs(fprime(xmin)-ymin(xmin, xmin1))>eps):
        if fsecond(xmin) < 0:
            xmin = xr
            a = xmin
            b = b
        if fsecond(xmin) > 0:
            xmin = xl
            a = a
            b = xmin


