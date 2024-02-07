n = int(input("Give the nth number : "))
sum = 0
for i in range(0,n):
    a = 2
    b = 9
    if i%2 == 0:
        # ch = '-'
        sum = sum - (a+(i*3))/(b+(i*4))
        # print((a+(i*3)),"/",(b+(i*4)),ch,end="")

    else:
        # ch = '+'
        sum = sum + (a+(i*3))/(b+(i*4))
        # print((a+(i*3)),"/",(b+(i*4)),ch,end="")
print()
print(sum)
