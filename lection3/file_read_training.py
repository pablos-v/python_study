# v stolbik
# with open('22.txt') as file:
#     ls = [(i, i ** 2) for i in [int(line.strip()) for line in file.readlines()] if not i % 2]

# print(ls)

# v stroky
with open('22.txt') as file:
    ls = [(i, i ** 2) for i in [int(e) for e in file.read().split()] if not i % 2]

print(ls)

