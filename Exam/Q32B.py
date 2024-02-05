def ugly(n):
    if n == 1:
        return 1
    elif n<=0:
        return 0
    elif n%2 == 0:
        return ugly(n//2)
    elif n%3 == 0:
        return ugly(n//3)
    elif n%5 == 0:
        return ugly(n//5)
    else:
        return 0
    
n = int(input("Give the number : "))
a = ugly(n)
print(a)