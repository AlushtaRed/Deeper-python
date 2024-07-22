# ✔ Напишите функцию, которая заполняет файл
# (добавляет в конец) случайными парами чисел.
# ✔ Первое число int, второе - float разделены вертикальной чертой.
# ✔ Минимальное число - -1000, максимальное - +1000.
# ✔ Количество строк и имя файла передаются как аргументы функции. 
from random import randint, uniform, sa

def filing_in_file(num: int, name: str):
    with open(name, 'w', encoding='utf-8') as f:
        f.writelines('\n'.join([f'{randint(-1000,1000)} | {round(uniform(-1000,1000),2)}' for i in range(num)]))

filing_in_file(15,'nums.txt')