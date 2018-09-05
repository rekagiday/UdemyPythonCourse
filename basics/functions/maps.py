nums = [1,2,3,4,5,6,7]

doubles = map(lambda c: x*2, nums)

####

names = [
    {"first": "Reka", "last": "Giday"},
    {"first": "Balint", "last": "Biro"},
    {"first": "Ted", "last": "Cooper"}
]
first_names = map(lambda name: names["first"], names)
