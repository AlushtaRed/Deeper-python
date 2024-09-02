import warnings

warnings.filterwarnings('ignore')

#При отправке кода на Выполнение раскомментируйте строку ниже, чтобы задать значения аргументов и вызвать функцию

#При отправке решения на Проверку закомментируйте эту строку обратно - система автоматически подставит разные значения аргументов и вызовет функцию для проверки

matrix = [[1]]

# Введите ваше решение ниже
def transpose(matrix):
    transposed_matrix =[]

    for i in zip(*matrix):
        transposed_matrix.append(list(i))
    return transposed_matrix




print(transpose(matrix)) 

