# Exercise 12 - List Ends
# Date: 19/5/20
# Description: Program takes in a list of numbers and makes a new list of only the first
# and last elements of the given list.
import random

a = [5, 10, 15, 20, 25]


def list_ends(arr):
    first = arr[0]
    last = arr[-1]
    random_dict = {1: first, 2: last}
    b = []
    for element in arr:
        element = random.randint(1, 2)
        element = random_dict.get(element)
        b.append(element)

    return b


print(list_ends(a))
