import os


def genfile(filename, directory):
    # os.system('pwd')
    # os.system(f'ls -al')
    os.system(f'ls -al {directory} > {filename}')


def delfile(filename):
    os.system(f'rm -rf {filename}')


def getData(filename):
    with open(filename, 'r') as file:
        listfile = file.readlines()
        filenames = []
        for i in range(0, len(listfile)-1):
            splitline = listfile[i].split(' ')
            filenames.append(splitline[len(splitline)-1])
        # totalitems = listfile[0].split(' ')[1]
        # print('Total items : ' + totalitems)
        
        #print(filenames)
        filenames.remove(filenames[0])
        filenames.remove('.\n')
        filenames.remove('..\n')
        filexts = []
        for i in range(0, len(filenames)-1):
            if filenames[i][0] == '.':
                filenames.remove(filenames[i])
            filenames[i] = filenames[i][0:-1]
            dot = len(filenames[i]) - filenames[i].find('.')
            filexts.append(filenames[i][-dot:])
            print(i, filenames[i])

        #print("Files : ", filenames)
        #print(filexts)

        extsfreq = {}
        for i in filexts:
            if i in extsfreq.keys():
                extsfreq[i] += 1
            else:
                extsfreq[i] = 1

        print("File types :", extsfreq)


dir = input('Enter directory : ')
savefile = input('Save output to file Y/N ? : ')
if savefile.upper() == 'Y':
    lsfile = input('Enter filename to save : ')
    genfile(lsfile, dir)
    getData(lsfile)
else: 
    lsfile = 'lsfile.txt'
    genfile(lsfile, dir)
    getData(lsfile)
    delfile(lsfile)

