# Exercise 2: Odd or Even
# 17/5/20
# Ask the user for a number and determine if the number is even or odd

# number = int(input('Enter a number: '))
# remainder1 = number % 4
# remainder2 = number % 2
# if remainder1 == 0:
#     print('The number ' + str(number) + ' is a multiple of 4.')
# elif remainder2 == 0:
#     print('The number ' + str(number) + ' is even.')
# else:
#     print('The number ' + str(number) + ' is odd.')

# Ask the user for a number to check (num) and another number to
# divide by (check). If answer retrieved from num divided by check
# is even or odd, tell user appropriately.

num = int(input('Enter a number: '))
check = int(input('Enter another number to divide: '))

ans = num / check
remainder = ans % 2
if remainder == 0:
    print('Answer is ' + str(ans) + ' which is even.')
else:
    print('Answer is ' + str(ans) + ' which is odd.')
