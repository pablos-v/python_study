# ## Почувствуй себя сеньором*
# 31. Задать массив из 8 элементов и вывести их на экран
# from array import *

# arr = array('i',[1,2,3,4,5,6,7,8])

# ls = list(range(8))
# arr2 = array('i')
# arr2.fromlist(ls)

# print (arr2)
# print (arr)

# 32. Задать массив из 8 элементов, заполненных нулями и единицами вывести их на экран
# from array import *
# from random import *

# ls = []
# for i in range(8):
#     ls.append(randint(0,1))
# arr = array('i')
# arr.fromlist(ls)

# print(arr)

# 33. Задать массив из 12 элементов, заполненных числами из [-9,9].
# Найти сумму положительных/отрицательных элементов массива

# from array import *
# from random import *

# def generate_array():
#     ls = []
#     for i in range(12):
#         ls.append(randint(-9,9))
#     arr = array('i')
#     arr.fromlist(ls)
#     return arr

# def counter(arr):
#     ls = [0,0]
#     for i in arr:
#         if i > 0:
#             ls[0] += i
#         else:
#             ls[1] +=i
#     return ls

# def main():
#     arr = generate_array()
#     print(arr)
#     ls = counter(arr)
#     print(f"Summ of positive numbers is {ls[0]}, summ of negative numbers is {ls[1]}")

# main()

# 34. Написать программу замену элементов массива на противоположные

# from array import *
# from random import *

# def generate_array(n):
#     ls = []
#     for i in range(n):
#         ls.append(randint(-9, 9))
#     arr = array('i')
#     arr.fromlist(ls)
#     print(arr)
#     return arr

# def change_1(arr):
#     i = 0
#     while i < len(arr):
#         arr[i] *= -1
#         i += 1
#     return arr

# print(change_1(generate_array(5)))

# 35. Определить, присутствует ли в заданном массиве, некоторое число

# from array import *
# from random import *

# def generate_array(n):
#     ls = []
#     for i in range(n):
#         ls.append(randint(-9, 9))
#     arr = array('i')
#     arr.fromlist(ls)
#     return arr

# def is_there_a_number(x, arr):
#     return "True" if x in arr else "False"

# def main():
#     arr = generate_array(15)
#     print(arr)
#     print(is_there_a_number(5, arr))

# main()

# 36. Задать массив, заполнить случайными положительными трёхзначными числами.
# Показать количество нечетных\четных чисел

# from array import *
# from random import *

# def generate_array(n):
#     ls = []
#     for i in range(n):
#         ls.append(randint(100,999))
#     arr = array('i')
#     arr.fromlist(ls)
#     return arr

# def num_of_even_odd(arr):
#     ls = [0,0]
#     for i in arr:
#         if i%2==0:
#             ls[0]+=1
#         else:
#             ls[1]+=1
#     return ls

# def main():
#     arr = generate_array(8)
#     ls = num_of_even_odd(arr)
#     print(arr)
#     print(f"There is {ls[0]} even and {ls[1]} odd numbers in given array.")

# main()

# 37. В одномерном массиве из 123 чисел найти количество элементов из отрезка [10,99]

# from array import *
# from random import *

# def generate_array(n):
#     ls = []
#     for i in range(n):
#         ls.append(randint(0,200))
#     arr = array('i')
#     arr.fromlist(ls)
#     return arr

# def number_of_objects(arr):
#     q = 0
#     for i in arr:
#         if i in range(10,100):
#             q+=1
#     return q

# print(number_of_objects(generate_array(123)))

# 38. Найти сумму чисел одномерного массива стоящих на нечетной позиции

# from array import *
# from random import *

# def generate_array(n):
#     ls = []
#     for i in range(n):
#         ls.append(randint(-9,9))
#     arr = array('i')
#     arr.fromlist(ls)
#     return arr

# def sum_of_odd_positions(arr):
#     sum = 0
#     for i in range(0, len(arr), 2):
#         sum += arr[i]
#     return sum

# def main():
#     arr = generate_array(5)
#     print(arr)
#     print(sum_of_odd_positions(arr))

# main()

