# ✔ Создайте вручную кортеж содержащий элементы разных типов.
# ✔ Получите из него словарь списков, где:
#   ключ — тип элемента,
#   значение — список элементов данного типа.

my_tuple = (1, 2, 3, 'ferf', 'ffewfew', 'dfe', 2.1, 4.5)
my_dict = {}
for i in my_tuple:
    key = type(i)
    my_dict.setdefault(key,[]).append(i)
print(my_dict)