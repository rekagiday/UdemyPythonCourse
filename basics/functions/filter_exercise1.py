users = [
    {'username': 'Sam', 'tweets': ['I love potatos!', 'I lost my food... :(']},
    {'username': 'Frodo', 'tweets': []},
    {'username': 'Gandalf', 'tweets': ['Run, you fools!']},
    {'username': 'Aragorn', 'tweets': []}
]

inactive_users = list(filter(lambda user: not user['tweets'], users))

print(inactive_users)
