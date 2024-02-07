n = int(input("Give range : "))

for i in range(0,n+2):
    for j in range(1,i):
        print(chr(j+64),end="")
    print()