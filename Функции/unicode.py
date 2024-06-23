# ✔ Напишите функцию, которая принимает строку текста.
# ✔ Сформируйте список с уникальными кодами Unicode каждого
# символа введённой строки отсортированный по убыванию.

def unicode(text):
    # split_text = list(text)
    result =[]
    for i in text:
        i = ord(i)
        result.append(i)
    result = list(set(result))
    print(sorted(result, reverse=True))

unicode('Компот вишневый')
# print(ord('s'))