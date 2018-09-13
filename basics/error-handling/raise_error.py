def colorize(text, color):
    colors = ('red', 'blue', 'purple', 'yellow', 'orange', 'white', 'black', 'green')
    if type(color) is not str :
        raise TypeError("color must be instance of string.")
    if type(text) is not str :
        raise TypeError("text must be instance of string.")
    if color not in colors:
        raise Exception("Color must be a base color")
    print(f"{text} in {color}")

colorize("hello!", "red")
colorize("hello!", "brown")
# colorize("hello!", 10)
# colorize(20, "red")
