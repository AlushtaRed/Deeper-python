# ✔ Дорабатываем функции из предыдущих задач.
# ✔ Генерируйте файлы в указанную директорию — отдельный параметр функции.
# ✔ Отсутствие/наличие директории не должно вызывать ошибок в работе функции
# (добавьте проверки).
# ✔ Существующие файлы не должны удаляться/изменяться в случае совпадения имён.
import  os
from random import randbytes, sample, randint

def create_file(my_path, extention,  min_len=6, max_len=30, min_bytes=256, max_bytes=4096, count=5):
    for i in range(count):
        name = ''
        vowel = 'qeyuioa'
        consonant = 'wrtpsdfghjklzxcvbnm'
        for i in range(randint(min_len,max_len)):
            if i%2 != 0 and i > 0:
                name += vowel[randint(0,len(vowel)-1)]
            else:
                name += consonant[randint(0,len(vowel)-1)]
        if not os.path.isdir(my_path):
            os.mkdir(my_path)
        with open(f'{my_path}/{name}.{extention}', 'wb') as f:
                f.write(randbytes(randint(min_bytes,max_bytes)))

def extentions_and (ext_num,my_path):
    for i in ext_num:
        create_file(my_path, extention=i[0], count=i[1])

extentions_and([('txt', 3),('py',4)],'garbage')