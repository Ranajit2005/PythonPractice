def check(user,ch):
    return user.lower().rfind(ch.lower())


user = input("Enter your string : ")
ch = "Emma"
print("Emma is found at position : ",check(user,ch))