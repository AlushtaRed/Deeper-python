# Напишите класс для хранения информации о человеке:
# ФИО, возраст и т.п. на ваш выбор.
# У класса должны быть методы birthday для увеличения
# возраста на год, full_name для вывода полного ФИО и т.п. на
# ваш выбор.
# Убедитесь, что свойство возраст недоступно для прямого
# изменения, но есть возможность получить текущий возраст.

class Human():
    def __init__(self, name, surname, age, sex):
        self.__name = name
        self.surname = surname
        self.__age = age
        self.sex = sex

    # def birthday(human):
    #     return human.__age+1
    
    # def full_name(human):
    #     print(f'{human.name} {human.surname} {human.__age}')
    @property
    def name(self):
        return self.__name
    
    # @name.setter
    # def name(self, value):
    #     self.__name = value
igor = Human('Igor','V', 39,'M')
# igor.__age = 50
# print(igor.__age)
# Human.full_name(igor)
# print(Human.birthday(igor))
print(igor.name)
