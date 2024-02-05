def check(user):
    # for ch in user:
    #     if ch != '0' or ch != '1':
    #         return 0
    # return 1
    return all((letter in '01')for letter in user)

user = input("Give a string : ")
a = check(user)
print(a)
