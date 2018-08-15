from random import choice

print("****  ROCK  ****  PAPER  **** SCISSORS  **** \n  r = rock, p = paper, s = scissors")
name = input('player name: ')
computer = choice(['r', 'p', 's'])
player = input('Make your choice, ' + name+ ': ')
print('Computer\'s choice: ' + computer)
if player and player == 'r' or player == 'p' or player == 's':
    if player == computer:
        print('Tie!')
    elif player == 'r' and computer == 's' or player == 'p' and computer == 'r' or player == 's' and computer == 'r':
        print(name + ' wins!')
    else:
        print('Computer wins!')
else:
    print('Invalid player input')
