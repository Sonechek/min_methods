import numpy as np
from scipy.optimize import linprog
import warnings
warnings.filterwarnings('ignore')
a = np.array([40, 30, 20])
b = np.array([30, 25, 18, 20])

D = np.array([[1, 2, 6, 4],
              [3, 1, 3, 2],
              [5, 7, 5, 1]])


# Необходима функция нахождения индексов минимального элемента матрицы
def ij(c_min):
    c = np.inf
    for i in range(c_min.shape[0]):
        for j in range(c_min.shape[1]):
            if (c_min[i, j] != 0) and (c_min[i, j] < c):
                c = c_min[i, j]
                i_, j_ = i, j
    return i_, j_


# Функция минимального элемента
def M_min(a_, b_, c_, print_=False):
    a = np.copy(a_)
    b = np.copy(b_)
    c = np.copy(c_)

    # Проверяем условие замкнутости: если не замкнута - меняем соотвествующие векторы и матрицу трансп. расходов
    if a.sum() > b.sum():
        b = np.hstack((b, [a.sum() - b.sum()]))
        c = np.hstack((c, np.zeros(len(a)).reshape(-1, 1)))
    elif a.sum() < b.sum():
        a = np.hstack((a, [b.sum() - a.sum()]))
        c = np.vstack((c, np.zeros(len(b))))

    m = len(a)
    n = len(b)
    x = np.zeros((m, n), dtype=int)  # создаем матрицу для x и заполняем нулями
    funk = 0
    while True:
        c_min = np.zeros((m, n))
        for i in range(m):
            for j in range(n):
                c_min[i, j] = (c[i, j] * min(a[i], b[j]))  # составляем матрицу суммарных расходов
        i, j = ij(c_min)  # определяем индексы минимального элемента составленной матрицы суммарных расходов
        x_ij = int(min(a[i], b[j]))
        x[i, j] = x_ij  # добавляем элемент x_ij в матрицу x
        funk += int(c_min[i, j])  # добавляем x_ij в итоговую функцию
        a[i] -= x_ij  #
        b[j] -= x_ij  # обновляем векторы a и b
        if print_:
            print('c_min:')
            print(c_min.astype(int))
            print('a: ', a)
            print('b: ', b)
            print()
        if len(c_min[c_min > 0]) == 1:  # повторяем до сходимости метода
            break
    return x, funk  # возращаем матрицу x и целевую функцию
x, funk = M_min(a, b, D, print_ = True)
print('x: ')
print(x)
print('Целевая функция: ', funk)


def sev_zap(a_, b_, c_):
    a = np.copy(a_)
    b = np.copy(b_)
    c = np.copy(c_)

    # Проверяем условие замкнутости:
    if a.sum() > b.sum():
        b = np.hstack((b, [a.sum() - b.sum()]))
        c = np.hstack((c, np.zeros(len(a)).reshape(-1, 1)))
    elif a.sum() < b.sum():
        a = np.hstack((a, [b.sum() - a.sum()]))
        c = np.vstack((c, np.zeros(len(b))))

    m = len(a)
    n = len(b)
    i = 0
    j = 0
    funk = 0
    x = np.zeros((m, n), dtype=int)
    while (i < m) and (j < n):  # повторяем цикл до сходимости метода
        x_ij = min(a[i], b[j])  # проверяем минимальность a_i и b_j
        funk += c[i, j] * min(a[i], b[j])  # записываем в итоговую функцию элемент трат
        a[i] -= x_ij  #
        b[j] -= x_ij  # обновляем векторы a и b
        x[i, j] = x_ij  # добавляем элемент x_ij в матрицу x

        if a[i] > b[j]:  # делаем сдвиги при выполнении условий
            j += 1
        elif a[i] < b[j]:
            i += 1
        else:
            i += 1
            j += 1
    return x, funk  # возращаем матрицу x и целевую функцию

def delta(a, b, c, x):

    # Проверяем условие замкнутости:
    if a.sum() > b.sum():
        b = np.hstack((b, [a.sum() - b.sum()]))
        c = np.hstack((c, np.zeros(len(a)).reshape(-1, 1)))
    elif a.sum() < b.sum():
        a = np.hstack((a, [b.sum() - a.sum()]))
        c = np.vstack((c, np.zeros(len(b))))

    m = len(a)
    n = len(b)

    u = np.zeros(m)
    v = np.zeros(n)

    for i in range(m):
        for j in range(n):
            if x[i, j] != 0:  # если элемент матрицы x не равен 0, расчитываем для данных индексов векторы u и v
                if v[j] != 0:
                    u[i] = c[i, j] - v[j]
                else:
                    v[j] = c[i, j] - u[i]

    delta = np.zeros((m, n))
    for i in range(m):
        for j in range(n):
            delta[i, j] = u[i] + v[j] - c[i, j]  # расчитываем элемент дельта матрицы
    return delta


def prepare(a, b):
    m = len(a)
    n = len(b)
    h = np.diag(np.ones(n))
    v = np.zeros((m, n))
    v[0] = 1
    for i in range(1, m):
        h = np.hstack((h, np.diag(np.ones(n))))
        k = np.zeros((m, n))
        k[i] = 1
        v = np.hstack((v, k))
    return np.vstack((h, v)).astype(int), np.hstack((b, a))



print('Матрица системы ограничений: \n', prepare(a, b)[0])
x, funk = M_min(a, b, D)
print('Метод минимального элемента: \n', x)
print('Целевая функция: ', funk)
print()
print('Дельта матрица для М - метода: \n', delta(a, b, D, x))
x1, funk1 = sev_zap(a, b, D)
print('Метод северо-западного угла: \n', x1)
print('Целевая функция: ', funk1)
print()
print('Дельта матрица для метода северо-западного угла: \n', delta(a, b, D, x1))

x1, funk1 = sev_zap(a, b, D)
print('Метод северо-западного угла: \n', x1)
print('Целевая функция: ', funk1)
print()
print('Дельта матрица для метода северо-западного угла: \n', delta(a, b, D, x1))
