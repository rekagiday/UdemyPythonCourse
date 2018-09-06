names = ['Arya', 'Bob', 'Kenny', 'Josephine', 'Zoey']
min(names) # Arya

min(len(name) for name in names) # 3 (length of 'Bob')

print(max(names, key = lambda name : len(name))) # Josiphine
