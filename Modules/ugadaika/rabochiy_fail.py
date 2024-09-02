from random import randint as r
from sys import argv

def my_func(min_=0, max_=100, count=10, *_):
    number = r(min_,max_)
    cnt = 1
    while cnt < count:
        result = int(input('Угадайте число: '))
        
        if result == number:
            print(f'Вы угадали число с {cnt} попытки')
            break
        elif result< number:
            print('Больше')
        else:
            print('Меньше')
        cnt += 1
    else:
        print(f'Вы не угадали чило {number} за {count} раз')

my_func(1,100,10)

# if __name__ == '__main':
#     min_, max_, count = [int(el) for el in argv[1:] ]