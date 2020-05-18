# Exercise 5 - List Overlap
# Date: 18/5/20
# Description: Program takes in two lists and returns a list that contains only
# the elements common between the lists without duplicates.

a = [1, 2, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []

print(a)
print(b)

for element in b:
    if element in a:
        c.append(element)

print(c)

# Extras
# Randomly generate two lists to test this
# Write this in one line of Python
import random

a = [random.randrange(1, 41) for _ in range(0, random.randint(1, 20))]
b = [random.randrange(1, 41) for _ in range(0, random.randint(1, 20))]
c = []

print(a)
print(b)

[c.append(element) for element in b if element in a], print(c)
