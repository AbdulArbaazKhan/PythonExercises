Dic = {
    "Arbaz" : "Human being",
    "age" : 34,
    "eligibal" : True
}

print(Dic)
# print(Dic['Arbaz5']) #TODO: this wil raise error if key not present
print(Dic.get('Arbaz5')) #TODO: This will not
print(Dic.keys())
print(Dic.values())
for key in Dic.keys():
    print(f"The value of key corespondes to {key} is {Dic[key]}")
print(Dic.items())
for key, value in Dic.items():
    print(f"The value of key corespondes to {key} is {value}")
