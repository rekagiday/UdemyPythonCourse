from pyfiglet import figlet_format
from termcolor import colored

def print_art(text, color):
    colors = ('red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white')
    if color not in colors:
        color = 'blue'
    ascii_text = figlet_format(text)
    colored_ascii = colored(ascii_text, color=color)
    print(colored_ascii)

text = input("What do you want to print? ")
color = input("Which color you wanna use? ")

print_art(text, color)
