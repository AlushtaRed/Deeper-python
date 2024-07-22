# ✔ Напишите программу, которая вычисляет площадь
# круга и длину окружности по введённому диаметру.
# ✔ Диаметр не превышает 1000 у.е.
# ✔ Точность вычислений должна составлять
# не менее 42 знаков после запятой.

from decimal import Decimal, getcontext
from math import pi

getcontext().prec = 42
d = 4
p = Decimal(pi)
d = Decimal(d)
s = p*(d/2)**2
l = p*d
print(s, l)