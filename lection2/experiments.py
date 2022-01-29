



from random import randint


def main():
    ls = random_list(6)
    print(ls)
    print(sum(i for i in ls[0:len(ls):2]))


def random_list(n):
    return [randint(-9, 9) for x in range(n)]


main()
