# ✔ Пользователь вводит строку текста.
# ✔ Подсчитайте сколько раз встречается
# каждая буква в строке без использования
# метода count и с ним.
# ✔ Результат сохраните в словаре, где ключ —
# символ, а значение — частота встречи
# символа в строке.
# ✔ Обратите внимание на порядок ключей.
# Объясните почему они совпадают
# или не совпадают в ваших решениях

text = 'а я иду шагаю по москве'
result = {}
for i in text:
    result[i] = result.get(i,0)+1
print(result)

for i in text:
    result[i] = text.count(i)

print(result)