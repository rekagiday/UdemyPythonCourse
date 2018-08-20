student = {
    'name': 'Réka',
    'owns_dragon': True,
    'age': 32.5,
    'favourite_color': 'purple',
    'languages': ['Java', 'JavaScript', 'Python']
}

# check if key exists in dict
if "name" in student:
    print(f"Name: {student['name']}")
else:
    print("name does not exist")

# check if value exists in dict
if "purple" in student.values():
    print("Awesome!")

language = "Java"
if language in student["languages"]:
    print(f"{student['name']} knows {language}")
else:
    print(f"{student['name']} doesn\'t know {language}")
