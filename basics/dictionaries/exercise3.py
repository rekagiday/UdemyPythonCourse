person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]

answer1 = {item[0]: item[1] for item in person}

answer2 = {k:v for k,v in person}

answer3 = dict(person)
