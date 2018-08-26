def generate_evens():
    return list(range(2,50,2))

def raise_to_power(num, power = 2):
    """raise_to_power(num, power): raises num to a specified power, power defaults to 2 """
    return num**power
print(raise_to_power(3,3))
print(raise_to_power(7))
print(raise_to_power(power = 3, num = 5))
print(raise_to_power.__doc__)

def add(a, b):
    return(a + b)

def subtract(a, b):
    return(a - b)

def math(a, b, fn = add):
    return(fn(a, b))

print(math(2,3))

print(math(10,2,subtract))
