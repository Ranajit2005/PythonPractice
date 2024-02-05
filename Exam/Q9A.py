li = []
n = int(input("Give the size : "))
for i in range(0,n):
    a = int(input("Give element : "))
    li.append(a)
print(li)
val = li[4]
li[2] = li[4]
li.append(val)
print(li)