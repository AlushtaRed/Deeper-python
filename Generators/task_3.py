# ✔ Продолжаем развивать задачу 2.
# ✔ Возьмите словарь, который вы получили.
# Сохраните его итераторатор.
# ✔ Далее выведите первые 5 пар ключ-значение,
# обращаясь к итератору, а не к словарю.

text = 'я иду шагаю по москве'
text_dict = {i:ord(i) for i in text}
print(text_dict)
iter_dict = iter(text_dict.items())

print(next(iter_dict))
print(next(iter_dict))
print(next(iter_dict))