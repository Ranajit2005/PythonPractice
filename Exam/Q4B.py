user = input("Give your string : ")
new = ''
for char in user:
    if char not in new:
        new = new + char
print("The new string : ",new)