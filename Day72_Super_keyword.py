class ParentClass:
    def parentmethod(self):
        print("This the parent method")


class ChildClass(ParentClass):
    # def parentmethod(self):
    #     print("This is the parent method in child")
    #     super().parentmethod() #Prints the method of its parent class
    def childmethod(self):
        print("This is the child method")
#
# obj = ChildClass()
# obj.parentmethod()

# /////////////////////////////////////////////////////////////////////
class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id


class Programmer(Employee):
    # if we want above details with language so one way is to do in the following way
    def __init__(self, name, id, lang):
        self.name = name
        self.id = id
        self.lang = lang

    # TODO: Other way
    def __init__(self, name, id, lang):
        super().__init__(name, id)
        self.lang = lang


a = Employee("Jhon", "23")
b = Programmer("Alex", "231", "Python")
print(b.name, b.id, b.lang)