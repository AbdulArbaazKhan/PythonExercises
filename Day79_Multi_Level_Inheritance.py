class Employee:
    def __init__(self, name):
        self.name = name

    def show(self):
        return f"The name is {self.name}"


class Dance:
    def __init__(self, dance):
        self.dance = dance

    def show(self):
        return f"The dance is {self.dance}"


class Dance_Employee(Employee, Dance): #order matters here, preference given to Employee class method
    def __init__(self, name, dance):
        super().__init__(name)
        # self.name = name
        self.dance = dance

    # def show(self):
    #     return f"The name is {self.name}"

o = Dance_Employee("Alex", "HipHop")

print(o.show()) #here it will print show method of class Employee
print(Dance_Employee.mro())