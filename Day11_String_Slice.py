name = "ABCDEFGHIJKLMNOP"

print(name[1:4])
print("The len of name is", len(name))
print(name[-16:-1])  # Here -1 means that len(name)-1
print(name[(len(name)-1) : (len(name)-4)])

print(name[:4])

print(name[::2])