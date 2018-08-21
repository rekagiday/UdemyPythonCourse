student = dict(name = 'Joe', age= 18, is_hungry=False)
person = student.copy()

# generating default values: .fromkeys
user = {}.fromkeys(['name', 'age', 'email', 'score', 'phone'], 'unknown')
stuff = dict.fromkeys(['name', 'price'], 'unknown')

student.clear() # clears the dict

person.get('age') # 18
person.get('score') # None

# pop: key must be provided!
user.pop('score')
print(user)

#popitem() : removes a random key-val pair (usually the last given)
user.popitem()
print(user)

# update() : adds a dict to an existing dict
location = dict.fromkeys(['country', 'city', 'address'], 'unknown')
person.update(location)
print(person)

# update also overwrites the items if key already exists in the dict
person.update(stuff)
print(person)
