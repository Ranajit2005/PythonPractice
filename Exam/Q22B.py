L = []
M = []
N = []
n = int(input("Give the size : "))
for i in range(0,n):
    a = int(input("Give element of 1st list : "))
    L.append(a)
for i in range(0,n):
    a = int(input("Give element of 2nd list : "))
    M.append(a)
for i in range(0,n):
    N.append(L[i]+M[i])

print(L,M,N)