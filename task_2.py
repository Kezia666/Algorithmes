def func(number):
    odd, even = 0, 0
    while True:
        n = number % 10
        if n % 2 == 1:
            odd += 1
        else:
            even += 1
        if number >= 10:
            number //= 10
        else:
            break
    return f"Чётных чифр - {even}, нечетных цифр - {odd}."


print(func(int(input("Введите натуральное число: "))))
