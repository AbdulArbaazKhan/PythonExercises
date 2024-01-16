list1 = [10, 10, 20, "none"]   #can be changed

# print(list1)
# print(list1[0])
# print(list1[1])
# print(list1[2])
#TODO: Index is 3 vs Length is 4

print(list1[-2])
print(list1[len(list1)-2])

if 4 in list1:
    print("Yes")
else:
    print("No")

#Same with strings
if "Ha" in "Harry":
    print("yes")

print(list1)
print(list1[:])
print(list1[1:-1])
print(list1[1:len(list1)-1:2]) #here 2 is jumpindex

#TODO: List comprehension
l = [i*i for i in range(10)]
print(l)
l = [i*i for i in range(10) if i%2==0]
print(l)