import os


def genfile(filename):
    os.system(f'neofetch > {filename}')


genfile('neo.txt')


def getmem(filename):
    with open(filename, 'r') as file:
        listfile = file.readlines()
        # for i in range(0, len(listfile)-1):
        #     print(i, listfile[i] + '\n')

        print(listfile[36])


getmem('neo.txt')
