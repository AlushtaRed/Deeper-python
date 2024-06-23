# ✔ Создайте несколько переменных заканчивающихся и не оканчивающихся на «s».
# ✔ Напишите функцию, которая при запуске заменяет содержимое переменных
# оканчивающихся на s (кроме переменной из одной буквы s) на None.
# ✔ Значения не удаляются, а помещаются в одноимённые переменные без s на конце.
from typing import Callable

start = 100
s = 'zxcv'
apples = 25
codes = 10110110

def func():
    temp_dict = {}
    for i in globals():
        if not i.startswith('__'):
            if i.endswith('s') and len(i)>1:
                temp_dict[i[:-1]] = globals()[i]
                temp_dict[i] = None
    globals().update(temp_dict)

func()
print([item for item in globals().items() if not item[0].startswith('__')])