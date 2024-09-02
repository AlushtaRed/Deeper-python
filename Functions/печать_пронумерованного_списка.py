# ✔ Напишите функцию, которая принимает строку текста.
# Вывести функцией каждое слово с новой строки.
# ✔ Строки нумеруются начиная с единицы.
# ✔ Слова выводятся отсортированными согласно кодировки Unicode.
# ✔ Текст выравнивается по правому краю так, чтобы у самого
# длинного слова был один пробел между ним и номером строки.


def print_text(text):
    result = sorted(text.split())

    len_max = max(result, key=len)
    len_max = len(len_max)

    for a,b in enumerate(result,1):
        print(f'{a}.{b:>{len_max+1}}')


print_text('а я иду шагаю по москве')