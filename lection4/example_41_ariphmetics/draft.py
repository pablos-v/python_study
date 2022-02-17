def str_to_ls(str):
    op = '+-*/'
    ls = []
    start = 0
    for i in range(len(str)):
        if str[i] in op:
            ls.extend([str[start:i], str[i]])
            start = i+1
            # if '+' or '-' or '*' or '/' in str[i+1:]:
            #     ls.extend([str[start:i], str[i]])
            #     start = i+1
            # else:
            #     ls.extend([str[start:i], str[i], str[i:]])
    ls.append(str[start:])
    return ls

print(str_to_ls('4+3-1*2+6-99*-10/-2'))
