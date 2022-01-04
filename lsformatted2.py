import os


def genfile(filename, directory):
    os.system(f'ls -A {directory} > {filename}')


def rmfile(filename):
    os.system(f'rm -rf {filename}')


def basicfreq(array):
    freqarr = {}
    for i in array:
        if i in freqarr.keys():
            freqarr[i] += 1
        else:
            freqarr[i] = 1

    return freqarr


def removelist(x, oldlist):
    newlist = []
    for i in oldlist:
        if i != x:
            newlist.append(i)

    return newlist


def removenewlines(string):
    newline = string.find('\n')
    if newline == -1:
        return string
    else:
        return string[:-1]


def fileinfo(filename):
    savefile = 'fileinfo.txt'
    os.system(f'file {filename} > {savefile}')
    with open(savefile, 'r') as file:
        text = file.readline()
        colon = len(text)-2 - text.find(':')

    return text[-colon:]

# x = fileinfo('lsformatted2.')
# print(x)


def formatdata(filename):
    noitems = 0
    dirs = []
    hiddens = []
    info = []
    with open(filename, 'r') as file:
        readlines = file.readlines()
        #print(readlines)
        noitems = len(readlines)
        for i in range(len(readlines)):
            readlines[i] = removenewlines(readlines[i])
            # print('test statement')
            info.append(fileinfo(readlines[i]))
            # print(fileinfo(readlines[i]))

    for i in range(len(info)):
        info[i] = removenewlines(info[i])
    # print(info)
    fileinfofreq = basicfreq(info)

    return fileinfofreq, noitems


genfile('lsresults.txt', '/home/admin1234/PycharmProjects/cybsecscripting')
print(formatdata('lsresults.txt'))

# directory = input("Enter directory : ")
# savefile = input("Save output to file ? Y/N : ")
# if savefile.upper() == 'Y':
#     filename = input("Enter filename to save : ")
#     genfile(filename, directory)

# TODO : change directory of fileinfo function