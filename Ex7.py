# Ex7
# Date: 19/5/20
# Description: Write one line of Python that takes in the given list
# and makes a new list that has only the even elements of this list in it

# a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# a = [y ** 2 for y in range(1,11)]

print([element for element in [1, 4, 9, 16, 25, 36, 49, 64, 81, 100] if element % 2 == 0])

# for element in a:
#     if element % 2 == 0:
#         b.append(element)
