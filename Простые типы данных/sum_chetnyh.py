# Задание №5
# Работа в консоли в режиме интерпретатора Python.
# Посчитайте сумму чётных элементов от 1 до n исключая кратные e.
# Используйте while и if.
# Попробуйте разные значения e и n

e = 4
print(e)
# print (type(e))
n = 10
sum = 0
i = 1 
while i <= n:
    if i%2 == 0 and i%e != 0:
        sum += i
    i += 1
print(sum)



        



    
