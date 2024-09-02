# Вспоминаем задачу 3 из прошлого семинара. Мы сформировали
# текстовый файл с псевдо именами и произведением чисел.
# Напишите функцию, которая создаёт из созданного ранее
# файла новый с данными в формате JSON.
# Имена пишите с большой буквы.
# Каждую пару сохраняйте с новой строки.

import json

f_name = 'result.txt'
j_name = 'result_json.txt'
with open(f_name, 'r') as f, open(j_name, 'w') as j:
    mydict = {}
    for line in f:
        key, value = line.split(':')
        print(key, value)
        mydict[key.title()] = float(value)
    json.dump(mydict, j, separators=(',\n', ':'),ensure_ascii=False)