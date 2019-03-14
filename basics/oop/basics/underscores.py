# _name       'private attribute': this is used to mark a private variable
# __name      'name mangling': makes an attribute unavailable to child classes
# __name__    'dunder method': this is used to override python specific methods

class Person():
    def __init__(self):
        self.name = "Pete"
        self._secret = "Hi!"  #marks a private attribute
        self.__message = "I like pie!" #this will only be available on Person class

p = Person()
print(p.name, p._secret)
print(p._Person__message)
