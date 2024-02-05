import numpy as np
print("Matrix is 3 * 3")
l=[]
for i in range(0,3):
    l.append([])
for i in range(0,3):
    for j in range(0,3):
        a = int(input("Give the ele of 1st matrix : "))
        l[i].append(a)
# print(l)
arr1 = np.array(l)

m=[]
for i in range(0,3):
    m.append([])
for i in range(0,3):
    for j in range(0,3):
        a = int(input("Give the ele of 2nd matrix : "))
        m[i].append(a)
# print(l)
arr2 = np.array(m)
print(arr1)
print()
print(arr2)
print()
arr3 = arr1+arr2
print(arr3)
print()
arr4 = arr1*arr2
print(arr4)