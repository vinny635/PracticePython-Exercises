# Exercise 14 - List Remove Duplicates
# 20/5/20
# Description: Program takes a list and returns a new list that contains all the elements
# of the first list minus all the duplicates
# Extras: Write two different functions: one using a loop and constructing a list, and another using sets
import random


def list_construct():
    a = [random.randrange(1, 41) for element in range(0, random.randint(1, 20))]
    print(a)
    return a


def set_construct(raw_list):
    return list(set(raw_list))


print(set_construct(list_construct()))
