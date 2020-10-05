def binary(num):
    s = ''
    while num > 0:
        s = f'{num % 2}{s}'
        num //= 2
    return s


# print(binary(255))
while True:
    number = int(input("Введите число: "))
    if number != 0:
        print(binary(number))
    else:
        break
