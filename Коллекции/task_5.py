# ✔ Создайте вручную список с повторяющимися целыми числами.
# ✔ Сформируйте список с порядковыми номерами
# нечётных элементов исходного списка.
# ✔ Нумерация начинается с единицы.

new_list = []
my_list = [1, 4, 2, 4, 5, 3, 5, 6, 23, 45, 23]

for index,value in enumerate(my_list,1):
    if value%2 != 0:
        new_list.append(index)
print(new_list)
print([index+1 for index,value in enumerate(my_list) if value%2 !=0])