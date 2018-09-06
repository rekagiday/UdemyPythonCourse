numbers = [1,76,2,5,4,3,242,0]
sorted(numbers) #[0,1,2,3,4,5,76,242]
sorted(numbers, reverse=True) # [242, 76, 5, 4, 3, 2, 1]
print(numbers) #[1,76,2,5,4,3,242,0]


##

users = [
    {'username': 'Sam', 'tweets': ['I love potatos!', 'I lost my food... :(']},
    {'username': 'Frodo', 'tweets': []},
    {'username': 'Gandalf', 'tweets': ['Run, you fools!']},
    {'username': 'Aragorn', 'tweets': []}
]

print(sorted(users, key = lambda user: user['username']))
print(sorted(users, key = lambda user: len(user['tweets'])))
