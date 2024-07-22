# Напишите функцию для транспонирования матрицы transposed_matrix, 
# принимает в аргументы matrix, и возвращает транспонированную матрицу.

# [[1, 4, 7], 
#  [2, 5, 8], 
#  [3, 6, 9]]

# matrix = [[1, 2, 3],
#          [4, 5, 6], 
#          [7, 8, 9]]
def transpose(matrix):
    transposed_matrix =  [[0 for i in range (len(matrix))] for j in range (len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            transposed_matrix[i][j] = matrix[j][i]
            # print(i,j)
    return transposed_matrix


# print(matrix)
# print(transpose([[1, 2, 3],
#          [4, 5, 6], 
#          [7, 8, 9]]))

print(transpose(matrix = [[1, 2], [3, 4]]))
# transposed_matrix=list(zip(matrix[0],matrix[1],matrix[2]))
# print(transposed_matrix)