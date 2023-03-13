import cmath
import math
import sympy as sp

def fprime(x):
    return 2 + x**2 + x ** (2/3) - cmath.phase(sp.log(1 + x ** (2/3))) - 2 * x * cmath.phase(sp.atan(x ** (1/3)))


def fsecond(x):
    return 2 * x - 2 * cmath.phase(sp.atan(x ** (1/3)))


def newton(x, eps):
    acc = 0
    while True:
        x1 = x - (fprime(x) / fsecond(x))
        t = abs(x1 - x)
        if t < eps:
            break
        x = x1
        acc += 1
    print("Количество итераций - " + str(acc))
    print("X min - " + str(x1))
    print("F(X min) - " + str(fprime(x1)))
    return x
