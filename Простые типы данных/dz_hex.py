# num = 255
# # result = 0
# num_test = num

# result = ''
# while num != 0:

#     a = num - (num//16)*16
#     if a == 10:
#         a = 'A'
#     elif a == 11:
#         a = 'B'
#     elif a == 12:
#         a = 'C'
#     elif a == 13:
#         a = 'D'
#     elif a == 14:
#         a = 'E'
#     elif a == 15:
#         a = 'F'
#     num = num//16
#     result = str(a) + result
# print(f'Шестнадцатеричное представление числа: {result}')
# print(f'Проверка результата: {hex(num_test)}')

# ИДЕАЛЬНОЕ РЕШЕНИЕ

num = 255
HEX = 16
hex_digits = "0123456789ABCDEF"

hex_num = ""
test_hex_num = hex(num)
print(num%16)
while num > 0:
    remainder = num % HEX
    hex_num = hex_digits[remainder] + hex_num
    num //= HEX

print("Шестнадцатеричное представление числа:", hex_num)
print("Проверка результата:", test_hex_num)
