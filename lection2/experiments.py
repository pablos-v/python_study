
def main(n):
    fibo(n, 0, 1)
    nego_fibo(n, 0, 1)
    print(ls)                                  


def fibo(n, a, b):
    if n <= 2:
        return a + b
    else:
        ls.append(a + b)
        return fibo(n - 1, b, a + b)


def nego_fibo(n, a, b):
    if n <= 1:
        return b - a
    else:
        ls.insert(0, b - a)
        return nego_fibo(n - 1, b - a, a)


ls = [0, 1]
main(10)