a = 5
b = 9
c = 5
text2 = ''
if a + b <= c:
    text = 'Треугольник не существует'
elif a+c <= b:
    text = 'Треугольник не существует'
elif c+b <= a:
    text = 'Треугольник не существует'
else:
    text = 'Треугольник существует'

    if a == b and b == c:
        text2 = 'Треугольник равносторонний'
    elif a == b or b == c or a == c:
        text2 = 'Треугольник равнобедренный'
    else:
        text2 = 'Треугольник разносторонний'
print(text)
if text2 != '':
    print(text2)
