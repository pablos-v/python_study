def solve(str):
    for i in range(len(str)):
        if str[i] == '+':
            res = int(str[:i]) + int(str[i+1:])
        if str[i] == '-':
            res = int(str[:i]) - int(str[i+1:])
        if str[i] == '*':
            res = int(str[:i]) * int(str[i+1:])
        if str[i] == '/':
            res = int(str[:i]) / int(str[i+1:])
    return res
