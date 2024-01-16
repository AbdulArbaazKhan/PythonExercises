class Vector:

    def __init__(self,i, j, k):
        self.i = i
        self.j = j
        self.k = k

    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"
    def __add__(self, other):
        return Vector(self.i + other.i, self.j + other.j, self.k + other.k) #we make a new vector by using vector constructor
v1 = Vector(3, 5, 7)
print(v1)

v2 = Vector(5, 8, 4)
print(v2)

print(v1+v2)