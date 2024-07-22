# ✔ Вручную создайте список с целыми числами, которые
# повторяются. Получите новый список, который содержит
# уникальные (без повтора) элементы исходного списка.
# ✔ *Подготовьте два решения, короткое и длинное, которое
# не использует другие коллекции помимо списков.
my_list = [1,2,3,4,5,6,7,45,3,2,1,6,7,45]
set_list = set(my_list)
print(list(set_list))
result = []
result2 = []
for i in my_list:
    if my_list.count(i) == 1:
        result.append(i)
print(result)
for i in my_list:
    if i not in result2:
        result2.append(i)
print(result2)