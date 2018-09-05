def remove_negatives(nums):
    return list(filter(lambda x: x>=0, nums))

print(remove_negatives([0,-1,2,-3,4,-45,134,-3425,7]))
