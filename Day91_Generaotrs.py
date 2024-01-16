# Genetrates on the fiy creates value
# Not stores the value but stores the info to make that value on the fly

def my_generater():
    for i in range(5):
        yield i

gen = my_generater()
# print(gen) #object
print(next(gen))
print(next(gen))
print(next(gen))

# Saves memory becz generates value on the fly while in list, tuples, strings we have to save values first

for g in gen:
    print(g)