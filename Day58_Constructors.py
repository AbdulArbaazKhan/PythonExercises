class Person():
    # name = "Harry"
    # Occupation = "Software Developer"
    # networth = 10
    def __init__(self, name, occ): #calls when object make
        self.name = name
        self.occp = occ
    def info(self):
        print(f"{self.name} is a {self.occp}")

a = Person("Harry", "SE")
a.info()


b = Person("Hamid", "Accountant")
b.info()

# Constructor returns None