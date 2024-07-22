# Напишите функцию key_params, принимающую на вход только ключевые параметры и возвращающую словарь, 
# где ключ - значение переданного аргумента, а значение - имя аргумента.
# Если ключ не хешируем, используйте его строковое представление.
import typing
result_dict = {}
def key_params(**kwargs):

    for key,value in kwargs.items():
        if not isinstance(value, typing.Hashable):
            value = str(value)
            result_dict[value] = key
        else:
            result_dict[value] = key

    return result_dict

params = key_params(a=1, b='hello', c=[1, 2, 3], d={})
print(params)