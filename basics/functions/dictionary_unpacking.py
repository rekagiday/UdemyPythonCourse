names = dict(first = "Colt", second = "Rusty")

def display_names(first, second):
    print(f"{first} says hello to {second}")

display_names(**names)
