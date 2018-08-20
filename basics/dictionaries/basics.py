student = {
    'name': 'Réka',
    'owns_dragon': True,
    'age': 32.5,
    'favourite_color': 'purple',
    'languages': ['Java', 'JavaScript', 'Python']
}
student2 = dict(name = 'Joe', age= 18, is_hungry=False)
# accessing a value:
print(student2['name'])

#accessing all keys and values separetly:
for key in student.keys():
    print(key)

for value in student.values():
    print(value)

# accessing all key-value pairs:
for key, value in student.items():
    print(f"{key}: {value}")
