string = "Hey, My name is {} and I am from {}"

name = "Arbaz"
country = "Pakistan"
print(string.format(name, country))
string2 = "Hey, My name is {1} and I am from {0}"

print(string2.format(country, name ))
print(f"Hey, My name is {name} and I am from {country}")

# txt = "For only {price:.2f} dollars!"
# print(txt.format(price=80.86776))
price=80.86776
txt = f"For only {price:.2f} dollars!"
print(txt)


print(f"Hey, My name is {{name}} and I am from {{country}}")