# ✔ Функция получает на вход список чисел.
# ✔ Отсортируйте его элементы in place без использования
# встроенных в язык сортировок.
# ✔ Как вариант напишите сортировку пузырьком.
# Её описание есть в википедии.

def bubble_sort(some_lst):
    for i in range(1, len(some_lst)):
        for j in range(len(some_lst)-i):
            if some_lst[j] > some_lst[j+1]:
                some_lst[j], some_lst[j+1] = some_lst[j+1], some_lst[j]


lst = [8, 4, 3, 9, 7]
bubble_sort(lst)
print(lst)
