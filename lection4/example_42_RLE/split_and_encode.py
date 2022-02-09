def encoder(input):
    s = ''
    for i in split_to_chars(input):
        s += str(len(i)) + i[0]
    return s


def decoder(input):
    st = ''
    for i in split_to_pairs(input):
        st += i[0] * i[1]
    return st


def split_to_pairs(input):
    nums = []
    chars = []
    temp = ''
    itr = 0
    while itr < len(input):
        try:
            n = int(input[itr])
            temp += input[itr]
            itr += 1
        except ValueError:
            if itr != len(input):
                nums.append(int(temp))
                temp = input[itr]
                for c in input[itr+1:]:
                    try:
                        n = int(c)
                        chars.append(temp)
                        temp = c
                        itr += 1
                        break
                    except ValueError:
                        temp += c
                        itr += 1
                else:
                    chars.append(temp)
                itr += 1

    return list(zip(nums, chars))


def split_to_chars(input):
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
