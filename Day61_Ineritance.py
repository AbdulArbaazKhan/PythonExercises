class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def show_details(self):
        print(f"Tha name is {self.name} and Id is {self.id}")


class Programmer(Employee):
    def showLanguages(self):
        print("The default language is Python")


a = Employee("Ali", 420)
a.show_details()
# a.showLanguages()
a = Programmer("Akram", 421)
a.show_details()
a.showLanguages()
