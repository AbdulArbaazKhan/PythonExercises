#TODO: Simply takes a function and returns a modified function

def greet(fx):
    def mfx(*args, **kwargs):
        print("Good morning")
        print(fx(*args, **kwargs))
        print("Thanks for using this function")
    return mfx

@greet
def hel():
    print("Hello World")
@greet
def add(a, b):
    return (a+b) #TODO: !

# greet(hel)()  #alternate method
# hel()

#greet(add)(1,2) #Here error bcz it is not taking arguments to do this use args and kwargs
add(1,2 ) # here i solved a problem in decorated function use print with fx bcz add has return value TODO: ! not print value

#TDOD: Watch video for better understanding