# 11 Для натурального N создать список: 1, -3, 9, -27, 81 и т.д.

# def sequence_3_powered(N):
#     return [(-3)**i for i in range(N)]


# print(sequence_3_powered(5))

# 12 Для натурального N создать словарь индекс-значение, состоящий
# из элементов последовательности 3k + 1.

# Имеется ввиду Гипо́теза Ко́ллатца?

# def collatz_sequence(N):
#     dict = {}
#     while N != 1:
#         if N % 2 == 0:
#             dict[N] = N // 2
#         else:
#             dict[N] = N * 3 + 1
#         N = dict[N]
#     return dict

# print(collatz_sequence(6))

# правленная задача: Для натурального n создать словарь индекс-значение, состоящий 
# из элементов последовательности 3n + 1.
# Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

# def create_dict(n):
#     return dict({i : 3 * i + 1 for i in range(1, n + 1)})


# print(create_dict(6))

# 13 Пользователь задаёт две строки. Определить количество количество
# вхождений одной строки в другой.

# print(input("We will take a look at this string: ").count(input("And count how many times we met this string: ")))

# 14 Подсчитать сумму цифр в вещественном числе.

# def sum_dec_digits(a):
#     sum = 0
#     for i in str(a):
#         if i.isdecimal():
#             sum += int(i)
#     return sum


# print(sum_dec_digits(1.234))

# 15 Написать программу получающую набор произведений чисел от 1 до N.
# Пример: пусть N = 4, тогда [ 1, 2, 6, 24 ]

# def factorial_row(n):
#     ls = [x for x in range(1, n + 1)]
#     mult = 1
#     i = 0
#     while i < n:
#         ls[i] *= mult
#         mult = ls[i]
#         i += 1
#     return ls

# print(factorial_row(6))

# 16 Задать список из n чисел последовательности (1+1/n)**n и вывести на экран их сумму

# def sum_sequence(n):
#     ls = []
#     for i in range(1,n+1):
#         ls.append((1+1/i)**i)
#     return ls


# print(sum(sum_sequence(5)))

# 17 Задать список из N элементов, заполненных числами из [-N, N].
# Найти произведение элементов на указанных позициях. Позиции хранятся
# в файле file.txt в одной строке одно число

# from random import randint
# import my_box


# def create_list(N):
#     return [randint(-N, N) for i in range(N)]


# def multiply(list, elements):
#     result = 1
#     for i in range(len(list)):
#         if i in elements:
#             result *= list[i]
#     return result


# def main(N):
#     list = create_list(N)
#     elements = my_box.int_from_txt_to_list('file.txt')
#     print("Given list:", list)
#     print("Element indexes to multiply:", elements)
#     print("Multiplication result:", multiply(list, elements))


# main(10)

# 18 Реализовать алгоритм перемешивания списка.
# import random


# def mixed_list(ls):
#     for i in range(len(ls)):
#         temp = 0
#         position = random.randint(i, len(ls)-1)
#         temp = ls[i]
#         ls[i] = ls[position]
#         ls[position] = temp
#     return ls


# def main():
#     ls = [x for x in range(10)]
#     print(ls)
#     print(mixed_list(ls))


# main()

# 19 Реализовать алгоритм задания случайных чисел.
# Без использования встроенного генератора псевдослучайных чисел
# import time

# def random_int_of_time():
#     ls = []
#     s = str(time.time())
#     for i in s:
#         if i.isdecimal():
#             ls.append(int(i))
#     return sum(ls)%10

# for i in range(10):
#     print(random_int_of_time(), end = " ")
#     time.sleep(0.02)

# 20 Определить, присутствует ли в заданном списке строк, некоторое число

# def main():
#     ls = ['Given 1', 'list', 'of', '5', 'values']
#     print(is_num_in_list(ls, 1))


# def is_num_in_list(ls, num):
#     list = []
#     for s in ls:
#         for i in s:
#             if i.isdecimal():
#                 list.append(int(i))
#     return num in list


# main()

# 21 Определить, позицию второго вхождения строки в списке либо сообщить, что его нет.

# def main(s):
#     ls = ['Given 1', 'list', 'of', '5', '5', 'values', 'values', 'values']
#     find_str_in_list(ls, s)


# def find_str_in_list(ls, s):
#     count = []
#     for i in ls:
#         if i == s:
#             count.append(ls.index(i))
#     if len(count) >= 2:
#         print(f"We meet string '{s}' second time at position {count[1]} of given list.")
#     else:
#         print(f"We can`t see string '{s}' twice in given list.")


# main('values')

# 22 Найти сумму чисел списка стоящих на нечетной позиции

# from random import randint


# def main():
#     ls = random_list(6)
#     print(ls)
#     print(sum(i for i in ls[0:len(ls):2]))


# def random_list(n):
#     return [randint(-9, 9) for x in range(n)]


# main()

# 23 Найти произведение пар чисел в списке. Парой считаем первый и последний
# элемент, второй и предпоследний и т.д.
# Пример: [2, 3, 4, 5, 6] => [12, 15, 16]; [2, 3, 5, 6] => [12, 15]

# from random import randint


# def random_list(n):
#     return [randint(1, 9) for x in range(n)]


# def multiply_pairs_in_list(ls):
#     if len(ls) % 2 == 1:
#         return [ls[i] * ls[-1 - i] for i in range(len(ls) // 2 + 1)]
#     else:
#         return [ls[i] * ls[-1 - i] for i in range(len(ls) // 2)]


# def main():
#     ls = random_list(5)
#     print("Given list:", ls)
#     print("List of multiplied values:", multiply_pairs_in_list(ls))

# main()

# 24 В заданном списке вещественных чисел найдите разницу между максимальным и
# минимальным значением дробной части элементов. Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19
# from random import random


# def frac_parts_diff(ls):
#     ls_fract_parts = [round(i % 1, 2) for i in ls]
#     return round(max(ls_fract_parts) - min(ls_fract_parts), 2)


# def main():
#     ls = [round(random()*10, 2) for i in range(5)]
#     print(
#         f"In the given list: {ls}\nDifference between max and min fractial parts is: {frac_parts_diff(ls)}")


# main()

# 25 Написать программу преобразования десятичного числа в двоичное

# def dec_to_bin(n):
#     ls = ''
#     while n > 0:
#         ls += str(n % 2)
#         n //= 2
#     return ls[::-1]


# print(f"0b{dec_to_bin(4)}")

# 26 Дано число. Составить список чисел Фибоначчи, в том числе для отрицательных индексов

# def fibo(n):
#     ls = [0, 1]
#     for i in range(1, n - 1):
#         ls.append(ls[i] + ls[i - 1])
#     return ls


# def nega_fibo(n):
#     row = fibo(n)
#     for i in range(n-1):
#         row.insert(0, row[1] - row[0])
#     return row


# print(nega_fibo(6))



# 27 Строка содержит набор чисел. Показать большее и меньшее число



# 28 Найти корни квадратного уравнения Ax² + Bx + C = 0
#       Математикой
#       Используя дополнительные библиотеки*
# 29 Найти НОК двух чисел
# 30 Вычислить число  c заданной точностью d Пример: при d = 0.001,  = 3.141. 10-1d10-10

# 31 Составить список простых множителей натурального числа N
