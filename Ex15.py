# Exercise 15 - Reverse Word Order
# Date: 20/5/20
# Description: Program asks a user for a long string containing multiple words. Print back to the user
# the same string, except with the words in backwards order.

def reverse():
    user = input('Type a string:')
    broken = user.split(' ')
    broken = broken[::-1]
    rejoin = ' '.join(broken)
    print(rejoin)

reverse()