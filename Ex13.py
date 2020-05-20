# Exercise 13 - Fibonacci
# Date: 20/5/20
# Description: Program asks the user how many Fibonacci numbers to generate and then
# generates them.


def fibonacci():
    a = [1]
    user = int(input('How many Fibonacci numbers do you want?'))
    if user == 0:
        return print('No sequence')
    elif user == 1:
        return print(a)
    else:
        value_2 = 0
        value_1 = 1
        for count in range(1, user):
            sum = value_1 + value_2
            a.append(sum)
            value_2 = value_1
            value_1 = sum
            count += 1
        return print(a)


fibonacci()
