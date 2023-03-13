import math
import gold
import newton

a = 0.5
b = 1
eps = math.pow(10, -6)


gold.gold(a, b, eps)
gold.grafik(a, b)
gold.popolam(a, b, eps)
newton.newton(a, eps)
