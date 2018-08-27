def sum_all_numbers(*args): # *args is a tuple
    sum = 0
    for num in args:
        sum += num
    return sum

nums_list = [45, 6, 321, 56.7, 543, -43]
nums_tuple = [45, 6, 321, 56.7, 543, -43]
print(sum_all_numbers(*nums_list))
print(sum_all_numbers(*nums_tuple))
