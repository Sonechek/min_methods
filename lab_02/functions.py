import math

import numpy as np
from matplotlib import pyplot as plt


def fprime(x1, x2):
    return x1 ** 4 + x2 ** 4 + math.sqrt(2 + x1 ** 2 + x2 ** 2) - 2 * x1 + 3 * x2


def fsx1(x1, x2):
    return (4 * x1 ** 3) + (x1 / math.sqrt(x1 ** 2 + x2 ** 2 + 2)) - 2


def fsx2(x1, x2):
    return (4 * x2 ** 3) + (x2 / math.sqrt(x1 ** 2 + x2 ** 2 + 2)) + 3


def grad(x1, x2):
    return {(4 * x1 ** 3) + (x1 / math.sqrt(x1 ** 2 + x2 ** 2 + 2)) - 2,
            (4 * x2 ** 3) + (x2 / math.sqrt(x1 ** 2 + x2 ** 2 + 2)) + 3}


def grafik():
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1, projection="3d")

    x1, x2 = np.meshgrid(np.linspace(-0.2, 1, 1000), np.linspace(-1, 0, 1000))
    z = x1 ** 4 + x2 ** 4 + np.sqrt(2 + x1 ** 2 + x2 ** 2) - 2 * x1 + 3 * x2

    ax.plot_surface(x1, x2, z, color="purple")
    plt.show()


def gradient():
    n = 1
    alpha = 0.1
    alpha = alpha / n
    eps = 10 ** -6
    x1 = 0
    x2 = 0
    acc = 0
    while 1:
        x11 = x1 - fsx1(x1, x2) * alpha
        x21 = x2 - fsx2(x1, x2) * alpha
        t = abs(fprime(x1, x2) - fprime(x11, x21))
        acc += 1
        if t < eps:
            break
        x1 = x11
        x2 = x21

    print('x1, x2 - ' + str(x1), str(x2))
    print('Количество итераций - ' + str(acc))


def hookjeevs():
    x1 = 0
    x2 = 0
    di1 = 1
    di2 = 1
    alpha = 2
    eps = 10 ** -6
    acc = 0
    while True:
        x1 = fprime(x1 + di1, x2)
        x2 = fprime(x1, x2 + di2)
