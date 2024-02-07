def isPrime(num):
    i = 2
    while(i<=num/2):
        if num%i == 0:
            return 0
            # break
        i = i+1
    print(num)
    return 1

n = int(input("Give the number : "))
for i in range(2,n):
    if(n%i == 0):
        isPrime(i)