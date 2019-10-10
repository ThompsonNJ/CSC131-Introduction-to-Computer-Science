myDict = {}
ifile = open('5char.txt','r')
line = ifile.readline()
count = 0
while line != '':
    line = ifile.readline()
    sline = sorted(line)
    sline = ''.join(sline)
    
    if sline in myDict:
        myDict[sline].add(line)
    else:
        myDict[sline] = set()
        myDict[sline].add(line)

for i in myDict:
    if len(myDict[i]) >= 8:
        print(myDict[i])
        count += 1
        
print('There are {} anagram groups greater than or equal to eight.'.format(count))    

ifile.close()
