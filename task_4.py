def func(n):
    if n == 0:
        return 0
    summa = 1
    number = 1
    while n > 1:
        number /= -2
        summa += number
        n -= 1
    return summa


print(f"Сумма = {func(int(input('Введите натуральное число: ')))}")
