with open('myfile2.txt', 'r+') as f:
    print(type(f))
    f.truncate(9)
    f.seek(10)
    print(f.tell()) # gives current_position
    data = f.read(3)
    print(data)