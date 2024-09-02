# Напишите функцию, которая в бесконечном цикле
# запрашивает имя, личный идентификатор и уровень
# доступа (от 1 до 7).
# После каждого ввода добавляйте новую информацию в
# JSON файл.
# Пользователи группируются по уровню доступа.
# Идентификатор пользователя выступает ключём для имени.
# Убедитесь, что все идентификаторы уникальны независимо
# от уровня доступа.
# При перезапуске функции уже записанные в файл данные
# должны сохраняться.
import json
import os
lst = []
with open('task_2v2.json', "w", encoding='utf-8') as js_f:
    json.dump(lst, js_f)

def fun_dump_json():

    name = input('Имя:')
    user_id = input('ID:')
    level = input('Level:')

    with open('task_2v2.json', "r", encoding='utf-8') as f:
        res = json.load(f)
        print(res)

    my_dct = {
        "level": level,
        "id": user_id,
        "name": name,
    }

    with open('task_2v2.json', "w", encoding='utf-8') as js_f:
        res.append(my_dct)
        json.dump(res, js_f, indent=2, separators=(',', ':'),
                  ensure_ascii=False, sort_keys=True)
        
s = 'n'
while s != 'y':
    fun_dump_json()
    s = input('выход y/n :>')

