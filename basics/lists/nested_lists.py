nested_list = [[1,2,3], [4,5,6], [7,8,9]]

# for list in nested_list:
#     for number in list:
#         print(number)

[[print(number) for number in list] for list in nested_list]

board =[[num for num in range(1,6)] for row in range(1,6)]
print(board)

print([['X' if num % 2 != 0 else 'O' for num in range(1,6)] for row in range(1,6)])
