import random

number = random.randint(0, 100)
i = 0
# print(number)
while i < 10:
    i += 1
    user_number = int(input(f"Попытка №{i}. Введите число: "))
    if user_number == number:
        break
    elif number < user_number:
        print("Ваше число больше загаданного")
    else:
        print("Ваше число меньше загаданного")

print(f"Компьютер загадал число {number}!")
