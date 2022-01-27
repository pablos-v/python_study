# 15 Написать программу получающую набор произведений чисел от 1 до N.
# Пример: пусть N = 4, тогда [ 1, 2, 6, 24 ]

def factorial_row(n):
    ls = [x for x in range(1, n + 1)]
    mult = 1
    i = 0
    while i < n:
        ls[i] *= mult
        mult = ls[i]
        i += 1
    return ls

print(factorial_row(6))

