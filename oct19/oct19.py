##ifile = open("KublaKhan.txt",'r')
##ifile.close()

##fname = input("File name: ")
##ifile = open(fname,'r')
##line = ifile.readline()
##while line != '':
##    print(line)
##    line = ifile.readline()
##ifile.close()

##fname = input("File name: ")
##ifile = open(fname,'r')
##line = ifile.readline()
##while line != '':
##    print(line.count('a'),line)
##    line = ifile.readline()
##ifile.close()

##fname = input("File name: ")
##ifile = open(fname,'r')
##line = ifile.readline()
##while line != '':
##    line = line.lower()
##    line = line.strip('\n')
##    print(line.count('a'),line)
##    line = ifile.readline()
##ifile.close()

fname = input("File name: ")
ifile = open(fname,'r')
line = ifile.readline()
while line != '':
    line = line.lower()
    line = line.strip('\n')
    eline = ''
    for c in line:
        if ord(c) < 97 or ord(c) > 122:
            eline = eline + c
        else:
            eline += chr(((ord(c)-94)%26)+97)
    print(line)
    print(eline)
    line = ifile.readline()
ifile.close()
