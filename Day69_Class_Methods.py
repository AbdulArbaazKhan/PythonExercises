class Employee:
    company = "Apple"

    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"The name of {self.name} and THe commpany is {self.company}")
    @classmethod
    def change_company(cls, new_company):
        cls.company = new_company

e1 = Employee("Jhon")
e1.show()
e1.change_company("Google") #Here it will not change the company name, bcz preference given to instance but to do see
e1.show()

print(Employee.company)

