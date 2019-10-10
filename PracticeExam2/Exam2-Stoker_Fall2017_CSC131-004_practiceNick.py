
#=========================================================================#
# *********************************************************************** #
# ************************** PRACTICE EXAM 2 **************************** #
# *********************************************************************** #
#=========================================================================#
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
import Dierbach_BBmodp as DB
score = 0

#==========================================================================
# q1 - modify the file Dierbach_BBmodp.py
#    - requirements are in the header of that file
#    - you do NOT need to create/modify anything in this file for q1
#==========================================================================
#==========================================================================
# q2 - create a function limerickFun() to meet the conditions below:
#    - add a docstring
#    - accept 1 string parameter; the name of a file
#    - use exception handling techniques to attempt to open the filename
#      provided, if it does not exist, return False
#    - if the file does open, you may assume it contains 2 Limericks, each
#      of 5 lines, separated by a line w/ 10 asterisks (i.e. **********)
#      You may inspect "TwoLimericksToMeasure.txt" - do NOT alter it.
#    - read the limericks from the file
#    - count the vowels (aeiou) in each to determine which has more
#    - write the limerick which has more vowels out to the file:
#    --- "LimerickOut.txt"
#    - return a dict w/ {vowel : count} for the limerick w/ the most vowels
#    --- e.g. {'a':1,'e':2,'i':3,'o':4,'u':5}
#==========================================================================
import collections

def limerickFun(fname):
    '''docstring'''
    vows = 'aeiou'
    countTop = 0
    countBot = 0
    textTop = ''
    textBot = ''
    vowDict = {}
    
    try:
        file = open(fname, 'r')
        wfile = open('LimerickOut.txt', 'w')
        text = file.readline()
        
    except:
        return False

    while text != '**********\n':
        for i in text.lower():
            if i in vows:
                countTop += 1
                
        textTop += text               
        text = file.readline()

    if text == '**********\n':
        while text != '':
            for i in text.lower():
                if i in vows:
                    countBot += 1
                    
            textBot += text                    
            text = file.readline()                  

    if countTop > countBot:
        wfile.write(textTop)
        #return countTop
    
    if countTop < countBot:
        wfile.write(textBot)
        #return countBot        
        
    file.close()
    wfile.close()

    rfile = open('LimerickOut.txt', 'r')
    Ltext = rfile.read()

    if Ltext != '':    
        count = collections.Counter(v for v in Ltext.lower() if v in vows)
        return count
    
    Ltext.close()
        
#==========================================================================
# q3 - create a function recursivePowerOf3() to meet the conditions below:
#    - add a docstring
#    - accept 1 integer parameter; an exponent
#    - you must only use recursion and multiplication to arrive at the answer
#    - return the result
#==========================================================================

def recursivePowerOf3(p):
    '''docstring'''
    if p == 0:
        return 1
    if p == 1:
        return 3
    return 3*recursivePowerOf3(p-1)   
    

#==========================================================================
# *************************************************************************
# ******************* DO NOT EDIT CODE BELOW THIS POINT *******************
# *************************************************************************
#==========================================================================

def printErr():
    print(" ",sys.exc_info()[0].__name__,"-line",sys.exc_info()[-1].tb_lineno)
    print(" ",sys.exc_info()[1])

print("*************************************************************")
print("********************* PRACTICE EXAM 2 ***********************")
print("*************************************************************")

# q1 - startItUp()
try:
    print("\nq1:  Checking startItUp() from Dierbach_BBmodp")
    DB.startItUp()
    print("startItUp() might be ok... no way to auto-know")
    score += 10
    if DB.__doc__ is None:
        print("No docstring for Dierbach_BBmodp.py")
    else:
        print("docstring for Dierbach_BBmodp.py")
        print(DB.__doc__)
        score += 2
except:
    print("**Something is wrong with startItUp()")
    printErr()
    score += 2

# q2 - limerickFun()
try:
    print("\nq2:  Checking limerickFun(badFileName.txt)")
    ra = limerickFun("badFileName.txt")
    if ra == False:
        print("Good!  You successfully handled a bad file name.")
        score += 4
    else:
        print("Hmmm.  The function returned an unexpected value.")
        
    ra = limerickFun("TwoLimericksToMeasure.txt")
    ds = {'a': 8, 'e': 18, 'i': 8, 'o': 9, 'u': 5}
    if ra == ds:
        print("Nice.  Expected dictionary was returned.")
        score += 10
    else:
        print("Function returned an incorrect value.")
        print("Expected:",ds)
        print("Received:",ra)

    if limerickFun.__doc__ is None:
        print("No docstring for limerickFun()")
    else:
        print("docstring for limerickFun()")
        print(limerickFun.__doc__)
        score += 2

    try:
        fp1 = open("LimerickOut.txt",'r')
        c1 = fp1.readline().strip('\n')
        fp1.close()
        if c1 == "A dozen, a gross, and a score":
            print("LimerickOut.txt appears to be correct.")
            score += 10
        else:
            print("LimerickOut.txt appears to be incorrect.")
            score += 5
    except:
        print("LimerickOut.txt does not exist.")

except:
    print("**Something is wrong with limerickFun()")
    printErr()
    score += 2


# q3 - recursivePowerOf3()
e = random.randint(0,10)
try:
    print("\nq3:  Checking recursivePowerOf3(" + str(e) + ")")
    p3 = recursivePowerOf3(e)
    if p3 == (3**e):
        print("Nice - recursivePowerOf3() returns the correct value:",p3)
        score += 10
    else:
        print("recursivePowerOf3() does NOT return the correct value")
        print("Expected: ",(3**e))
        print("Returned: ",p3)
        score += 5

    if recursivePowerOf3.__doc__ is None:
        print("No docstring for recursivePowerOf3()")
    else:
        print("docstring for recursivePowerOf3()")
        print(recursivePowerOf3.__doc__)
        score += 2
except:
    print("**Something is wrong with recursivePowerOf3()")
    printErr()
    score += 2
    

print("\nProgam complete...\n")
print("Estimated highest potential score is: ",score,"/ 50\n")
print("*************************************************************")
print("********************* PRACTICE EXAM 2 ***********************")
print("*************************************************************")
#END
