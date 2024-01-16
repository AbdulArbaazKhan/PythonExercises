lst = [2, 34, 56, 6, 455, 43, 5, 6, 23, 4, 3, 4, 3, 2, 5]

# lst.append("Added an item after last item")
lst.sort()  # Ascending
lst.sort(reverse=True) # decending
print(lst)

m = lst #TODO: here, m is a reference of lst
m[0]=100
print(lst)

m = lst.copy() #TODO: here, m is a reference of lst
m[0]=200


lst.insert(0, 400) #here, 0 is index and 400 is the value to insert before that index

new = [50, 30, 20]
# lst.extend(new)
k = m+lst
print(k)