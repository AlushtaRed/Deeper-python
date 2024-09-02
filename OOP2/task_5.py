# Задание №5
# Дорабатываем класс прямоугольник из прошлого семинара.
# Добавьте возможность сложения и вычитания.
# При этом должен создаваться новый экземпляр
# прямоугольника.
# Складываем и вычитаем периметры, а не длинну и ширину.
# При вычитании не допускайте отрицательных значений.

class Rectangle():
    def __init__(self, *args):
        self.length = args[0]
        self.width = args[1] if len(args) == 2 else args[0]
    def perimeter(self):
        return (self.length+self.width)*2
    def square(self):
        return(self.length*self.width)
    
    def __add__(self,other):
        new_perimetre = self.perimeter() + other.perimeter()
        return new_perimetre
    
a = Rectangle(2,3)
b = Rectangle(3,4)
c = a+b
print(c)