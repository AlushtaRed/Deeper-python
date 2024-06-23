# Функция получает на вход словарь с названием компании в качестве ключа
# и списком с доходами и расходами (3-10 чисел) в качестве значения.
# ✔ Вычислите итоговую прибыль или убыток каждой компании. Если все компании
# прибыльные, верните истину, а если хотя бы одна убыточная — ложь.
import random
companies = {name: [random.randint(-1000,1000) for i_ in range(random.randint(3,10))] 
             for name in ['adidas', 'nike', 'reebok']}
print (companies)

def func(dct_comp):
    for i in dct_comp:
        dct_comp[i] = sum(dct_comp[i])
    print(dct_comp)
    return all(map(lambda x: x>0, dct_comp.values()))

print(func(companies))