# Создайте класс Сотрудник.
# Воспользуйтесь классом человека из прошлого задания.
# У сотрудника должен быть:
# ○ шестизначный идентификационный номер
# ○ уровень доступа вычисляемый как остаток от деления
# суммы цифр id на семь
class Human():
    def __init__(self, name, surname, age, sex):
        self.name = name
        self.surname = surname
        self._age = age
        self.sex = sex

    def birthday(human):
        return human._age+1
    
    def full_name(human):
        print(f'{human.name} {human.surname}')
        return f'{human.name} {human.surname}'

class Personal(Human):
    def __init__(self, id, *args, **kwargs):
        self.id = id
        self.level = int(id%7)
        super().__init__(*args,**kwargs)

igor = Personal(777777,'Igor','V', 39,'M')
# alex = Human()
print(f'{igor.name = }, {igor.id = }, {igor.level = }, {Personal.full_name(igor) = }')
