# ## Почувствуй себя интерном*
#  0. Вывести квадрат числа
# n = 3
# print(n**2)

#  1. По двум заданным числам проверять является ли первое квадратом второго
# a=3
# b=9
# print(b==a*a)

#  2. Даны два числа. Показать большее и меньшее число
# a = 3
# b = 4

# def max_min(a, b):
#     if a > b:
#         print(f"Большее число {a}, меньшее число {b}")
#     else:
#         print(f"Большее число {b}, меньшее число {a}")

# max_min(a, b)

#  3. По заданному номеру дня недели вывести его название

# week_dict = {
#     1: 'Monday',
#     2: 'Tuesday',
#     3: 'Wednesday',
#     4: 'Thursday',
#     5: 'Friday',
#     6: 'Saturday',
#     7: 'Sunday'
# }

# n=int(input("Enter day number:"))

# print(f"It is {week_dict[n]}")

#  4. Найти максимальное из трех чисел

# Без ввода чисел

# Просто

# print(max(22,55,76))

# Итеративно

# def find_max(r,t,y):
#     max = r
#     if t > max:
#         max = t
#     elif y > max:
#         max = y
#     return max
# print(find_max(3,55,67))

# Списком

# list_of_nums = [5, 66, 9]
# print(max(list_of_nums))

# Со вводом чисел, любое количество чисел

# def compare_nums(n):
#     list = []
#     for i in range(n):
#         list.append(input("Enter a number to compare: "))
#     return list

# print(max(compare_nums(3)))

#  5. Написать программу вычисления значения функции y = f(a)

# import math

# def some_func(degrees):
#     return round(math.sin(math.pi*degrees/180.0), 2)

# a = 30
# print(some_func(a))

#  6. Выяснить является ли число чётным

# def even_odd():
#     num = int(input("Enter number: "))
#     if num % 2 == 0:
#         return "even"
#     return "odd"

# print(even_odd())

# shortly

# num = int(input("Enter number: "))
# print("even" if num % 2 == 0 else "odd")

#  7. Показать числа от -N до N

# Veriant 1
# def show_nums(N):
#     list = []
#     for i in range(-N, N+1):
#         list.append(i)
#     return list

# print(show_nums(5))

# Veriant 2
# def show_nums(N):
#     for i in range(-N, N+1):
#         print(i, end=" ")

# show_nums(4)

#  8. Показать четные числа от 1 до N

# def print_even(n):
#     for i in range(1, n+1):
#         if i % 2 == 0:
#             print(i)

# print_even(50)

#  9. Показать последнюю цифру трёхзначного числа

# def print_last_of_three(n):
#     print(n % 10)

# print_last_of_three(783)

# 10. Показать вторую цифру трёхзначного числа

# def print_two_of_three(n):
#     print((n//10) % 10)

# print_two_of_three(783)

# 11. Дано число из отрезка [10, 99]. Показать наибольшую цифру числа

# import random

# def max_digit(a):
#     print(f"In the number {a} maximal digit is {a//10 if a % 10 < a//10 else a % 10}")

# max_digit(random.randint(10, 99))

# def max_digit_via_str(a):
#     a = str(a)
#     print(f"In the number {a} maximal digit is {max(a)}")

# max_digit_via_str(random.randint(10, 99))

# 12. Удалить вторую цифру трёхзначного числа



# 13. Выяснить, кратно ли число заданному, если нет, вывести остаток.
# 14. Найти третью цифру числа или сообщить, что её нет

# ## Почувствуй себя джуном*
# 15. Дано число. Проверить кратно ли оно 7 и 23
# 16. Дано число обозначающее день недели. Выяснить является номер дня недели выходным
# 17. По двум заданным числам проверять является ли одно квадратом другого
# 18. Проверить истинность утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z

# def func(x, y, z):
#     return not(x and y and z) == (not x or not y or not z)

# def print_bool():
#     for u in range(0, 2):
#         for j in range(0, 2):
#             for i in range(0, 2):
#                 print(func(u, j, i))

# print_bool()

# 19. Определить номер четверти плоскости, в которой находится точка с координатами Х и У, причем X ≠ 0 и Y ≠ 0

# from random import *
# x=0
# y=0
# while x == 0 and y ==0:
#     x = randint(-10, 10)
#     y = randint(-10, 10)

# def f(x, y):
#     if x > 0 and y > 0:
#         return 1
#     elif x > 0 and y < 0:
#         return 2
#     elif x < 0 and y > 0:
#         return 3
#     else:
#         return 4

# print(f"{x}, {y}, четверть {f(x,y)}")

# 20. Задать номер четверти, показать диапазоны для возможных координат
# 21. Программа проверяет пятизначное число на палиндромом.

# n = 54345

# def IsPalindrom(n):
#     n = str(n)
#     return n[0]==n[4] and n[1]==n[3]
# print(IsPalindrom(n))

# 22. Найти расстояние между точками в пространстве 2D/3D

# ## Почувствуй себя мидлом*
# 23. Показать таблицу квадратов чисел от 1 до N

# def enter_num(phrase):
#     while True:
#         try:
#             n = int(input(phrase))
#             if n > 0:
#                 return n
#         except ValueError:
#             print("Something is wrong, try one more time!")

# def print_it(r):
#     for i in range(1, r+1):
#         print(i**2)

# print_it(enter_num("Enter number N: "))

# 24. Найти кубы чисел от 1 до N
# 25. Найти сумму чисел от 1 до А
# 26. Возведите число А в натуральную степень B используя цикл
# 27. Определить количество цифр в числе
# 28. Подсчитать сумму цифр в числе
# 29. Написать программу вычисления произведения чисел от 1 до N
# 30. Показать кубы чисел, заканчивающихся на четную цифру
