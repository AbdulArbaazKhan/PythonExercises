x = [1, 2, 3]
print(dir(x))  # dir() Gives all the method of the widget we are using in above case Lists
print(x.__le__)


# TODO: __dict__ Gives atttribute as a dictionary
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.version = 1


p = Person("K", "23")
print(p.__dict__)


print(help(Person))
