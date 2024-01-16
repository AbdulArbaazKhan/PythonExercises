# TODO: Walrus Operator is used to assign value within an expression

a = True
# Now i want to do a to false so simply we wil do this
# a = False
print(a)

# But you can do this with the Walrus operator easily

print(a := False)  # Here a has assigned value False and we can also print it
print(a := 4)  # Here a has assigned value 4 and we can also print it

# Use in while loop
numbers = [4, 5, 6, 7, 8, 9]
while (n := len(numbers)) > 0:
    print(numbers.pop())

# Other examples

food = list()
# while True:
#     fd = input("What would you like: ")
#     if fd=="break":
#         break
#     food.append(fd)
# print(food)

while (fd := input("Which food you like: ")) != "quit":
    food.append(fd)
print(food)