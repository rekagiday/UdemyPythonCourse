instructors = ['Abigail', 'Bob', 'Colt']

names = ['Lassie', 'Blue', 'Jamie', 'Colt']

your_instructors = list(map(lambda name: f"Your instructor is: {name}",
    filter(lambda val : val in instructors, names)))

#same with list comprehension:
your_instructors2 = [f"Your instructor is: {n}" for n in names if n in instructors]

print(your_instructors)
print(your_instructors2)
