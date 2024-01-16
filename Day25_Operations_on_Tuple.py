#TODO: As tuple are immutanle

# countries = ("Spain", "Africa", "China", "Pakistan")
# temp = list(countries)
# temp.append("Russia")  #add item
# temp.pop(3) #remove item
# temp[2] = "Finland" #change item
# countries = tuple(temp)
# print(countries)

tuple1 = (1,23,44,23,5,4,5,45,4,4,4,5,54,5,45,3,2,3,3,3,3,3,3,)
# print("The number of occurrence of 4 is ", tuple1.count(4))
# print(tuple1.index(3))  # Gives the index of first occurrence
print(tuple1.index(3, 0, 18))  # Gives the index of first occurrence in range 0 to 18
#index method raise value error it element is not in range
print(len(tuple1))