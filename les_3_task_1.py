# 1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
# Примечание: 8 разных ответов.

my_list = [i for i in range(2, 100)]

print(my_list)

for i in range(2, 10):
    count = 0
    for j in my_list:
        if j % i == 0:
            count += 1
    print(count)
