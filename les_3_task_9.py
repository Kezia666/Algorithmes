# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.

import random

matrix = []
row_num = 5

for i in range(row_num):
    matrix.append([random.randint(-5, 5) for i in range(row_num)])
    print(matrix[i])

result = []

for num1 in range(row_num):
    min_value = matrix[0][num1]
    for num2 in range(row_num):
        value = matrix[num2][num1]
        if value < min_value:
            min_value = value
    result.append(min_value)

print()
print(result)
print()

max_value = result[0]
for number in result:
    if number > max_value:
        max_value = number

print(max_value)
