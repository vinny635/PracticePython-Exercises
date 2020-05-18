# Exercise 3: List Less Than Ten
# 17/5/20
# Take a list and write a program that prints out all the elements of
# the list that are less than 5

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []

for element in a:
    if element < 5:
      b.append(element)

print(b)
b = []
# [2.b] output as extra 1 solution
print([element for element in [1, 1, 2, 3, 6, 8, 13, 21, 34, 55, 89] if element < 5])

# [2.c]

num = int(input('Enter a number: '))
for element in a:
    if element < num:
      b.append(element)

print(b)
