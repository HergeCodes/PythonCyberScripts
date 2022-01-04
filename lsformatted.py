import os


def genfile(filename, dir):
    os.system(f'ls -A {dir} > {filename}')


def rmfile(filename):
    os.system(f'rm -rf {filename}')


def getfilext(filename):
    dot = filename.find('.')
    if dot == -1:
        return -1
    if dot == 0:
        return -2
    else:
        dot = len(filename) - dot
        return filename[-dot:]


def basicfreq(array):
    freqarr = {}
    for i in array:
        if i in freqarr.keys():
            freqarr[i] += 1
        else:
            freqarr[i] = 1

    return freqarr


def printlist(array, sepchar):
    stringlist = ''
    for i in range(len(array)):
        newline = array[i].find('\n')
        if newline != -1:
            if i == len(array)-1:
                stringlist += array[i][:-1]
            else:
                stringlist += array[i][:-1] + sepchar

    return stringlist


def removelist(x, oldlist):
    newlist = []
    for i in range(len(oldlist)):
        if oldlist[i] != x:
            newlist.append(oldlist[i])

    return newlist


def moreinfo(filename, savefile):
    os.system(f'file {filename} > {savefile}')
    stringreturn = ''
    with open(savefile, 'r') as file:
        listlines = file.readlines()
        # print(listlines)
        for i in range(len(listlines)):
            newline = listlines[i].find('\n')
            if newline != -1:
                # print(i, listlines[i][:-1])
                colon = len(listlines[0]) - 2 - listlines[0].find(':')
                stringreturn = listlines[0][-colon:]

                return f'{filename} : {stringreturn}'

        return


# print(moreinfo('encryption1.py', 'info.txt'))
# listfiles = ['encryption1.py\n', 'lsformatted.py']
# for i in listfiles:
#     print(moreinfo(i, 'info.txt'))
# listfiles = ['encryption1.py\n', '.idea\n', 'info.txt\n', 'keyfile.txt\n', 'ls-altocsv.py\n', 'lsfile2.txt\n', 'lsformatted.py\n', 'neofetch.py\n', 'neo.txt\n', 'ordtest.py\n', 'passwordgenerator.py\n', 'password.txt\n', 'test.txt\n', 'venv\n']
# for i in range(len(listfiles)):
#     if moreinfo(listfiles[i], 'info.txt') == None:
#         continue
#     else:
#         print(i, moreinfo(listfiles[i], 'info.txt'))


def getdata(filename):
    with open(filename, 'r') as file:
        listfile = file.readlines()
        #print(listfile)
        #lists
        filexts = []
        dirs = []
        hidden = []
        # print(listfile)
        for i in range(len(listfile)):
            # print(i, listfile[i])
            filext = getfilext(listfile[i])
            if filext == -1:
                dirs.append(listfile[i])
            elif filext == -2:
                hidden.append(listfile[i])
            filexts.append(filext)

        filexts = removelist(-1, filexts)
        filexts = removelist(-2, filexts)
        # remove '\n'
        for i in range(len(filexts)):
            filexts[i] = filexts[i][:-1]

        sep1 = '\n'
        sep2 = ' '
        print(f'ls -al : {printlist(listfile, sep1)}')
        # more info
        for i in range(len(listfile)):
            if moreinfo(listfile[i], 'info.txt') == None:
                continue
            else:
                print(moreinfo(listfile[i], 'info.txt'))
        print(f'Directories : {printlist(dirs, sep2)}')
        print(f'Hidden Files : {printlist(hidden, sep2)}')
        print(f'File Types : {basicfreq(filexts)}')


directory = input('Enter directory : ') # '/home/admin1234/PycharmProjects/CSHWalton'
savefile = input('Save output to file ? Y/N : ')
if savefile.upper() == 'Y':
    filename = input('Enter filename to save : ')
    genfile(filename, directory)
    getdata(filename)
else:
    filename = 'lsfile2.txt'
    genfile(filename, directory)
    getdata(filename)
    rmfile(filename)
