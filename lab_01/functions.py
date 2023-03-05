import random
from matplotlib import pyplot as plt
import sympy as sp
import math


def f(x):
    return 2 + sp.Pow(x, 2) + sp.Pow(x, 2 / 3) - sp.log(1 + sp.Pow(x, 2 / 3)) - 2 * x * sp.atan(sp.Pow(x, 1/3))


def diffed(i):
     x = sp.Symbol('x')
     g = 2 + sp.Pow(x, 2) + sp.Pow(x, 2 / 3) - sp.log(1 + sp.Pow(x, 2 / 3)) - 2 * x * sp.atan(sp.Pow(x, 1 / 3))
     g_x = g.diff(x)
     # print(g_x)
     return g_x


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


def kas(a, b, eps):
    acc = 0
    xn1 = 0
    x_rand = random.uniform(a, b)
    # d_a = diffed(a)
    # d_b = diffed(b)
    print(f(x_rand))
    print(diffed(x_rand))
    while (abs(xn1-x_rand)>=eps):
        x_min = (f(b) - f(a) + (d_a * a) - (d_b * b)) / (d_a - d_b)
        xn_rand = x_rand - (f(x_rand)/diffed(x_rand))
        if(diffed(x_min)<0):
        print(x_rand)
        acc += 1
    print(x_min)


def grafik(a,b):
    x_mas = []
    y_mas = []
    while (a < b):
        x_mas.append(a)
        y_mas.append(f(a))
        a = a + 0.01
    plt.plot(x_mas, y_mas, color='red')
    plt.show()
    # print(min(y_mas))
