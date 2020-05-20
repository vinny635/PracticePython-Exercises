# Exercise 6 - String Lists
# Date: 18/5/20
# Ask the user for a string and print out if this string is a palindrome or not
# A palindrome is a string that reads the same forward and backward

string = input('Type a string:')

if string[:] == string[::-1]:
    print('This is a palindrome.')
else:
    print('This is not a palindrome in which the reverse string is %s.' % string[::-1])
