# Tuples cannot be changed

tp = (2,4,6,8,10)
print(tp)
print(type(tp))

# TODO: See a new challenging situation
# tp = (8)  # is it tuple or not
print(type(tp)) # see it is int
#TODO: it should be write tp = (8,)

# tp[0] = 80 # error not changeable
print(tp[0])
print(tp[1])
print(tp[2])
print(tp[3])
print(tp[-3])
print(tp[::2])