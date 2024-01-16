# Here is simple concept to understand between Break / Continue

# Break means skip the loop at the point of its declaration

for i in range(15):
    if i==11:
        break
    print(5, "x", i, "=", 5*i)

# Continue means skip the iteration at the point of its declaration

for i in range(15):
    if i==11:
        print("Skip the iteration")  # Here it will execute
        continue # Statements below continue not executed
    print(5, "x", i, "=", 5*i)


# TODO: Do-while loop emulate


while True:
    n = int(input("Enter a number (0 to quit)\n"))
    print("The square of number is ", n**2)
    if n==0:
        break