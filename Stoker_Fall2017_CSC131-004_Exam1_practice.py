#=========================================================================#
# *********************************************************************** #
# ************************** PRACTICE EXAM 1 **************************** #
# *********************************************************************** #
#=========================================================================#

#==========================================================================
# PROGRAM PURPOSE:... Exam1, test programming ability thus far in CSC 131
# AUTHOR:............ Last, First
# COURSE:............ CSC 131-004
# TERM:.............. Fall 2017
# COLLABORATION:..... None
# WORK TIME(h:mm):... 1:30
#==========================================================================
import sys
import random
from operator import itemgetter
score = 0

#==========================================================================
# q1 - modify familiarStart() to meet the conditions below
#    - request the user input an integer >0 and <=500
#    - if the input does not meet conditions, prompt for input until it does
#    - if integer is even, print "Even"
#    - if integer is odd, print "Odd"
#    - there is no return value for this function
#==========================================================================
def familiarStart():    
    try:
        userInput = int(input("Please enter an integer greater than 0 and less than or equal to 500: "))
        if userInput in range(1, 501):
            if (userInput % 2) == 0:
                print("{} is even.".format(userInput))
            else:
                print("{} is odd.".format(userInput))
        else:
            raise ValueError         
                
    except ValueError:
        print("INVAlID INPUT")
        familiarStart()
       

#==========================================================================
# q2 - modify powerOfTwo() to meet the conditions below
#    - accept 1 integer parameter; an exponent
#    - print to the screen 2 raised to the exponent argument, example:
#    --- "2 to the power of 2 is 4"
#    - also return the result (for the example, you would return 4)
#==========================================================================
def powerOfTwo(p2):
    try:
        print("2 to the power of {} is {}".format(p2, 2**p2))
        return 2**p2
    
    except ValueError:
        print("I said an integer!")
        powerOfTwo()

#==========================================================================
# q3 - modify equal3() to meet the conditions below
#    - accept 3 integer parameters
#    - return True if all 3 are equal; False if otherwise 
#==========================================================================
def equal3(a, b, c):   
    if a == b == c:        
        return True
    else:
        return False

#==========================================================================
# q4 - modify capsNoVowels() to meet the conditions below
#    - accept 1 string parameter where all letters are lowercase
#    - modify the string as follows: 
#    --- remove all vowels ('a', 'e', 'i', 'o', 'u')
#    --- change remaining letters to UPPERCASE
#    --- leave spaces alone
#    --- example:  "the dog barks" becomes "TH DG BRKS"
#    - return the resultant string
#==========================================================================
def capsNoVowels(s):
    vow = ('a', 'e', 'i', 'o', 'u')
    result = []
    
    for i in s:
        if i not in vow:
            result.append(i)

    return "".join(result).upper()


#==========================================================================
# q5 - modify gradeAvg() to meet the conditions below
#    - accept 2 parameters (both are *equal lenth* lists)
#    - student list is argument 1; list of strings, example:
#    - ["Jo", "Ji", "Ja"]
#    - grades list is argument 2; list of lists of 3 floats, example:
#    --- [[1,2.5,3],[4.5,5,6],[7,8,9]]
#    - student names correspond to 3 grades by list position, example:
#    - Jo's grades are [1,2.5,3]; Ja's grades are [7,8,9]
#    - create a new list w/ 2 items, grade average and student name
#    - print name/avg sorted by avg (hi to lo), example:
#    --- "Ja/8"
#        "Ji/5.17"
#    - there is no return value for this function
#==========================================================================
def gradeAvg(stu, gra):
    avgGrades = [sum(x) / len(x) for x in gra]
    combined = list(zip(stu, avgGrades))
    combined.sort(key=itemgetter(1), reverse=True)
    for y, z in combined:
            print("{}/{}".format(y, int(z)))

##def gradeAvg(stu,gra):
##    print("In gradeAvg()")
##    nL = []
##    x = 0
##    while x < len(stu):
##        avg = int((gra[x][0]+gra[x][1]+gra[x][2])/3)
##        nL.append([avg,stu[x]])
##        x += 1
##
##    nL.sort(reverse=True)
##
##    for r in nL:
##        print(r[1]+"/"+str(r[0]))

#==========================================================================
# *************************************************************************
# ******************* DO NOT EDIT CODE BELOW THIS POINT *******************
# *************************************************************************
#==========================================================================

def printErr():
    print(" ",sys.exc_info()[0].__name__,"-line",sys.exc_info()[-1].tb_lineno)
    print(" ",sys.exc_info()[1])

def e3(L3):
    if L3[0] == L3[1]:
        if L3[1] == L3[2]:
            return True
    return False

print("*************************************************************")
print("********************* PRACTICE EXAM 1 ***********************")
print("*************************************************************")

# q1 - familiarStart()
try:
    print("\nq1:  Checking familiarStart()")
    familiarStart()
    print("familiarStart() might be ok... no way to auto-know")
    score += 12
