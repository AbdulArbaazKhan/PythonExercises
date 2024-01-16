

"""
    r - read only when file exists otherwise through error, also default mode
    w - open in write mode and also creates the file if not exists, deletes previous text
    a - append the text at the end
    b - open in binary mode like rb for jpeg like formats
    x - this mode creates the file and give error if the file exists
    r+ - read and write

"""
# f = open('myfile.txt', 'r')
# print(f)
# text = f.read()
# print(text)
# f.close()

# f = open('myfile.txt', 'w')
# f.write("Hello world")
# f.close()

# f = open('myfile.txt', 'a')
# f.write("Hello world")
# f.close()

with open('myfile.txt', 'a') as f:
    f.write("Hey i am in inside")
    #This will automatically close the file