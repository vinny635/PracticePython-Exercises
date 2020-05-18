# EX5
# 18/5/20
# Program takes in two lists and returns a list that contains only
# the elements common between the lists without duplicates.

# a = [1, 2, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []

a = input()
b = input()

print(a, b)

for element in b:
    if element in a:
        c.append(element)

print(c)