year = int(input('Введите год для проверки: '))
if year%4 != 0:
    year = 'Год не високосный'
elif year%100 != 0:
    year = 'Год високосный'
elif year%100 == 0 and year%400 ==0:
    year = 'Год високосный'
else: year = 'Год не високосный'
print(year)
 