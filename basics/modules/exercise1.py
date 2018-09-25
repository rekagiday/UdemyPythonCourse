import keyword

def contains_keyword(*args):
    for word in args:
        if keyword.iskeyword(word):
            return True
    return False
print(contains_keyword("def", "happy"))
