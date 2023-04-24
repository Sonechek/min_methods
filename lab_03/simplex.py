from pulp import *

# Создание задачи линейного программирования
prob = LpProblem("SimplexProblem", LpMaximize)

# Создание переменных решения
x1 = LpVariable("x1", lowBound=0)
x2 = LpVariable("x2", lowBound=0)

# Добавление целевой функции
prob += 1 * x1 + 2 * x2

# Добавление ограничений
prob += -3 * x1 + 2 * x2 <= 9
prob += -3 * x1 + -4 * x2 <= -27
prob += 2 * x1 + x2 <= 14

# Решение задачи методом симплекса
prob.solve()

# Вывод результатов
print("Status:", LpStatus[prob.status])
for v in prob.variables():
    print(v.name, "=", v.varValue)
print("Total Cost =", value(prob.objective))
