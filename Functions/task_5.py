# ✔ Функция принимает на вход три списка одинаковой длины:
# ✔ имена str,
# ✔ ставка int,
# ✔ премия str с указанием процентов вида «10.25%».
# ✔ Вернуть словарь с именем в качестве ключа и суммой
# премии в качестве значения.
# ✔ Сумма рассчитывается как ставка умноженная на процент премии. 
names = ['Борис', 'Иван', 'Петр', "Сергей"]
salarys = [10000, 12000, 16000, 14000]
awards = ['12.35%', '10.25%', '7.75%', '8.85%']


def make_dict(name:str, salary:int, award:str):
    return {name:salary*float(award.rstrip('%'))/100 for name, salary, award in zip(names,salarys,awards)}

print(make_dict(names,salarys,awards))
