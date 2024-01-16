try:
    l = [1,5,6,7]
    i = int(input("Enter the index: "))
    print(l[i])
except:
    print("Some error occurred")

finally:
    print("I am always executed not matter error has or not")

#TODO: There is a slight difference in other approach of Finally - see

def func1():
    try:
        l = [1, 5, 6, 7]
        i = int(input("Enter the index: "))
        print(l[i])
        return 1
    except:
        print("Some error occurred")
        return 0

    finally:
        print("I am always executed not matter error has or not")

    # print("I am always executed not matter error has or not")

print(func1())
# See the last print statement will be skipped, but finally executed even if the function is returned - easy