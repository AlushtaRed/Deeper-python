# В большой текстовой строке text подсчитать количество встречаемых слов и вернуть 10 самых частых. 
# Не учитывать знаки препинания и регистр символов.

# Слова разделяются пробелами. Такие слова как don t, it s, didn t итд 
# (после того, как убрали знак препинания апостроф) считать двумя словами.
# Цифры за слова не считаем.

# Отсортируйте по убыванию значения количества повторяющихся слов. 
# Слова выведите в обратном алфавитном порядке.

text = 'Hello world. Hello Python. 5 6 Hello again.'
new_text = text.lower()
new_text = new_text.replace('.', ' ')
new_text = new_text.replace(',', ' ')
new_text = new_text.replace("'", ' ')
new_text = new_text.replace('!', ' ')
new_text = new_text.replace('?', ' ')
new_text = new_text.replace('  ', ' ')
list_text = new_text.split()
result_list = []
for i in list_text:
    if i.isdigit():
        continue
    else:
        result_list.append((i,list_text.count(i)))

result_list = list(set(result_list))
result_list = sorted(result_list, key=  lambda x:(x[1], x[0]), reverse=True)
print(result_list)
