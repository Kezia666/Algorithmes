# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

my_list = [random.randint(0, 50) for i in range(8)]
min_value = min(my_list)
max_value = max(my_list)
for i, value in enumerate(my_list):
    if value == min_value

print(my_list)
print(min_value, max_value)