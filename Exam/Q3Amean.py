def mean(li):
    return sum(li)/len(li)

def meadian(li):
    Sortli = sorted(li)
    n = len(li)
    mid = n//2
    if n%2 == 0:
        return (Sortli[mid]+Sortli[mid-1])/2
    else:
        return Sortli[mid]

# def main() :
n = int(input("Give thye size of the array : "))
li=[]
for i in range(0,n) :
    a = float(input("Give the element : "))
    li.append(a)
a = mean(li)
print(li)
print("The mean is : ",a)