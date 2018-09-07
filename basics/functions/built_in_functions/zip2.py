students = ['Bill', 'Amanda', 'Joe', 'Mary']
midterms = [98, 72, 87, 37]
finals = [90, 88, 92, 69]

grades = dict(zip(students, map(lambda pair: max(pair), zip(midterms, finals))))

print(grades)

avg_grades = dict(zip(students, map(lambda score: ((score[0]+score[1])/2), zip(midterms, finals))))

print(avg_grades)
