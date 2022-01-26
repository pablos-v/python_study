import random


def generate_2D_int_list(m,n):
    return [[random.randint(-9, 9) for i in range(n)] for i in range(m)]


def enter_num(phrase):
    while True:
        try:
            num = int(input(phrase))
            return num
        except ValueError:
            print("Something is wrong, try one more time!")


def print_2D_list(ls):
    for i in ls:
        print(i)