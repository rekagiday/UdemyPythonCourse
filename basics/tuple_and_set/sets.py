stuff = set({1,2,3,3,4,5,6,6,6,6}) # {1,2,3,4,5,6} ----- cannot have duplicates

s = {1,2,3}

1 in s #True
4 in s #False

for number in s:
    print(number)

list_of_cities = ['Budapest', 'Szeged', 'Dublin', 'Los Angeles', 'Tokyo', 'Budapest', 'Oslo', 'Szeged']
# sorting the list to leave unique entries only:
print(list(set(list_of_cities)))

list_of_cities.add('Ohio')

list_of_cities.remove('Los Angeles')
list_of_cities.discard('Los Angeles') #same as remove but wont throw an error if item is not in the set

other_list_of_cities = list_of_cities.copy()

list_of_cities.clear()

#set of square numbers
{x**2 for x in range(10)}
