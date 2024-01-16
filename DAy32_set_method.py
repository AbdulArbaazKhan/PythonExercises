s1 = {3,5,7}
s2 = {2, 4, 6}

# print(s1.union(s2)) #TODO: it will create a new with union on it
# s1.update(s2)  #TODO: It will update the set s1 with union
# print(s1)
#
#
# print(s1.intersection(s2))
# s2.intersection_update(s1)
# print(s2)

# s1.symmetric_difference_update(s2)
# print(s1)
#
# s1.difference_update(s2)
# print(s1)

print(s1.isdisjoint(s2))
print(s1.issuperset(s2))
print(s2.issubset(s1))
s1.add("GE")  #TODO: YOu can add by update method
s1.remove("GE") #TODO: It will raise error while discard not
s1.discard("GE")
print(s1)

item = s1.pop()
print(s1)
print(item)


#TODO: THIS will clear all set
s3 = {44.434,54,5,454,}
s3.clear()
print(s3)
del s3

info = {"Carla", 19, False, 5.9}
if "Carla" in info:
    print("Carla is present.")
else:
    print("Carla is absent.")