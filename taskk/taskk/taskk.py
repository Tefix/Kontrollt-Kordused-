#1
while True:
    try:
        n = int(input("Введите число от 1 до 9: "))
        if 1 <= n <= 9:
            rabbit = [
                "  (\_/)",
                "  (o o)",
                "  / | \\",
            ]

            for i in rabbit:
                print((i + "  ") * n)
            break
        else:
            print("Число должно быть от 1 до 9!")
    except ValueError:
        print("Пожалуйста, введите целое число!")

#2
while True:
    try:
        L = int(input("Введите число: "))
        if L < 0:
            print("Введите неотрицательное число.")
        else:
            total = sum(range(L + 1))  
            print(f"Сумма чисел от 0 до {L} ровна: {total}")
    except ValueError:
        print("Ошибка! Введите целое число.")  

# #3
while True:
    import random
    randomnumber = random.randint(1, 100)

    print("Угадайте число от 1 до 100.")
    randomnum = int(input("Введите число: "))
    if randomnumber == randomnum:
        print("Вы угадали!")
    else:
        print("У вас осталось 9 попыток")

    for i in range(9):
        randomnum = int(input("Введите число: "))
        if randomnumber == randomnum:
            print("Вы угадали!")
            break
        else:
            print(f"У вас осталось {8 - i} попыток")

# #4
while True:
    num = input("Введите число: ")
    reversednum = ""

    for reverse in num:
        reversednum = reverse + reversednum

    print("Обратное число:", reversednum)
#     5
while True:
    try:
        n=(int(input("Введите число: ")))
        break
    except ValueError:
        print("Это не число. попробуйте еще раз")


summa = 0
tööd = 1
while n > 0:
    k = n % 10
    summa = summa + k
    n = n // 10
    tööd = tööd * k
print("Сумма чисел равна", summa)
print("Произведение числа равно", tööd)
