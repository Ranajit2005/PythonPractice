n = int(input("Give size : "))
li=[]
for i in range(0,n):
    a = int(input("Give element : "))
    li.append(a)
# print(li)
new=[]
for j in li:
    if j not in new:
        new.append(j)
print(new)