numbers = [1, 2, 3, 1, 2, 3, 1, 2, 3]

numbers.index(3)  # 2
numbers.index(3, 6) # 9: index of first occurence of given item, starting from nth index (2nd param)
numbers.index(3, 3, 6) # 5, first occurence of given item in between 2nd and 3rd params as indexes

numbers.count(1) # 3
numbers.count(8) # 0

numbers.reverse() # [3 ,2, 1, 3, 2, 1, 3, 2, 1]

numbers.sort() # [1, 1, 2, 2, 3, 3]
