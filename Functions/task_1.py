# ✔ Напишите функцию, которая принимает строку текста.
# Вывести функцией каждое слово с новой строки.
# ✔ Строки нумеруются начиная с единицы.
# ✔ Слова выводятся отсортированными согласно кодировки Unicode.
# ✔ Текст выравнивается по правому краю так, чтобы у самого
# длинного слова был один пробел между ним и номером строки.

text = 'Шла саша по шоссе и сосала сушку'


def sort_text(text: str):
    list_text = sorted(text.lower().split())
    max_len = max(list_text, key=len)
    for index, word in enumerate(list_text, 1):
        print(f'{index}. {word:>{len(max_len)}}')

if __name__ == 'main':
    sort_text(text)
