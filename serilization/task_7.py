# Прочитайте созданный в прошлом задании csv файл без
# использования csv.DictReader.
# Распечатайте его как pickle строку.
import csv
import pickle

with open("new_csv.csv", "r", encoding="utf-8") as c:
    reader = csv.reader(c)
    data = pickle.dumps(list(reader))
    print(pickle.loads(data))