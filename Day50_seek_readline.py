# with open('myfile.txt') as f:
#     i = 0
#     while True:
#         i += 1
#         line = f.readline()
#         if not line:
#             print(line, type(line))
#             break
#         m1 = line.split(",")[0]
#         m2 = line.split(",")[1]
#         m3 = line.split(",")[2]
#         print(f"Marks of studnt {i} in English is", m1)
#         print(f"Marks of studnt {i} in Maths is", m2)
#         print(f"Marks of studnt {i} in Science is", m3)

f = open('myfile2.txt', 'w')
lines = ["line 1\n", "line 2\n", "line 3\n", ]
f.writelines(lines)
f.close()