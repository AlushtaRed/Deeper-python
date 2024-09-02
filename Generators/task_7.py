# ✔ Создайте функцию-генератор.
# ✔ Функция генерирует N простых чисел,
# начиная с числа 2.
# ✔ Для проверки числа на простоту используйте
# правило: «число является простым, если делится
# нацело только на единицу и на себя».

def gen_n_simple(n):
    
    def simple_num():
        for i in range(2, 1000000):
            j = 1
            count = 0
            while j <= i:
                if i % j == 0:
                    count = count + 1
                j = j+1
            if count<3:
                yield i

    f = simple_num()
    for i in range(n):
        print(next(f))

gen_n_simple(100)

