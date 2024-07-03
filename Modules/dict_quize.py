# � Добавьте в модуль с загадками функцию, которая хранит
# словарь списков.
# � Ключ словаря - загадка, значение - список с отгадками.
# � Функция в цикле вызывает загадывающую функцию, чтобы
# передать ей все свои загадки.
import random



def quize_gemnerator():
    dict_quize = {'зимой и летом одним цветом  ': ['елка', 'ель','елочка'],
                  'висит груша - нельзя скушать': ['лампочка','лампа',''], 
                  'не лает, не кусает, а в дом не пускает': ['замок','замочек']}
    while dict_quize:
        key = random.choice(list(dict_quize))    
        yield key , dict_quize.pop(key)

def my_quize(count: int):
    result = []
    
    for quize in quize_gemnerator():
        riddle, answer = quize
        temp_cnt = 1
        answer = list(map(lambda x: x.lower(), answer))
        while temp_cnt <= count:
            user_string = input(riddle + ': ').lower()
            if user_string in answer:
                result.append(temp_cnt)
                break
            temp_cnt += 1
        else:
            result.append(0)
            
    return result