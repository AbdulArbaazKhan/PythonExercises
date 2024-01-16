class Person():
    name = "Harry"
    Occupation = "Software Developer"
    networth = 10
    def info(self):
        print(f"{self.name} is a {self.Occupation}")

a = Person()
a.name = "Ali"
a.Occupation = "Painter"
b = Person()
b.name = "Aman"
b.Occupation = "Racer"
# print(a.name)
a.info() # self is a
b.info() # self is b