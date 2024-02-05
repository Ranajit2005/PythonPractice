def cube(num):
    return num**3

li = []
n = int(input("Give the size : "))
for i in range(0,n):
    a = int(input("Give element : "))
    li.append(a)
list1 = list(map(cube,li))
print(list1)
print("Max : ",max(list1))
print("Min : ",min(list1))