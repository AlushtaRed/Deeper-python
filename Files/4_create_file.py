# ✔ Создайте функцию, которая создаёт файлы с указанным расширением.
# Функция принимает следующие параметры:
# ✔ расширение
# ✔ минимальная длина случайно сгенерированного имени, по умолчанию 6
# ✔ максимальная длина случайно сгенерированного имени, по умолчанию 30
# ✔ минимальное число случайных байт, записанных в файл, по умолчанию 256
# ✔ максимальное число случайных байт, записанных в файл, по умолчанию 4096
# ✔ количество файлов, по умолчанию 42
# ✔ Имя файла и его размер должны быть в рамках переданного диапазона.
from random import randbytes, sample, randint

def create_file(extention, min_len=6, max_len=30, min_bytes=256, max_bytes=4096, count=5):
    for i in range(count):
        name = ''
        vowel = 'qeyuioa'
        consonant = 'wrtpsdfghjklzxcvbnm'
        for i in range(randint(min_len,max_len)):
            if i%2 != 0 and i > 0:
                name += vowel[randint(0,len(vowel)-1)]
            else:
                name += consonant[randint(0,len(vowel)-1)]
        with open(f'{name}.{extention}', 'wb') as f:
            f.write(randbytes(randint(min_bytes,max_bytes)))

create_file(extention='txt')