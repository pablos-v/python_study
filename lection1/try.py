# from random import *
# print(randint(1, 23))
from random import*
from array import*

def generate_array():
    ls = []
    for i in range(12):
        ls.append(randint(-9,9))
    arr = array('i')
    arr.fromlist(ls)
    return arr

print(generate_array())