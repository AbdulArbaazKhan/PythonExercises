# There are four types of arguments in function

# Default argument
# Keyword Argument
# Variable length Argument
# Required Argument


# def average(c, a=2, b=2):  # Here 2, 2 are default
#     # Here c is required argument
#     print("The average is ", (a + b) / 2)
#
#
# # averg(5) a =5
# average(4, a=8, b=9) # order does not matter (Keyword argument key=value)


def average(*numbers): # Variable Length arguments
    sum = 0
    for i in numbers:
        sum += i
    # print("The average is: ", sum/len(numbers))
    return  sum/len(numbers)

print(average(10,10))



def name(**name): # Keyword arbitarily argument
    print(name)

name(one="A", two="B")
