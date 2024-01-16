# Here fuction means entity to represent a part and separate the code that use repeatedly

def mux(a, b):
    if a > b:
        print(a, "is greater than", b)
    elif a < b:
        print(b, "is greater than", a)
    else:
        print(a, "and", b, "are equal")


mux(3, 6)
