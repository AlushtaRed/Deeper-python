# Создайте класс Моя Строка, где:
# будут доступны все возможности str
# дополнительно хранятся имя автора строки и время создания
# (time.time)
import time

class MyString(str):
    """
    Документация к моей строке
    """
    def __new__(cls,name):
        instance = super().__new__(cls)
        instance.name = name
        instance.time = time.time()
        return instance
    def __str__(self):
        return 'tekst'
my_string = MyString('Igor')
# print(my_string.time, my_string.name)

# print(help(MyString))
# print(MyString.__doc__)

print(my_string)
