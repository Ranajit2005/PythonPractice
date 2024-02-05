item = int(input("Give the numbet of the items : "))

if item<10:
    print("Your total cost is : ",item*120)
if item>10 and item<90:
    print("Your total cost is : ",item*100)
if item>90:
    print("Your total cost is : ",item*70)