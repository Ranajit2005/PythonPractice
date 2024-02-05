n = int(input("Give nunber : "))
for i in range(1,n):
    for j in range(n-i):
        print(" ",end="")
    for k in range(1,i+1):
        print(k," ",end="")
    print()
for i in range(n,0,-1):
    for j in range(n-i):
        print("  ",end="")
    for k in range(1,i+1):
        print(k," ",end="")
    print()