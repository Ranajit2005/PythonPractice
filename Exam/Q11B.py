n = int(input("Give range : "))

for i in range(0,n):
    for j in range(1,i):
        print(chr(j+64),end="")
    print()