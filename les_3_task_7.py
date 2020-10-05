# 7. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба минимальны), так и различаться.

import random

my_list = [random.randint(-5, 5) for i in range(10)]
print(my_list)

result = []

for i in range(2):
    min_value = my_list[0]
    for j in my_list:
        if j < min_value:
            min_value = j
    my_list.remove(min_value)
    result.append(min_value)

print(result)
