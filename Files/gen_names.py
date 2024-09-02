# ✔ Напишите функцию, которая генерирует
# псевдоимена.
# ✔ Имя должно начинаться с заглавной буквы,
# состоять из 4-7 букв, среди которых
# обязательно должны быть гласные.
# ✔ Полученные имена сохраните в файл.
from random import randint

def name_generate():
    name = ''
    vowel = 'уеаоэяию'
    consonant = 'цкнгшзфвпрлджчсмтб' 
    for i in range(randint(4,7)):
        if i%2 != 0 and i > 0:
            name += vowel[randint(0,len(vowel)-1)]
        else:
            name += consonant[randint(0,len(vowel)-1)]
    name = name.title()
    print(name)

    with open('task_2.txt', 'a', encoding='utf-8') as f:
        f.write(f'{name}\n')


name_generate()
