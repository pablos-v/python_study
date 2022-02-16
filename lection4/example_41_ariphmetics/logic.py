op = '+-*/'

def solve(str):
    if len(str) == 1:
        return str
    for i in range(len(str)-1, -1):
        if '+' or '-' or '*' or '/' in str[i:]:
            if str[i] in op:
                return calculate(str[i], int(solve(str[:i])), int(str[i+1]) )
            else:
                continue


def calculate(operator, a, b):
    return {
        '+': lambda: a + b,
        '-': lambda: a - b,
        '*': lambda: a * b,
        '/': lambda: a / b,
    }.get(operator, lambda: 'Not a valid operation')()