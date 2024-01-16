#TODO: Sometimes we need to execute some code even after the error

# You can raise or handle error of specific error


try:
    n = int(input("Enter a number\n"))
    a = [9, 10]
    print(a[n])
    for i in range(n):
        print(f"{n} x {i} = {n*i}")
except ValueError:
    print("Invalid input")
# except Exception as e:
#     print(e,  "This is the error")
except IndexError:
    print("Index error")
print("These are most important code to execute") # But if there is error in any above line then this code is not executed
#To do this use try except block