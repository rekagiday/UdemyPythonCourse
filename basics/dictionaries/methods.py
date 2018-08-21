student = dict(name = 'Joe', age= 18, is_hungry=False)
person = student.copy()

# generating default values: .fromkeys
user = {}.fromkeys(['name', 'age', 'email', 'score', 'phone'], 'unknown')
stuff = dict.fromkeys(['name', 'price'], 'unknown')

student.clear() # clears the dict

person.get('age') # 18
person.get('score') # None 
