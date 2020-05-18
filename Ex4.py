# Ex 4
# 18/5/20
# Ask the user for a number then prints out a list of all the divisors
# for that number (divisor is a number that divides evenly into another
# number). For eg. 13 is a divisor of 26.

num = int(input('Enter a number: '))

print(list(range(2, num + 1)))
array = []
for element in list(range(2, num+1)):
    if num % element == 0:
        array.append(element)

print(array)
