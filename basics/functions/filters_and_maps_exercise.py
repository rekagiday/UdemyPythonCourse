instructors = ['Abigail', 'Bob', 'Colt']

names = ['Lassie', 'Blue', 'Jamie', 'Colt']

your_instructors = list(map(lambda name: f"Your instructor is: {name}",
    filter(lambda val : val in instructors, names)))

print(your_instructors)
