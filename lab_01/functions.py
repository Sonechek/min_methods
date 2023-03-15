import random
from matplotlib import pyplot as plt
import math


def grafik(a, b):
    x_mas = []
    y_mas = []
    while a < b:
        x_mas.append(a)
        y_mas.append(fprime(a))
        a = a + 0.01
    plt.plot(x_mas, y_mas, color='red')
    plt.show()


def fprime(x):
    return (x ** 2 / 2) - math.cos(x)


def fsecond(x):
    return x + math.sin(x)


def popolam(a, b, eps):
    acc = 0
    d = 10 ** -7
    while abs(a - b) >= eps:
        x1 = (a + b - d) / 2
        x2 = (a + b + d) / 2
        if fprime(x1) > fprime(x2):
            a = x1
        else:
            b = x2
        acc += 1
    print("Количество итераций - " + str(acc))
    print("X min - " + str((a + b) / 2))
    print("F(X min) - " + str(fprime((a + b) / 2)))


def gold(a, b, eps):
    acc = 0
    while abs(a - b) >= eps:
        x1 = a + ((3 - math.sqrt(5) / 2) * (b - a))
        x2 = a + ((math.sqrt(5) - 1 / 2) * (b - a))
        func_x1 = fprime(x1)
        func_x2 = fprime(x2)
        if func_x1 > func_x2:
            a = x2
        else:
            b = x1
        acc += 1
    print("Количество итераций - " + str(acc))
    print("X min - " + str((a + b) / 2))
    print("F(X min) - " + str(fprime((a + b) / 2)))


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


def nk(b):
    x2 = random.uniform(0, 3)
    x, e = b, 0.0000001
    xx = x2
    acc = 0
    while 1:
        acc += 1
        if fsecond(x) != 0:
            x = x-fprime(x)/fsecond(x)
        else:
            print('Error')
            break
        if abs(x-xx) < e:
            print('Количество итераций - ' + str(acc))
            print('X min - ' + str(x))
            print('F(x Min) - ' + str(fprime(x)))

            break
        xx = x
        print(x)
