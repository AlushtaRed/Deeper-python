import fractions

frac1 = "1/2"
frac2 = "1/3"
a_1 = int(frac1[0])
b_1 = int(frac1[2])
a_2 = int(frac2[0])
b_2 = int(frac2[2])
a_3 = (a_1*b_2)+(a_2*b_1)
b_3 = b_1*b_2
print('Сумма дробей: ', a_3,'/',b_3, sep='')
print('Произведение дробей: ', a_1*a_2,'/',b_1*b_2, sep='')
f1=fractions.Fraction(a_1, b_1)
f2=fractions.Fraction(a_2,b_2)
print(f'Сумма дробей: {f1+f2}')
print(f'Произведение дробей: {f1*f2}')

# ИДЕАЛЬНОЕ РЕШЕНИЕ

from fractions import Fraction
#frac1 = '2/5'
#frac2 = '3/5'

# Разбиваем строки на числитель и знаменатель без использования map
numerator1_str, denominator1_str = frac1.split('/')
numerator2_str, denominator2_str = frac2.split('/')

# Преобразуем строки в целые числа
numerator1 = int(numerator1_str)
denominator1 = int(denominator1_str)
numerator2 = int(numerator2_str)
denominator2 = int(denominator2_str)

common_denominator = denominator1 * denominator2

new_numerator1 = numerator1 * denominator2
new_numerator2 = numerator2 * denominator1

summation_numerator = new_numerator1 + new_numerator2
multiplication_numerator = numerator1 * numerator2

print(f"Сумма дробей: {summation_numerator}/{common_denominator}")
print(f"Произведение дробей: {multiplication_numerator}/{common_denominator}")

# Преобразуем введенные строки в объекты Fraction
fraction1 = Fraction(frac1)
fraction2 = Fraction(frac2)

# Вычисляем сумму и произведение дробей
summation = fraction1 + fraction2
multiplication = fraction1 * fraction2

print(f"Сумма дробей: {summation}")
print(f"Произведение дробей: {multiplication}")