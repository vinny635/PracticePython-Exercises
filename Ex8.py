# Exercise 8 - Rock Paper Scissors
# Date 19/5/20
# Make a two-player Rock Paper Scissors game. Ask for player plays, compare them,
# print out a message of congratulations to the winner and ask if the players want
# to start a new game

# not_game_over = True
# print('Rock Paper Scissors Game')
# a = input('Player 1\'s turn:')
# b = input('Player 2\'s turn:')
#
# while not_game_over:
#     if a == b:
#         print('It is a tie. Try again.')
#         a = input('Player 1\'s turn:')
#         b = input('Player 2\'s turn:')
#     elif a == 'rock' and b == 'scissors' or a == 'scissors' and b == 'paper' or a == 'paper' and b == 'rock':
#         print('Player 1 wins!')
#         again = input('Try again?')
#         if again == 'no':
#             not_game_over = False
#         elif again == 'yes':
#             a = input('Player 1\'s turn:')
#             b = input('Player 2\'s turn:')
#     elif b == 'rock' and a == 'scissors' or b == 'scissors' and a == 'paper' or b == 'paper' and a == 'rock':
#         print('Player 2 wins!')
#         again = input('Try again?')
#         if again == 'no':
#             not_game_over = False
#         elif again == 'yes':
#             a = input('Player 1\'s turn:')
#             b = input('Player 2\'s turn:')
#     elif a != 'rock' or a != 'paper' or a != 'scissors' or b != 'rock' or b != 'paper' or c != 'scissors':
#         print('Invalid. Key in either rock, paper, or scissors.')
#         a = input('Player 1\'s turn:')
#         b = input('Player 2\'s turn:')

# PLAYER 2 IS COMPUTER
import random

plays = ['rock', 'paper', 'scissors']
computer = plays[random.randint(0, 2)]

not_game_over = True
print('Rock Paper Scissors Game')
a = input('Player 1\'s turn:')
print('Player 2\'s turn: %s' % computer)

while not_game_over:
    if a == computer:
        print('It is a tie. Try again.')
        a = input('Player 1\'s turn:')
        computer = plays[random.randint(0, 2)]
        print('Player 2\'s turn: %s' % computer)
    elif a == 'rock' and computer == 'scissors' or a == 'scissors' and computer == 'paper' or a == 'paper' and computer == 'rock':
        print('Player 1 wins!')
        again = input('Try again?')
        if again == 'no':
            not_game_over = False
        elif again == 'yes':
            a = input('Player 1\'s turn:')
            computer = plays[random.randint(0, 2)]
            print('Player 2\'s turn: %s' % computer)
    elif computer == 'rock' and a == 'scissors' or computer == 'scissors' and a == 'paper' or computer == 'paper' and a == 'rock':
        print('Player 2 wins!')
        again = input('Try again?')
        if again == 'no':
            not_game_over = False
        elif again == 'yes':
            a = input('Player 1\'s turn:')
            computer = plays[random.randint(0, 2)]
            print('Player 2\'s turn: %s' % computer)
    else:
        print('Invalid. Key in either rock, paper, or scissors.')
        a = input('Player 1\'s turn:')
        computer = plays[random.randint(0, 2)]
        print('Player 2\'s turn: %s' % computer)
