# Напишите функцию, которая сохраняет созданный в
# прошлом задании файл в формате CSV.
import json
import csv

def create_csv():
    with open('task_2v2.json', "r", encoding='utf-8') as js_f:
        res = json.load(js_f)
        keys = res[0].keys()
        lst = []
        lst.append(keys)
        for line in res:
            values = line.values()
            lst.append(values)
    with open('task_2v2.csv', "w", newline='', encoding='utf-8') as cs_f:
        writer = csv.writer(cs_f)
        writer.writerows(lst)

create_csv()