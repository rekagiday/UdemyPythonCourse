from random import choice

player_wins = 0
computer_wins = 0
print("****  ROCK  ****  PAPER  **** SCISSORS  **** \n type: r = rock, p = paper, s = scissors")
name = input('player name: ')

while player_wins < 3 and computer_wins < 3:
    computer = choice(['r', 'p', 's'])
    player = input('Make your choice, ' + name+ ': ').lower()
    print('Computer\'s choice: ' + computer)
    if player and player == 'r' or player == 'p' or player == 's':
        if player == computer:
            print('Tie!')
        elif player == 'r' and computer == 's' or player == 'p' and computer == 'r' or player == 's' and computer == 'r':
            player_wins += 1
            print(name + ' wins!')
        else:
            computer_wins += 1
            print('Computer wins!')
    else:
        print('Invalid player input')
print("Game over!")
if player_wins == 3:
    print(f"The winner is: {name}!")
else:
    print("The winner is the Computer!")