# 39. Найти произведение пар чисел в одномерном массиве.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# from array import *
# from random import *

# def generate_array(n):
#     ls = []
#     for i in range(n):
#         ls.append(randint(-9, 9))
#     arr = array('i')
#     arr.fromlist(ls)
#     return arr

# def count_pairs(arr):
#     ls = []
#     i = 0
#     y = len(arr)-1
#     while i < y/2:
#         ls.append(arr[i] * arr[y-i])
#         i += 1
#     return ls

# def main():
#     arr = generate_array(6)
#     print(arr)
#     print(count_pairs(arr))

# main()

# 40. В Указанном массиве вещественных чисел найдите разницу
# между максимальным и минимальным элементом

# from array import *
# from random import *

# def generate_array(n):
#     arr = array('i')
#     for i in range(n):
#         arr.append(randint(-9,9))
#     return arr

# def diff_max_min(arr):
#     return max(arr)-min(arr)

# def main():
#     arr = generate_array(5)
#     print(arr)
#     print(diff_max_min(arr))

# main()

# ## Почувствуй себя лидом*
# 41. Выяснить являются ли три числа сторонами треугольника
# В треугольнике сумма длин двух любых сторон больше длины третьей стороны

# def enter_num(phrase):
#     while True:
#         triangle = input(phrase).split(",")
#         if len(triangle) == 3:
#             try:
#                 for x in triangle:
#                     triangle[triangle.index(x)] = float(x)
#                 return triangle
#             except ValueError:
#                 print("Something is wrong, try one more time!")

# def is_triangle(t):
#     return t[0]+t[1] > t[2] and t[0]+t[2] > t[1] and t[1]+t[2] > t[0]

# print(is_triangle(enter_num("Type in sides of tiangle values, sparate commas: ")))

# 42. Определить сколько чисел больше 0 введено с клавиатуры

# def enter_num(phrase):
#     while True:
#         nums = input(phrase).split(",")
#         try:
#             for x in nums:
#                 nums[nums.index(x)] = float(x)
#             return nums
#         except ValueError:
#             print("Something is wrong, try one more time!")

# def count_positive_numbers(ls):
#     count = 0
#     for i in ls:
#         if i > 0:
#             count+=1
#     return count

# def main():
#     v = count_positive_numbers(enter_num("Enter numbers you want to check, separate commas: "))
#     print(f"You have entered {v} positive numbers")

# main()

# Optimized
# def enter_num_and_count(phrase):
#     while True:
#         nums = input(phrase).split(",")
#         count = 0
#         try:
#             for x in nums:
#                 if float(x) > 0:
#                     count += 1
#             return count
#         except ValueError:
#             print("Something is wrong, try one more time!")

# def main():
#     v = enter_num_and_count("Enter numbers you want to check, separate commas: ")
#     print(f"Positive numbers entered: {v} ")

# main()

# 43. Написать программу преобразования десятичного числа в двоичное

# print(bin(5))

# 44. Найти точку пересечения двух прямых заданных уравнением y = k1 * x + b1, y = k2 * x + b2, b1 k1 и b2 и k2 заданы

# def lines_cross_point(b1, k1, b2, k2):
#     x = round((b2 - b1) / (k1 - k2), 2)
#     y = round(k1 * x + b1, 2)
#     return x, y

# def main():
#     k1, b1, k2, b2 = 1, -3, -1, 2
#     if (k1 == k2 and b1 != b2): return "Parallel"
#     elif (k1 == k2 and b1 == b2): return "Match up"
#     else: return print(f"Cross point coordinates: {lines_cross_point(1,-3,-1,2)}")

# main()

# 45. Показать числа Фибоначчи



# 46. Написать программу масштабирования фигуры
# ```
# Тут для тех кто далеко улетел, чтобы задавались вершины фигуры списком (одной строкой)
# например: "(0,0) (2,0) (2,2) (0,2)"
# коэффициент масштабирования k задавался отдельно - 2 или 4 или 0.5
# В результате показать координаты, которые получатся.
# при k = 2 получаем "(0,0) (4,0) (4,4) (0,4)"
# ```
# 47. Написать программу копирования массива
