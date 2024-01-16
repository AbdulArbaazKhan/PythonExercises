from functools import reduce
# MAP
def cube(x):
    return x ** 3


l = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# new_l = []
# for item in l:
#     new_l.append(cube(item))
# TODO: See - this is very painful, so there is an essay approach to do this


# You can use lambda function in map


# new_l = map(cube, l) # returns the map object
# new_l = list(map(cube, l))
new_l = list(map(lambda x : x**3, l))
print(new_l)


# FILTER
def filter_func(a):
    return a > 4


# new_l2 = filter(filter_func, l) #gives the filter object
# new_l2 = list(filter(filter_func, l))
new_l2 = list(filter(lambda a : a>4, l))
print(new_l2)

# REDUCE

numbers = [1, 3, 5, 7, 11]

new_l3 = reduce(lambda x,y : x + y, numbers)
#TODO: See how it wil calculate
# [1, 3, 5, 7, 11]
# [4, 5, 7, 11]
# [9, 7, 11]
# [16, 11]
# 27
print(new_l3)