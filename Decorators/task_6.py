# Доработайте прошлую задачу добавив декоратор wraps в
# каждый из декораторов.

from json import dump
from functools import wraps

def cache(num):
    def real_decor(func):
        @wraps(func)
        def wrapper(*args,**kwargs):
            count = 0
            for _ in range(num):
                res = func(args[0], args[1])
                count += 1
            return res, count
        return wrapper
    return real_decor

def decorator(func):
    my_dict = {}
    @wraps(func)
    def wrapper(*args,**kwargs):
        res = func(*args,**kwargs)
        file_name = f'{func.__name__}.json'
        my_dict['args'] = f'{args[0]},{args[1]}'
        for k,v in my_dict.items():
            my_dict[k] = v
        my_dict['res'] = res
        with open(file_name, 'a', encoding="utf-8") as js_f:
            dump(my_dict, js_f, indent=2)
        return res
    return wrapper

@cache(1)
@decorator
def guess_num(num,attempts):
    """исходная"""
    while attempts > 0:
        number = int(input('Введите число: '))
        if number == num:
            return 'угадали'
        attempts -= 1
    return 'не угадали'

print(guess_num(45,5))
print(guess_num.__name__)
help(guess_num)