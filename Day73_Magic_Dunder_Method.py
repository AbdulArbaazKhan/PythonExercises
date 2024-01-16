class Employee:
    def __init__(self, name):
        self.name = name

    def __len__(self):
        i = 0
        for c in self.name:
            i += 1

        return i

    def __str__(self):
        return f"The name of the Employee is {self.name} str"

    # TODO: If str is not defined then repr is used
    def __repr__(self):
        # return f"The name of the Employee is {self.name} repr"
        return f"Employee('{self.name}')"

    def __call__(self, *args, **kwargs):
        return "Hey, I am good"

e = Employee("Aliya")
print(e)  # see we get the str, if it is not defined it will show object location
print(len(e))  # we use these without _ (underscore)

print(str(e))
print(repr(e))
print(e())