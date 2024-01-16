import time

# def using_for():
#     for i in range(200):
#         print(i)
#
#
# def using_while():
#     i = 0
#     while i<200:
#         print(i)
#         i+=1
#
# initial = time.time()
# using_for()
# finial = time.time()
# print(finial - initial)
# using_while()
# print(time.time() - finial)

# print(4)
# time.sleep(2)
# print("2 secs")

t = time.localtime()
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", t)
print(formatted_time)