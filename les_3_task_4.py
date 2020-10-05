# 4. Определить, какое число в массиве встречается чаще всего.

import random

first_list = [random.randint(0, 5) for i in range(20)]
max_count = 1

for i, value in enumerate(first_list):
    if first_list.count(value) > max_count:
        max_count = first_list.count(value)
        max_value = value

print(first_list)
print(value)
