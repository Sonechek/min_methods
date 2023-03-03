import math
import matplotlib


def f(x):
    return 2 + math.pow(x, 2) + math.pow(x, (2 / 3)) - math.log1p(1 + math.pow(x, 2 / 3)) - 2 * x * math.pow(math.atan(x), (1 / 3))

def gold(a, b, e):

    acc = 0

    while (abs(a - b) > e):
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


def kas(a, b , e):



a = 0.5
b = 1
e = math.pow(10, -6)


gold(a, b, e)
