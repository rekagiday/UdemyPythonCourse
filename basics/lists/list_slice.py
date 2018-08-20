names = ['Anna', 'Betty', 'Charles', 'Dave', 'Eric', 'Frank', 'Gerry', 'Hugo', 'Ian', 'Joe', 'Kelly']

# slice: list[stat:end:step]

print(names[2:]) # prints from the 2nd index
print(names[-5:]) # prints the last 5 elements

print(names[:2]) # prints from 0 to 2 index
print(names[2:5]) # prints from index 2 (inclusive) to index5 (exclusive)

print(names[2:9:2]) # prints every 2nd element from index 2 (inclusive) to index 9 (exclusive)
print(names[::3]) # prints every 3rd element

# negative 3rd parameter reverses the order, end < start now
print(names[7:0:-1]) # prints from index7 back to index 0(exclusive)
print(names[7::-1]) # prints from index7 back to index 0
print(names[::-2]) # print every other element starting from the last going backwards

#replacing certain elements
names[1:4] = ['Xavier', 'Yennefer', 'Zoey']
print(names)
