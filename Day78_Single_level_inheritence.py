class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        return "Sound made by animal"

class Cat(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name, species="Cat")
        self.breed = breed

    def make_sound(self):
        return "Mew!"

    def move(self):
        return "Moved 10 meter"

cat1 = Animal("Cat", "Cat")
print(cat1.make_sound())
cat2 = Cat("Cat", "Cater")
print(cat2.make_sound())
