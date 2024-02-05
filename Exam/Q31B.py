n = int(input("Give the renge : "))
li = []
for i in range(1,n+1):
    li.append(chr(96+i)*i)
print(li)