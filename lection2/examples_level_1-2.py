# 1 По двум заданным числам проверить является ли одно квадратом второго

# def is_square(a, b):
#     if a < b:
#         return is_square(b, a)
#     else:
#         return a == b * b


# print(is_square(4,16))

# 2 Найти максимальное из пяти чисел

# ls = [1,2,5,3,4]
# print(max(ls))

# 3 Вывести на экран числа от -N до N

# def printer(n):
#     ls = [x for x in range(-n, n+1)]
#     for i in ls:
#         print(i, end = " ")


# def prnt(n):
#      print([x for x in range(-n, n+1)])


# printer(5)
# prnt(6)

# 4 Показать первую цифру дробной части числа

# def find_1_fraction_part(a):
#     return int(a * 10) % 10


# print(find_1_fraction_part(1.456))

# 5 Дано число. Проверить кратно ли оно 5 и 10 или 15 но не 30

# def is_multiple(n):
#     return n % 5 == 0 and n % 10 == 0 or n % 15 == 0 and not n % 30 == 0


# print(is_multiple(45))

# 6 Дано число обозначающее день недели. Вывести его название и указать является ли он выходным.

# solved in lection1

# 7 Проверить истинность утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат

# solved in lection1

# 8 Сообщить в какой четверти координатной плоскости или на какой оси находится точка с координатами Х и У

# solved in lection1

# 9 Указав номер четверти прямоугольной системы координат, показать допустимые значения координат для точек этой четверти

# solved in lection1

# 10 Найти расстояние между двумя точками пространства

# solved in lection1