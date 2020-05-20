# Exercise 9 - Guessing Game One
# 19/5/20
# Description: Generate a random number between 1 and 9 and ask the user to
# guess the number, telling them if they guessed too high, too low or exactly
# right

# Extras
# Keep the game going until user types 'exit
# Keep track of how many guesses the user took and when the game ends, print it out
import random

# while condition for verifying if user wants to play again
x = False
not_game_over = True
count = 0
jackpot = random.randint(1, 9)
user = int(input('Guess the number between 1 and 9 (both inclusive):'))
while not_game_over:
    if user > jackpot:
        print('You\'ve guessed too high!')
        user = int(input('Guess the number between 1 and 9 (both inclusive):'))
        count += 1
    elif user < jackpot:
        print('You\'ve guessed too low!')
        user = int(input('Guess the number between 1 and 9 (both inclusive):'))
        count += 1
    else:
        print('You\'ve guessed it correctly!')
        count += 1
        print('You took ' + str(count) + ' tries.')
        count = 0
        again = input('Play again? (Key either \'exit\' or \'yes\'):')
        x = True
        while x:
            if again == 'exit':
                not_game_over = False
                x = False
            elif again == 'yes':
                jackpot = random.randint(1, 9)
                user = int(input('Guess the number between 1 and 9 (both inclusive):'))
                x = False
            else:
                again = input('Invalid input. Key either \'exit\' or \'yes\':')
