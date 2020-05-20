# Exercise 11 - Check Primality Functions
# Date: 19/5/20
# Description: Ask the user for a number and determine if the number is prime or not.

def prime(num):
    for element in range(2, num):
        if num % element == 0:
            print('The number is not a prime number.')
            break
        else:
            print('The number is a prime number.')
            break


num = int(input('Key a number to check if it\'s a prime number:'))
prime(num)
