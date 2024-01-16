x = 6
print(x)

def hello():
    global x
    x = 5
    y = 1
    print("The local x is ", x)
    print("Hello")
hello()
print("The global x is ", x)
# print(y) #error bcz y is local