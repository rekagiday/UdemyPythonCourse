data = [1,2,3]
data.clear()
data.append(4)
data.extend([5,6,7,8])
data.insert(0, 'Hi!')
data.insert(len(data), 'last')
print(data)

data.pop()
print(data)

data.pop(0)
print(data)

data.remove(6)
print(data)
