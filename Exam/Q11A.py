def isPrime(num):
    if(num < 1):
        return 0
    i = 2
    while(i<=num/2):
        if num%i == 0:
            return 0
            break
        i = i+1
    return 1

def isPlai(num):
    s = str(num)
    if s==s[::-1]:
        return 1
    else :
        return 0

n = int(input("Give range : "))
# a = isPrime(n)
# print(a)
# b = isPlai(n)
# print(b)
for i in range(2,n):
    if isPrime(i) and isPlai(i):
        print(i)
