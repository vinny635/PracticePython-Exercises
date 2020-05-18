# Exercise 1
# Date: 17/5/20
# Description: Program asks for user's name and age. Print a message
# telling them the year that they will turn 100 years old

name = input('Enter name: ')
print('Your name is ' + name + '.')

hundred = 100
age = input('Enter age: ')
print('You are ' + age + ' years old.')
age = int(age)

diff = hundred - age
year = 2020
future_year = 2020 + diff
future_year = str(future_year)
print('You will reach 100 years old in the year ' + future_year + '.')
