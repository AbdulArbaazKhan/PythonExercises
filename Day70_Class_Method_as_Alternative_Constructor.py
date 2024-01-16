class Employee:
    def __init__(self, name , age):

        self.name = name
        self.age = age

    @classmethod  # Here classmethod as alternative constructor
    def from_str(cls, data_of_e):
        return cls(data_of_e.split("-")[0], data_of_e.split("-")[1])

e1 = Employee("Jhon", 21)
print(e1.name, e1.age)

#TODO: Alternative method if data is given in another variety

data_of_e1 = "Alex-12"
e2 = Employee(data_of_e1.split("-")[0], data_of_e1.split("-")[1])
print(e2.name, e2.age)  #TODO: But we can do it in more organized way by class method

e3 = Employee.from_str("ALiya-23")
print(e3.name, e3.age)