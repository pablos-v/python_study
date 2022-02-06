# Задачи 32, 33, 35, 36, 38, 39, 42, 43 в приоритете т к они попроще
# Задачи 34, 37, 40,  41, 44  посложнее, можно их оставить на потом

# 32 Дана последовательность чисел. Получить список неповторяющихся элементов исходной последовательности
# Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [1, 2, 3, 5, 10]

# li = [1, 2, 3, 2, 3, 4, 3, 4, 5]
# res = list(set(li))
# print(res)

# 33 Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# *Пример: k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

# import random


# def el(li, k, l):
#     res_list = ''
#     for m in range(0, l):
#         if k == 1:
#             res_list += (f'{li[m]}x + ')
#         elif k == 0:
#             res_list += (f'{li[m]} = 0')
#         else:
#             res_list += (f'{li[m]}x^{k} + ')
#         k -= 1
#     return res_list

# def main(k):
#     li = [random.randint(0,100) for i in range(k + 1)]
#     with open ("33.txt", 'w') as file:
#         file.write(el(li, 3, len(li)))

# main(3)

# 34 Даны два файла в каждом из которых находится запись многочлена.
# Сформировать файл содержащий сумму многочленов.


# 35 В файле находится N натуральных чисел, записанных через пробел. Среди чисел не хватает одного,
# чтобы выполнялось условие A[i] - 1 = A[i-1]. Найти его.

# def main():
#     with open('35.txt') as file:
#         # A = [int(x) for x in file.read().split()]
#         A = list(map(int, file.read().split()))

#     print(finder(A))


# def finder(A):
#     for i in range(1, len(A)):
#         if not A[i] - 1 == A[i-1]:
#             return A[i] - 1


# main()

# 36 Дан список чисел. Выделить среди них числа, удовлетворяющие условию:
# следующее больше предыдущего.
# Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.
# Порядок элементов менять нельзя

# def compare(ls):
#     lst = [ls[0]]
#     for i in ls:
#         if i > lst[-1]:
#             lst.append(i)
#     return lst


# li = [1, 5, 2, 3, 4, 6, 1, 7]
# print(compare(li))

# 37 Дан список чисел. Выделить среди них максимальное количество чисел,
# удовлетворяющих условию предыдущей задачи.
# Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3, 4, 6, 7]

# def compare(ls):
#     res = []
#     for i in range(1, len(ls)-1):
#         temp = [ls[0]]
#         for e in range(i, len(ls)):
#             if ls[e] > temp[-1]:
#                 temp.append(ls[e])
#         res.append(temp)
#     return res


# def find_longest(final):
#     for k in final:
#         if len(k) == max(len(i) for i in final):
#             return final[final.index(k)]


# def main(given_list):
#     longest = find_longest(compare(given_list))
#     print(longest)


# main([1, 5, 2, 3, 4, 6, 1, 7])

# 38 Напишите программу, удаляющую из текста все слова содержащие "абв".

# def delete_phrase(s):
#     start_list = list(s.split())
#     filtered_list = list(filter(lambda string: not 'абв' in string, start_list))
#     return ' '.join(filtered_list)

# def main(s):
#     res = delete_phrase(s)
#     print(res)

# main('абва авба быва беба глабвас')

# 39 Помните игру с конфетами из модуля "Математика и Информатика"?
# Создайте такую игру для игры человек против человека
#   a Добавьте игру против бота
#   b Подумайте как наделить бота "интеллектом"

#  суть игры: на столе 21 спичка, за ход можно взять от 1 до 4 спичек
# побеждает тот, кто забрал последнюю
import my_box


def main():
    print('There are 21 matches on the table, you can take from 1 to 4 matches per turn.\nLast hand wins.')
    if game_type() == 1:
        play_bot()
    else:
        play_friend()
    main() if play_again() else exit()


def game_type():
    while True:
        players = my_box.enter_num(
            'There is two game options:\n1 - play with bot.\n2 - play with your friend.\nChoose option: ')
        if 3 > players > 0:
            return players


def play_again():
    return input('If you want play again, type "y", or anything else to exit.') == 'y'

def play_bot():
    

def play_friend():


# 40 Вы когда-нибудь играли в игру "Крестики-нолики"? Попробуйте создать её.


# 41 Написать программу вычисления арифметического выражения заданного строкой.
# Используются операции +,-,/,*. приоритет операций стандартный.
# Пример: 2+2 => 4; 1+2*3 => 7; 1-2*3 => -5;
#   a Добавить возможность использования скобок, меняющих приоритет операций.
#     Пример: 1+2*3 => 7; (1+2)*3 => 9;


# 42 Реализовать RLE (https://en.wikipedia.org/wiki/Run-length_encoding) алгоритм.
# реализовать модуль сжатия и восстановления данных.
#   a входные и выходные данные хранятся в отдельных файлах


# 43 Дана последовательность чисел. Получить список уникальных элементов заданной
# последовательности. Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]

# def main(ls):
#     res = find_uniq_nums(ls)
#     print(res)


# def find_uniq_nums(ls):
#     all_nums = list(set(ls))  # form list of all numbers without repeats
#     for i in all_nums:  # leave only repeating nums in ls
#         ls.remove(i)
#     return list(set(ls) ^ set(all_nums))


# main([1, 2, 3, 5, 1, 5, 3, 10])

# simplified_0

# def main_s(lst):
#     res = [i for i in lst if i not in lst[lst.index(i)+1:]]
#     print(res)


# main_s([1, 2, 3, 5, 1, 5, 3, 10])

# simplified_1

# def main_s_1(ls):
#     ls = [i for i in ls if ls.count(i) == 1]
#     print(ls)


# main_s_1([1, 2, 3, 5, 1, 5, 3, 10])

# simplified_2

# a = lambda ls:[i for i in ls if ls.count(i) == 1]
# print(a([1, 2, 3, 5, 1, 5, 3, 10]))

# 44 Секретная задача
