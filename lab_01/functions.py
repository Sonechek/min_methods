import random
from matplotlib import pyplot as plt
import sympy as sp
import math


def f(x):
    # temp =math.atan(x)
    temp = sp.log(1 + x ** (2/3))
    print(temp)
    return 2 + x**2 + x ** (2/3) - sp.log(1 + x ** (2/3)) - 2 * x * sp.atan(x ** (1/3))

def diffed(i):
     x = sp.Symbol('x')
     g = 2 + x**2 + x ** (2/3) - sp.log(1 + x ** (2/3)) - 2 * x * sp.atan(x ** (1/3))
     g_x = g.diff(x)
     g_x = str(g_x)
     g_x = g_x.replace('atan', 'math.atan')
     g_x = g_x.replace('x', str(i))
     g_x = eval(g_x)
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
    x_min = (f(b) - f(a) + (diffed(s) * a) - (diffed(b) * b)) / (diffed(a) - diffed(b))
    x_min = str(x_min).replace('pi', '3.14')
    x_min = x_min.replace('log', 'math.log')
    x_min = eval(x_min)
    print(x_min)
    # temp = temp.replace('x', str(a))
    # temp = eval(temp)
    # y_min = f(x_min) + (diffed(x_min) * (x_min - x_min))
    # while (abs(xn1-x_rand)>=eps):
    #     xn_rand = x_rand - (f(x_rand)/diffed(x_rand))
    #     if(diffed(x_min)<0):
    #         a = x_min
    #         x_min = xr
    #     else:
    #         b = x_min
    #         x_min = xl
    #     print(x_rand)
    #     acc += 1
    # print(x_min)


def newton(a, b, eps):
    rand_1 = random.randint(1, 2)
    if (rand_1 == 1):
        xk = a
    else:
        xk = b
    xkn = 1
    acc = 0
    while (abs(xkn - xk) > eps):
        if acc == 0:
            xk = xk
        else:
            xk = xkn
        xk_d = diffed(xk)
        fun_xk = f(xk)
        xkn = (xk - fun_xk) / xk_d
        print(xkn)
        acc += 1
    print(acc)
    print(xkn)


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
