# Access Specifier - specifies the access of the class attribute(variable) and member function ( functions)
# Types:
# Public - By default
# Private - In python __Variable , But can be accessed by _ClassName__Variable (Name Mangling)
# Protected - In python _Variable, But can be accessed by _Variable same (No name mangling)
#

class Employee:
    def __init__(self):
        self.name = "Arbaz"  # Public
        self.__id = 20221   # Private
        self._age = 20      # Protected
    def _food(self):        # Protected
        return "The favorite food is Rice"
class Servant(Employee):
    pass
a = Employee()
b = Servant()
print(a.name) # can be accessed, changed
# print(a.__id) # cannot be accessed, changed outside
# But to access Private in Python use
print(a._Employee__id) # accessed indirectly can be changed

print(a._age)    #Protected but in python can be accessed
print(b._food()) # Protected

print(a.__dir__())
