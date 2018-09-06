people = ['Cody', 'Claire', 'Charlie', 'Joe']
all(name[0] == 'C' for name in people) #False

any(name[0] == 'J' for name in people) #True
