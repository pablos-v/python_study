# v stolbik
# with open('22.txt') as file:
#     ls = [(i, i ** 2) for i in [int(line.strip()) for line in file.readlines()] if i % 2 == 0]

# print(ls)

# v stroky
with open('22.txt') as file:
    ls = [(i, i ** 2) for i in [int(line) for line in (file.read()).split(' ')] if i % 2 == 0]

print(ls)

