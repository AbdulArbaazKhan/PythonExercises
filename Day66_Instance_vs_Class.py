class Employee:
    company_name = "Panda"  #class variable
    No_of_Employee = 0
    def __init__(self, name):
        self.name = name
        self.raise_amount = 0.02  #instance variable bcz associated with instance
        Employee.No_of_Employee += 1

    def showDetails(self):
        print(f"The name of Employee is {self.name}. The raise amount in {self.company_name} is {self.raise_amount}. Company Employee is {Employee.No_of_Employee}")

emp1 = Employee("Jhon")
emp1.company_name = "USA Panda"  # Preference given to instance var
Employee.showDetails(emp1)
emp1.showDetails()

Employee.company_name = "Google"

emp2 = Employee("Alex")
emp2.raise_amount = 3
Employee.showDetails(emp2)
emp2.showDetails()