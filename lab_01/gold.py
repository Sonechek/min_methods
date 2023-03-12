from matplotlib import pyplot as plt
import sympy as sp
import math


def grafik(a, b):
    x_mas = []
    y_mas = []
    while (a < b):
        x_mas.append(a)
        y_mas.append(f(a))
        a = a + 0.01
    plt.plot(x_mas, y_mas, color='red')
    plt.show()


def f(x):
    return 2 + x**2 + x ** (2/3) - sp.log(1 + x ** (2/3)) - 2 * x * sp.atan(x ** (1/3))


def gold(a, b, eps):
    acc = 0
    while (abs(a - b) >= eps):
        x1 = a + ((3 - math.sqrt(5) / 2) * (b - a))
        x2 = a + ((math.sqrt(5) - 1 / 2) * (b - a))
        func_x1 = f(x1)
        func_x2 = f(x2)
        if (func_x1 > func_x2):
            a = x1
        else:
            b = x2
        acc += 1
    print(acc)
    print((a + b) / 2)
    print(f(a + b / 2))
