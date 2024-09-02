# ✔ Продолжаем развивать задачу 2.
# ✔ Возьмите словарь, который вы получили.
# Сохраните его итераторатор.
# ✔ Далее выведите первые 5 пар ключ-значение,
# обращаясь к итератору, а не к словарю.
lst = 'veverlkывака5%'
result_dict = {i:ord(i) for i in lst}

iter_dict = iter(result_dict.items())


print(next(iter_dict))
print(next(iter_dict))
print(next(iter_dict))