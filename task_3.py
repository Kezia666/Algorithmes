def func(number):
    if number < 10:
        return number
    return f"{number % 10}{func(number // 10)}"


print(func(int(input("Введите натуральное число: "))))
