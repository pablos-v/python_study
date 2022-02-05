

def main_s_1(ls):
    ls = [i for i in ls if ls.count(i) == 1]
    print(ls)


main_s_1([1, 2, 3, 5, 1, 5, 3, 10])

a = lambda ls:[i for i in ls if ls.count(i) == 1]
print(a([1, 2, 3, 5, 1, 5, 3, 10]))