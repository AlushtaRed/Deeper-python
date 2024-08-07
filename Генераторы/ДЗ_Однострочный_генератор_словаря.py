# Напишите однострочный генератор словаря, 
# который принимает на вход три списка одинаковой длины: имена str, 
# ставка int, премия str с указанием процентов вида 10.25%.
# В результате result получаем словарь с именем в качестве 
# ключа и суммой премии в качестве значения.
names = ["Alice", "Bob", "Charlie"]
salary = [5000, 6000, 7000]
bonus = ["10%", "5%", "15%"]
result = {name:salary*float(bonus[:-1])/100 for name, salary, bonus in zip(names,salary,bonus)}
print(result)