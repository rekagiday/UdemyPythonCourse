name = "Réka"
guess = 7

answer = f"Nice try, {name}, but your guess of {guess} is wrong." #from python 3.6
print(answer)

guess += 1
old_answer = "Nice try, {}, but your guess of {} is wrong.".format(name, guess) #older versions before 3.6
print(old_answer)
