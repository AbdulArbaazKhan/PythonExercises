class Maths:
    def __init__(self, n):
        self.num = n

    def increment_num(self, n):
        self.num += n

    @staticmethod
    def add(a, b):
        return a + b


obj = Maths(5)
print(obj.num)
obj.increment_num(10)
print(obj.num)

# TODO: Staticmethods are those that are not associated with instances or objects
print(obj.add(3, 5))
print(Maths.add(4, 7))
# This is a simple add function in class like an ordinary function
# Interview Question: Is self is compulsory to make method in class
# TODO: No, it's not see bcz we can use staticmethod to make function without self
