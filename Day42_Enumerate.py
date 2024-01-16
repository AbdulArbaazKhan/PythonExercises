marks_from_10 = [2, 5, 6, 8, 10, 7]
index = 0
# for mark in marks_from_10:
#     print(mark)
#     if index == 4:
#         print("Arbaz, Awesome!")
#     index += 1


# for index, mark in enumerate(marks_from_10):
#     print(mark)
#     if index == 4:
#         print("Arbaz, Awesome!")

for t in enumerate(marks_from_10):
    print(t, type(t))

# TODO: By the way, you can specify the index
for index, mark in enumerate(marks_from_10, start=4):
    print(index, mark)