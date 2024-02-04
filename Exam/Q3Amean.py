def mean(li):
    return sum(li)/len(li)



# def main() :
n = int(input("Give thye size of the array : "))
li=[]
for i in range(0,n) :
    a = float(input("Give the element : "))
    li.append(a)
a = mean(li)
print(li)
print("The mean is : ",a)