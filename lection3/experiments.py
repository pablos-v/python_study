import my_box


def main():
    ls = my_box.enter_list_int_nums(2)
    while len(ls) > 1:
        a, b = ls.pop(), ls.pop()
        min_common_divisor = int(a * b / find_divisor(a, b))
        ls.append(min_common_divisor)
    print(ls[0])


def find_divisor(a, b):
    if a < b:
        a, b = b, a
    while a % b:
        temp = b
        b = a % b
        a = temp
    return b


main()
