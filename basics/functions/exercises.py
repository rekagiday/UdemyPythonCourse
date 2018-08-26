weekdays = ['Sunday', 'Monday','Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
def return_day(num):
    if num >=1 and num <= 7:
        return weekdays[num-1]
    return None

print(return_day(3))
print(return_day(8))

    ######

def last_element(list):
    if list:
        return list[-1]
    return None

print(last_element([1,2,3]))
print(last_element([]))

    ######

def number_compare(a, b):
    if a > b:
        return "First is greater"
    elif b > a:
        return 'Second is greater'
    return 'Numbers are equal'

print(number_compare(1,3))
print(number_compare(1343252524542,3141234141))
print(number_compare(77,77))

    ######

def single_letter_count(string, letter):
    return string.lower().count(letter.lower())

print(single_letter_count('alMAfa', 'a'))
print(single_letter_count('alMAfa', 'x'))

    ######

def multiple_letter_count(string):
    return {letter:string.count(letter) for letter in string}

print(multiple_letter_count('awesomesauce'))

    #####

def list_manipulation(list, command, location, value=0):
    if command == 'remove':
        if location == 'end':
            return list.pop()
        elif location == 'beginning':
            return list.pop(0)
    elif command == 'add' and value:
        if location == 'end':
            list.append(value)
        elif location == 'beginning':
            list.insert(0, value)
        return list

print(list_manipulation([1,2,3], "remove", "end"))
print(list_manipulation([1,2,3], "remove", "beginning"))
print(list_manipulation([1,2,3], "add", "beginning", 20))
print(list_manipulation([1,2,3], "add", "end", 30))

    #####

def is_palindrome(string):
    s = string.replace(" ", "")
    return s.lower() == s[::-1].lower()
    return s.lower() == s[::-1].lower()

print(is_palindrome('taCocAT'))
print(is_palindrome('a man a plan a canal Panama'))

    ######

def frequency(list, term):
    return list.count(term)

print(frequency([1,2,3,1,2,3,1,2,1,2,1], 1))

    ######

def multiply_even_numbers(list):
    total = 1
    for num in list:
        if num % 2 == 0:
            total = num * total
    return total

print(multiply_even_numbers([1,2,3,4,5,6]))

    ######

def capitalize(string):
    return string[0].upper() + string[1:]

print(capitalize("reka"))

    #####

def compact(l):
    """ compact(list): accepts a list as parameter and returns a list with only the truty values from the original list """
    return [val for val in l if val]

print([1,0,"", "Hello", [22,33], []])

    #####

def intersection(a, b):
    """" intersection of 2 lists """
    return list(set(a) & set(b))

print(intersection([1,2,3,4],[3,4,5,6]))

    ######


def isEven(num):
    return num % 2 == 0

def partition(list, function):
    """ sorts a list of numbers depending on partity to 2 lists (evens and odds)
    returns with these lists as a list """

    evens = []
    odds = []
    for num in list:
        if isEven(num):
            evens.append(num)
        else:
            odds.append(num)
    return [evens, odds]

print(partition([1,2,3,4,5,6,7,8], isEven))
