li=[]
while(1):
    a = input("Give the value :")
    if a == 'q':
        break
    else:
        li.append(int(a))
x= sum(li)/len(li)
print(x)