except:
    print("**Something is wrong with familiarStart()")
    printErr()


# q2 - powerOfTwo(e)
e = random.randint(3,22)
try:
    print("\nq2:  Checking powerOfTwo(" + str(e) + ")")
    p2 = powerOfTwo(e)
    if p2 == (2 ** e):
        print("Good job! powerOfTwo() returns the correct value")
        score += 12
    else:
        print("Hmmm - powerOfTwo() does NOT return the correct value")
        print("Expected: ",2**e)
        print("Returned: ",p2)
        score += 5
except:
    print("**Something is wrong with powerOfTwo()")
    printErr()
    score += 2


# q3 - equal3(x,y,z)
LL = [0,0,0]
LL[0] = random.randint(1,3)
LL[1] = random.randint(1,3)
LL[2] = random.randint(1,3)
try:
    print("\nq3:  Checking equal3(" + str(LL[0]) + "," + str(LL[1]) + ","
          + str(LL[2]) + ")")
    L = equal3(LL[0],LL[1],LL[2])
    if L == e3(LL):
        print("Nice - equal3() returns the correct value [test1]")
        print("q3:  Checking equal3(17,17,17)")
        L = equal3(17,17,17)
        if L:
            print("Nice, again - equal3() returns the correct value [test2]")
            score += 12
        else:
            print("Strange... equal3() does NOT return the correct value [test2]")
            score += 8
    else:
        print("equal3() does NOT return the correct value [test1]")
        print("Expected: ",e3(LL))
        print("Returned: ",L)
        score += 5
except:
    print("**Something is wrong with equal3()")
    printErr()
    score += 2
    

# q4 - capsNoVowels(s)
w1 = ("my", "her", "his", "our")
w2 = ("dad", "mom", "dog", "cat")
w3 = ("runs", "swims", "sings", "jumps")
w4 = ("quite", "very", "quite", "very")
w5 = ("slowly", "quickly", "loudly", "softly")
s = w1[random.randint(0,3)] + ' '
s = s + w2[random.randint(0,3)] + ' '
s = s + w3[random.randint(0,3)] + ' '
s = s + w4[random.randint(0,3)] + ' '
s = s + w5[random.randint(0,3)]
try:
    print("\nq4:  Checking capsNoVowels(" + s + ")")
    sL = ''.join([c for c in s if ord(c) not in (97,101,105,111,117)])
    sL = ''.join([chr(ord(c)-32) if ord(c) != 32 else c for c in sL ])
    sO = capsNoVowels(s)
    if sO == sL:
        print("Great!  capsNoVowels() returns the correct value")
        print("Expected: ",sL)
        print("Returned: ",sO)
        score += 12
    else:
        print("Not quite -- capsNoVowels() does NOT return the correct value")
        print("Expected: ",sL)
        print("Returned: ",sO)
        score += 8
except:
    print("**Something is wrong with capsNoVowels()")
    printErr()
    score += 2


# q5 - gradeAvg(studetns,grades)
students = ["Zaylee", "Ellis", "Mariyah", "Natalee", "Denise", "Janiya",
            "Sariyah", "Ophelia", "Rhea", "Libby", "Frankie", "Kimora", "Abril",
            "Giavanna", "Hadleigh", "Ingrid", "Princess", "Charlize", "Taya"]
grades = [[90.5,81,71.5], [88,76,64], [97.5,95,92.5], [96,92,88], [88.5,77,65.5],
          [82.5,65,47.5], [93,86,79], [95,90,85], [93.5,87,80.5], [98,96,94],
          [87.5,75,62.5], [99,98,97], [90,80,70], [87,74,61], [85.5,71,56.5],
          [84.5,69,53.5], [94.5,89,83.5], [89.5,79,68.5], [92,84,76]]

try:
    print("\nq5:  Checking gradeAvg([list] of students, [list] of grades)")
    gradeAvg(students,grades)
    print("\ngradeAvg() might be ok... no way to auto-know; expected output:")
    print("Kimora/98")
    print("Libby/96")
    print("Mariyah/95")
    print("Natalee/92")
    print("Ophelia/90")
    print("Princess/89")
    print("Rhea/87")
    print("Sariyah/86")
    print("Taya/84")
    print("Zaylee/81")
    print("Abril/80")
    print("Charlize/79")
    print("Denise/77")
    print("Ellis/76")
    print("Frankie/75")
    print("Giavanna/74")
    print("Hadleigh/71")
    print("Ingrid/69")
    print("Janiya/65")
    score += 12
except:
    print("**Something is wrong with gradeAvg()")
    printErr()
    score += 2


print("\nProgam complete...\n")
print("Estimated highest potential PRACTICE score is: ",score,"/ 60\n")
print("*************************************************************")
print("********************* PRACTICE EXAM 1 ***********************")
print("*************************************************************")
#END
