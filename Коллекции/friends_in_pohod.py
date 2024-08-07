# ✔ Три друга взяли вещи в поход. Сформируйте
# словарь, где ключ — имя друга, а значение —
# кортеж вещей. Ответьте на вопросы:
# ✔ Какие вещи взяли все три друга
# ✔ Какие вещи уникальны, есть только у одного друга
# ✔ Какие вещи есть у всех друзей кроме одного
# и имя того, у кого данная вещь отсутствует
# ✔ Для решения используйте операции
# с множествами. Код должен расширяться
# на любое большее количество друзей.
hike = {'Игорь': {'Рюкзак', 'Нож', 'Спички','Вода'}, 'Витя': {'Рюкзак','Вода','Еда','Книга'}, 
        'Рома': {'Рюкзак','Еда','Журнал','Книга'}, 'Ира': {'Вино','Рюкзак'}}
result = hike['Витя']
# result = set()
for value in hike.values():
    result = result.intersection(value)
    # print(result)
if result == set():
    print('Нет вещей, которые взял каждый друг')
else:
    print(*result, ' взял каждый друг')

result = []
for value in hike.values():
    result += list(value)
    
# print(result)
for i in result:
    if result.count(i) == 1:
        print(i, ' взял только один из друзей')
        for key,value in hike.items():
            if i not in value:
                print(f'{key} не взял с собой {i}')
            

# print(result)