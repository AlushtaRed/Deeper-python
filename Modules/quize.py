# � Создайте модуль с функцией внутри.
# � Функция получает на вход загадку, список с возможными
# вариантами отгадок и количество попыток на угадывание.
# � Программа возвращает номер попытки, с которой была
# отгадана загадка или ноль, если попытки исчерпаны.

def my_quize(question: str, answer: list, count: int):
    
    temp_cnt = 1
    answer = list(map(lambda x: x.lower(), answer))
    while temp_cnt <= count:
        user_string = input(question).lower()
        if user_string in answer:
            return temp_cnt
        temp_cnt += 1
    return 0