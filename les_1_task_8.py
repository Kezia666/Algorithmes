# 8. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

a = int(input("Введите a: "))
b = int(input("Введите b: "))
c = int(input("Введите c: "))
if a > b:
    if a < c:
        m = a
    else:
        if b > c:
            m = b
        else:
            m = c
else:
    if b > c:
        if a > c:
            m = a
        else:
            m = c
    else:
        m = b
print(f"Среднее число: {m}")