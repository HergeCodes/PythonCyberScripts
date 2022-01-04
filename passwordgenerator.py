import random


def genpass(x, chars, writetofile, filename):
    if chars == '-1':
        chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-='
    passlist = []
    for i in range(0, x):
        randi = random.randint(0, len(chars)-1)
        passlist.append(chars[randi])

    stringpass = ''
    for i in range(len(passlist)):
        stringpass += str(passlist[i])

    if writetofile.upper() == 'Y':
        if filename == '-1':
            file = open('pass.txt', 'w')
        else:
            file = open(filename, 'w')
        file.write(stringpass)
        file.close()
    else:
        print(stringpass)


lenpass = int(input("Enter password length : "))
chars = input("Enter characters string or -1 for default character set : ")
fileYN = input("Write to file ? Y/N : ")
if fileYN.upper() == 'Y':
    filename = input("Filename to write to or -1 for default ('pass.txt') : ")
else:
    filename = '-1'

genpass(lenpass, chars, fileYN, filename)
