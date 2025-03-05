# while True:
#     try:
#         n = int(input("Введите число от 1 до 9: "))
#         if 1 <= n <= 9:
#             rabbit = [
#                 "  (\_/)",
#                 "  (o o)",
#                 "  / | \\",
#             ]
#
#             for line in rabbit:
#                 print((line + "  ") * n)
#             break
#         else:
#             print("Число должно быть от 1 до 9!")
#     except ValueError:
#         print("Пожалуйста, введите целое число!")

#2
# try:
#     L = int(input("Введите число: "))
#     if L < 0:
#         print("Введите неотрицательное число.")
#     else:
#         total = sum(range(L + 1))  #
#         print(f"Сумма чисел от 0 до {L} ровна: {total}")
# except ValueError:
#     print("Ошибка! Введите целое число.")
#
#3
# import random
# randomnumber = random.randint(1, 100)
#
# print("Угадайте число от 1 до 100.")
# randomnum = int(input("Введите число: "))
# if randomnumber == randomnum:
#     print("Вы угадали!")
# else:
#     print("У вас осталось 9 попыток")
#
# for i in range(9):
#     randomnum = int(input("Введите число: "))
#     if randomnumber == randomnum:
#         print("Вы угадали!")
#         break
#     else:
#         print(f"У вас осталось {8 - i} попыток")

#4



