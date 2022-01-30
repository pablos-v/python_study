



def Fibo( n, a, b):
    if n <= 1:
        print(a + b)
    else:
        print(f"{a + b} {Fibo(n - 1, b, a + b)}")

Fibo(4, 0, 1)
