# Создайте класс прямоугольник.
# Класс должен принимать длину и ширину при создании
# экземпляра.
# У класса должно быть два метода, возвращающие периметр
# и площадь.
# Если при создании экземпляра передаётся только одна
# сторона, считаем что у нас квадрат.

class Rectangle():
    def __init__(self, *args):
        self.length = args[0]
        self.width = args[1] if len(args) == 2 else args[0]
    def perimeter(self):
        return (self.length+self.width)*2
    def square(self):
        return(self.length*self.width)

rectangle1 = Rectangle(2)
print(f'{rectangle1.length = }, {rectangle1.width = }, {rectangle1.perimeter() = }, {rectangle1.square() = }')