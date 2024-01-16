class MyClass:
    def __init__(self, value):
        self._value = value

    def show(self):
        print(f"Value is {self._value}")
    @property
    def ten_value(self):
        return 10* self._value

    # @value.setter
    # def value(self, value):
    #     self._value = value
    @ten_value.setter
    def ten_value(self, new_value):
        self._value = new_value/10


obj = MyClass(10)
obj.ten_value = 67 # error you can't set attribute for this make setter
print(obj.ten_value)
# print(obj._value)
obj.show()

#This is encapsulation method