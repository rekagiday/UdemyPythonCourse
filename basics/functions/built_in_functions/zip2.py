students = ['Bill', 'Amanda', 'Joe', 'Mary']
midterms = [98, 72, 87, 37]
finals = [90, 88, 92, 69]

# grades is the highest score of the 2 tests

grades = zip(
    students, map(lambda pair: max(pair), zip(midterms, finals))
)

print(dict(grades))
