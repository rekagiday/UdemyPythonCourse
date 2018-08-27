# def sum_all_numbers(num1, num2, num3, num4):
#     return sum1 + sum2 + sum3 + sum4

def sum_all_numbers(*args): # *args is a tuple
    sum = 0
    for num in args:
        sum += num
    return sum

print(sum_all_numbers(2,6,2,87,342,0,233,12,-6))
print(sum_all_numbers(2,-6))


def check_correct_user(*args):
    if "Reka" in args and "Giday" in args:
        return "Welcome back, Reka!"
    return "Who are you?"

print(check_correct_user("Reka", 10, "python", "Giday", True))
print(check_correct_user())

def fav_colors(**kwargs): # **kwargs (keyword args) is a dictionary
    for person, color in kwargs.items():
        print(f"{person}\'s favourite color is {color}")

fav_colors(Reka="purple", Balint="blue")


def combine_words(word, **kwargs):
    if 'prefix' in kwargs:
        return kwargs['prefix'] + word
    elif 'suffix' in kwargs:
        return word + kwargs['suffix']
    return word

print(combine_words("child", prefix="foster"))
print(combine_words("child", suffix="ish"))
print(combine_words("child", name="Ashley"))
