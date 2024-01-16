#TODO: Doc-strings provide info about function, method, class

def square(n):
    """
    This function takkes an int
    :return: square
    """

    print(n**2)

print(square.__doc__)
#TODO: If it is not written below the name of class or function or any then its not a doc-sting
def square2(n):
    print(n)
    """
    This function takkes an int
    :return: square
    """

    print(n**2)


print(square2.__doc__)

#TODO: FIng info PEP-8
import this