# Создайте класс окружность.
# Класс должен принимать радиус окружности при создании
# экземпляра.
# У класса должно быть два метода, возвращающие длину
# окружности и её площадь.
import math

class Circle():
    def __init__(self, r):
        self.r = r

    def square(self):
        return math.pi*(self.r)**2
    def length_(self):
        return 2*math.pi*self.r
    
circle1 = Circle(0.5)
print(f'{circle1.length_()=} {circle1.square()=}')