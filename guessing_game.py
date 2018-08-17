import random

wanna_play ="y"
while wanna_play != "n":
    random_number = random.randint(1,30)
    player_guess = int(input("Guess the number from 1 to 30: "))
    while player_guess != random_number:
        if player_guess > random_number:
            player_guess = int(input("Too high, try again "))
        else:
            player_guess = int(input("Too low, try again "))
    print("Correct! You win.")
    wanna_play = input("Do you want to play again? y/n ")
    if wanna_play != "y":
        break
print("Thanks for playing! Bye!")
