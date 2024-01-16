# import string
#
# import random
#
#
# def return_3chars():
#     return f"{random.choice(list(string.ascii_letters))}{random.choice(list(string.ascii_letters))}{random.choice(list(string.ascii_letters))}"
#
#
# text = input("Enter a text:\n")
#
# words = text.split(" ")
#
# coded_text = ""
# for word in words:
#     if len(word) <= 2:
#         coded_text += word[::-1] + " "
#     else:
#         coded_text += f"{word[1:]}{return_3chars()}{word[0]}{return_3chars()}" + " "
#
# print("\nYour coded is:")
# print(coded_text)
#
# text = input("\nEnter code text:\n")
# # text = "upleFuSTbxV "
# words = text.split(" ")
# encoded_text = ""
# for word in words:
#     if len(word) <= 2:
#         encoded_text += word[::-1] + " "
#     else:
#         encoded_text += word[-4:-3]+word[0: len(word)-7] + " "
#
# print("\nYour encoded text is:")
# print(encoded_text)
import math
area_of_sq = 36
l = int(math.sqrt(36))
print(l)
for i in range(10):
    print(l * "* ")
    print(l*"*\n" + (l-1)*' ' + "*\n", end="")
    print(l*"* ")
    print("\n")
