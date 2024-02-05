def fuck(num):
    if num == 1:
        return 1
    else:
        return num*fuck(num-1)

# a = fuck(5)
# print(a)
n = int(input("Give the number : "))
sum = 1
for i in range(1,n):
    a = fuck(i)
    sum = sum + 1/a
print(sum)
