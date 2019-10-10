#==========================================================================
# PROGRAM PURPOSE:... Exam2, test programming ability since Objects
# AUTHOR:............ Last, First
# COURSE:............ CSC 131-004
# TERM:.............. Fall 2017
# COLLABORATION:..... None
# WORK TIME(h:mm):... 1:30
#==========================================================================
import sys
import random
import Dierbach_BBmod as DB
score = 0

#==========================================================================
# q1 - modify the file Dierbach_BBmod.py
#    - requirements are in the header of that file
#    - you do NOT need to create/modify anything in this file for q1
#==========================================================================
#==========================================================================
# q2 - create a function unmixLimericks() to meet the conditions below:
#    - add a docstring
#    - accept 1 string parameter; the name of a file
#    - use exception handling techniques to attempt to open the filename
#      provided, if it does not exist, return False
#    - if the file does open, you may assume it contains 2 Limericks each
#      of 5 lines that have been interleved.  The odd numbered lines are
#      one limerick and the even numbered lines are another.
#      You may inspect "TwoMixedLimericks.txt" - do NOT alter it.
#    - read the limericks from the file
#    - count all the vowels (aeiou) in both limericks
#    --- count in a non-case-sensitive way (e.g. 'A' and 'a' are the same)
#    - write out the 2 limericks to a file called "TwoLimericks.txt" with
#      a blank line between them; maintain original letter case and
#      punctuation (i.e. exactly like "TwoLimericks_ex.txt")
#    - return a dict w/ {vowel : count} for the total of both limericks
#    --- e.g. {'a':1,'e':2,'i':3,'o':4,'u':5}
#==========================================================================
from itertools import zip_longest as zip2
import collections

def unmixLimericks(fname):
    '''docstring for q2'''

    vow = 'aeiou'
    count = 0
    lists = [[], []]
    limerickDict = {}
    
    try:
        file = open(fname, 'r')
        wfile = open('TwoLimericks.txt', 'w')
        
    except:
        return False
    
    for i,line in enumerate(file):
        lists[i%2].append(line.strip())

    wfile.write(lists[0][0])
    wfile.close()
    wfile = open('TwoLimericks.txt', 'a')
    wfile.write('\n')
    wfile.write(lists[0][1])
    wfile.write('\n')
    wfile.write(lists[0][2])
    wfile.write('\n')
    wfile.write(lists[0][3])
    wfile.write('\n')
    wfile.write(lists[0][4])
    wfile.write('\n')
    wfile.write('\n')    
    wfile.write(lists[1][0])
    wfile.write('\n')
    wfile.write(lists[1][1])
    wfile.write('\n')
    wfile.write(lists[1][2])
    wfile.write('\n')
    wfile.write(lists[1][3])
    wfile.write('\n')
    wfile.write(lists[1][4])

    file.close()
    wfile.close()

    rfile = open('TwoLimericks.txt', 'r')
    Ltext = rfile.read()

    for k in range(0,5):
             limerickDict[vow[k]] = Ltext.lower().count(vow[k])

    return(limerickDict)

    Ltext.close()
#==========================================================================
# q3 - create a function recursivePowerOf2() to meet the conditions below:
#    - add a docstring
#    - accept 1 integer parameter; an exponent
#    - calculate 2 raised to the exponent argument
#    - you must only use recursion and addition to arrive at the answer
#    - return the result
#==========================================================================
def recursivePowerOf2(p):
    '''docstring for q3'''
    if p == 0:
        return 1
    if p == 1:
        return 2
    return recursivePowerOf2(p-1) + recursivePowerOf2(p-1)  

#==========================================================================
# *************************************************************************
# ******************* DO NOT EDIT CODE BELOW THIS POINT *******************
# *************************************************************************
#==========================================================================
def printErr():
    print(" ",sys.exc_info()[0].__name__,"-line",sys.exc_info()[-1].tb_lineno)
    print(" ",sys.exc_info()[1])

# q1 - startItUp()
try:
    print("\nq1:  Checking startItUp() from Dierbach_BBmod")
    DB.startItUp()
    print("startItUp() might be ok... no way to auto-know")
    score += 10
    if DB.__doc__ is None:
        print(" **No docstring for Dierbach_BBmod.py")
    else:
        print('   docstring for Dierbach_BBmodp.py: "' +
              DB.__doc__ + '"')
        score += 2
except:
    print("**Something is wrong with startItUp()")
    printErr()
    score += 2

# q2 - unmixLimericks()
try:
    print("\nq2:  Checking unmixLimericks(badFileName.txt)")
    ra = unmixLimericks("badFileName.txt")
    if ra == False:
        print("Good!  You successfully handled a bad file name.")
        score += 4
    else:
        print("Hmmm.  The function returned an unexpected value.")

    print("\nq2:  Checking unmixLimericks(TwoMixedLimericks.txt)")
    ra = unmixLimericks("TwoMixedLimericks.txt")
    ds = {'a': 17, 'e': 39, 'i': 15, 'o': 16, 'u': 6}
    if ra == ds:
        print("Nice.  Expected dictionary was returned.")
        score += 10
    else:
        print("Function returned an incorrect value.")
        print("Expected:",ds)
        print("Received:",ra)
        score += 5

    if unmixLimericks.__doc__ is None:
        print(" **No docstring for unmixLimericks()")
    else:
        print('   docstring for unmixLimericks(): "' +
              unmixLimericks.__doc__ + '"')
        score += 2

    try:
        fp1 = open("TwoLimericks_ex.txt",'r')
        c1 = fp1.read()
        fp1.close()
        fp2 = open("TwoLimericks.txt",'r')
        c2 = fp2.read()
        fp2.close()
        if c1 == c2:
            print("TwoLimericks.txt appears to be correct.")
            score += 10
        else:
            print("TwoLimericks.txt appears to be incorrect.")
            score += 5
    except:
        print("TwoLimericks.txt does not seem to exist.")

except:
    print("**Something is wrong with unmixLimericks()")
    printErr()
    score += 2


# q3 - recursivePowerOf2()
e = random.randint(0,5)
try:
    print("\nq3:  Checking recursivePowerOf2(" + str(e) + ")")
    p2 = recursivePowerOf2(e)
    if p2 == (2**e):
        print("Nice - recursivePowerOf2() returns the correct value:",p2)
        score += 5
    else:
        print("recursivePowerOf2() does NOT return the correct value")
        print("Expected: ",(2**e))
        print("Returned: ",p2)
        score += 2.5

    e = random.randint(6,11)
    print("\nq3:  Checking recursivePowerOf2(" + str(e) + ")")
    p2 = recursivePowerOf2(e)
    if p2 == (2**e):
        print("Nice - recursivePowerOf2() returns the correct value:",p2)
        score += 5
    else:
        print("recursivePowerOf2() does NOT return the correct value")
        print("Expected: ",(2**e))
        print("Returned: ",p2)
        score += 2.5

    if recursivePowerOf2.__doc__ is None:
        print(" **No docstring for recursivePowerOf2()")
    else:
        print('   docstring for recursivePowerOf2(): "' +
              recursivePowerOf2.__doc__ + '"')
        score += 2
except:
    print("**Something is wrong with recursivePowerOf2()")
    printErr()
    score += 2
    

print("\nProgam complete...\n")
print("Estimated highest potential score is: ",score,"/ 50\n")
#END
