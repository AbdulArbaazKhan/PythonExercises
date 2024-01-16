# lambda function is a small function like an expression
# lambda argument : expression

# def double(x):
#     return x*2

double = lambda x: x * 2
cube = lambda x: x ** 3
# avg = lambda x,y : (x+y)/2
avg = lambda x, y, z: (x + y + z) / 2


def give_function(fx, value):
    return 6 + fx(value)


print(double(10))
print(cube(10))
print(avg(10, 10, 10))

print(give_function(cube, 2))
print(give_function(lambda x: x ** 3, 2))

# TODO: These are anonymous function
