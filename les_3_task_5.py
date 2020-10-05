# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
# Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».
# Это два абсолютно разных значения.

import random

my_list = [random.randint(-5, 5) for i in range(10)]
negative = [i for i in my_list if i < 0]
max_value = negative[0]
for i in negative:
    if i > max_value:
        max_value = i
positions = [i for i, value in enumerate(my_list) if value == max_value]

print(my_list)
print(f"Значение: {max_value}, позиции: {positions}")
