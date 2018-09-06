import sys

list_comprehension = sys.getsizeof([x*2 for x in range(1000)])
generator_expression = sys.getsizeof(x*2 for x in range(1000))

print("To do the same thing, it takes: ")
print(f"{list_comprehension} bytes with list comprehension")
print(f"{generator_expression} bytes with generator expression")
