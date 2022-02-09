def split_data(input):
    res = []
    temp = [input[0]]
    for i in range(1, len(input)):
        if input[i] == temp[-1]:
            temp.append(input[i])
        else:
            res.append(temp)
            temp = [input[i]]
    res.append(temp)
    return res


def encoder(input):
    s = ''
    for i in split_data(input):
        s += str(len(i)) + i[0]
    return s
