# � Добавьте в модуль с загадками функцию, которая
# принимает на вход строку (текст загадки) и число (номер
# попытки, с которой она угадана).
# � Функция формирует словарь с информацией о результатах
# отгадывания.
# � Для хранения используйте защищённый словарь уровня
# модуля.
# � Отдельно напишите функцию, которая выводит результаты
# угадывания из защищённого словаря в удобном для чтения
# виде.
# � Для формирования результатов используйте генераторное
# выражение.
import random

_results = {}

def quize_gemnerator():
    dict_quize = {'зимой и летом одним цветом': ['елка', 'ель','елочка'],
                  'висит груша - нельзя скушать': ['лампочка','лампа',''], 
                  'не лает, не кусает, а в дом не пускает': ['замок','замочек']}
    while dict_quize:
        key = random.choice(list(dict_quize))    
        yield key , dict_quize.pop(key)

def my_quize(count: int):
    global _results
    for quize in quize_gemnerator():
        riddle, answer = quize
        temp_cnt = 1
        answer = list(map(lambda x: x.lower(), answer))
        while temp_cnt <= count:
            user_string = input(riddle + ': ').lower()
            if user_string in answer:
                _results[riddle] = temp_cnt
                break
            temp_cnt += 1
        else:
            _results[riddle] = 0
            
def show_results():
    global _results
    result = ['Результаты: ']
    max_len = len(max(list(_results), key=len)) +2
    for riddle, count in _results.items():
        riddle += ': '
        result.append(f'{riddle:<{max_len}}отгадана с {count} попытки')
    return '\n'.join(result)