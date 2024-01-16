ep1 = {
    122: 45,
    123: 34,
    124: 90
}

ep2 = {222: 43, 500: 43}
ep1.update(ep2)
print(ep1)

# ep1.clear()
# print(ep1)
empt = dict()  # or {}

ep1.pop(122)
print(ep1)

ep1.popitem()  # removes last item
print(ep1)

# del ep2
# del ep2[500] # Then that key will be deleted

