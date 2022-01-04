import random


def genpass(x):
    passlist = [''] * x
    lowerchars = 'abcdefghijklmnopqrstuvwxyz'
    upperchars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    chars = '!@#$%^&*()_+-='
    for i in range(len(passlist)):
        if i % 4 == 0:
            passlist[i] = str(random.randint(0, 9))
        elif i % 3 == 0:
            passlist[i] = chars[random.randint(0, len(chars)-1)]
        elif i % 2 == 0:
            passlist[i] = upperchars[random.randint(0, 25)]
        elif i % 1 == 0:
            passlist[i] = lowerchars[random.randint(0, 25)]

    random.shuffle(passlist)
    
    return passlist, len(passlist)


def listtostring(list):
    string = ''
    for i in list:
        string += str(i)
    
    return string


length = int(input("Enter password length : "))
listpass, x = genpass(length)
passwd = listtostring(listpass)
# print(listpass)
print(passwd)

