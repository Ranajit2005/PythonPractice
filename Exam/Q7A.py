a = int(input("Give 1st side : "))
b = int(input("Give 2nd side : "))
c = int(input("Give 3rd side : "))

if a+b>c or b+c>a or c+a>b:
    if(a==b==c):
        print("Eqa")
    elif(a==b or b==c or c==a):
        print("Iso")
    else:
        print("Sca")
else:
    print("Not valid")