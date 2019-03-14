class User:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

user1=User("Joe", "Smith", 73)
user2=User("Anne", "Perry", 20)
print(user1.first_name, user1.last_name)
print(user2.first_name, user2.last_name)
