instructor = dict(name = 'Colt', language = 'Python', city ='San Fransisco', color = 'purple')
yelling_instructor = {(k.upper() if k is 'color' else k):v.upper() for k,v in instructor.items()}
print(yelling_instructor)


print({num:("even" if num % 2 == 0 else "odd") for num in range(1,21)})
