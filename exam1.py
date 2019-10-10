import sys
import random
score = 0

#==========================================================================
# q1 - modify familiarStart() to meet the conditions below
#    - request the user input an integer >0 and <=100
#    - if the input does not meet conditions, prompt for input until it does
#    - if integer is in the range 1-50 print "Lower half"
#    - if integer is in the range 51-100 print "Upper half", examples:
#    --- user inputs 51, output to the screen is "Upper half"
#    --- user inputs 17, output to the screen is "Lower half"
#    - there is no return value for this function
#==========================================================================
def familiarStart():
    try:
        userInput = int(input("Please enter an integer greater than 0 and less than or equal to 100: "))
    
        if userInput in range(1, 51):
            print("Lower half")
        elif userInput in range(51, 101):
            print("Upper half")
        else:
            raise ValueError         
            
    except ValueError:
        print("INVAlID INPUT")
        familiarStart()


#==========================================================================
# q2 - modify powerUp() to meet the conditions below
#    - accept 2 integer parameters; a base and an exponent
#    - base is argument 1 and exponent is argument 2
#    - print information to the screen, example:
#    --- "10 to the power of 5 is 100000"
#    - also return the result (for the example, you would return 100000)
#==========================================================================
def powerUp(a, b):
    print("{} to the power of {} is {}".format(a, b, a**b))

    return a**b

#==========================================================================
# q3 - modify largest() to meet the conditions below
#    - accept 3 integer parameters
#    - return the largest of the 3 
#==========================================================================
def largest(c, d, e):
    return max(c, d, e)

#==========================================================================
# q4 - modify capitalizeVowels() to meet the conditions below
#    - accept 1 string parameter where all letters are lowercase
#    - iterate over the string and change all vowels to UPPERCASE, example:
#    --- "the dog barks" becomes "thE dOg bArks"
#    - vowels are 'a', 'e', 'i', 'o', 'u'
#    - return the string w/ UPPERCASE vowels
#==========================================================================
def capitalizeVowels(f):
    try:
        from string import maketrans

    except ImportError:
        maketrans = str.maketrans

    vow = 'aeiou'
    upperMap = maketrans(vow, vow.upper())
    mystring = f
    mystring = mystring.translate(upperMap)

    return mystring


#==========================================================================
# q5 - modify stateCapitals() to meet the conditions below
#    - accept 2 parameters (both are *equal length* lists of strings)
#    - capital list is argument 1 and state list is argument 2
#    - sort capital list reverse-alphabetically
#    - sort state list alphabetically
#    - iterate over both sorted lists and print matching capital/state, example:
#    --- "Sacremento/California"
#        "Lansing/Michigan"
#    - there is no return value for this function
#==========================================================================
def stateCapitals(cap, st):
    cap.sort(reverse=True)
    st.sort()
    combined = list(zip(cap, st))
    for y, z in combined:
            print("{}/{}".format(y, z))



#==========================================================================
# *************************************************************************
# ******************* DO NOT EDIT CODE BELOW THIS POINT *******************
# *************************************************************************
#==========================================================================

def printErr():
    print(" ",sys.exc_info()[0].__name__,"-line",sys.exc_info()[-1].tb_lineno)
    print(" ",sys.exc_info()[1])

# q1 - familiarStart()
try:
    print("\nq1:  Checking familiarStart()")
    familiarStart()
    print("familiarStart() might be ok... no way to auto-know")
    score += 12
except:
    print("**Something is wrong with familiarStart()")
    printErr()
    score += 2


# q2 - powerUp(b,e)
b = random.randint(5,11)
e = random.randint(2,4)
try:
    print("\nq2:  Checking powerUp(" + str(b) + "," + str(e) + ")")
    pU = powerUp(b,e)
    if pU == b ** e:
        print("Good job1! powerUp() returns the correct value [test1]")
        print("q2:  Checking powerUp(" + str(e) + "," + str(b) + ")")
        pU = powerUp(e,b)
        if pU == e ** b:
            print("Good job2! powerUp() returns the correct value [test2]")
            score += 12
        else:
            print("Strange... powerUp() does NOT return the correct value [test2]")
            print("Expected: ",e**b)
            print("Returned: ",pU)
            score += 8
    else:
        print("Hmmm - powerUp() does NOT return the correct value [test1]")
        print("Expected: ",b**e)
        print("Returned: ",pU)
        score += 5
except:
    print("**Something is wrong with powerUp()")
    printErr()
    score += 2


# q3 - largest(x,y,z)
LL = [0,0,0]
LL[0] = random.randint(1,100)
LL[1] = random.randint(1,100)
LL[2] = random.randint(1,100)
try:
    print("\nq3:  Checking largest(" + str(LL[0]) + "," + str(LL[1]) + ","
          + str(LL[2]) + ")")
    L = largest(LL[0],LL[1],LL[2])
    if L == max(LL):
        print("Nice - largest() returns the correct value [test1]:",L)
        print("q3:  Checking largest(51,17,51)")
        L = largest(51,17,51)
        if L == 51:
            print("Nice, again - largest() returns the correct value [test2]:",L)
            score += 12
        else:
            print("Strange... largest() does NOT return the correct value [test2]")
            print("Expected: ",51)
            print("Returned: ",L)
            score += 8
    else:
        print("largest() does NOT return the correct value [test1]")
        print("Expected: ",max(LL))
        print("Returned: ",L)
        score += 5
except:
    print("**Something is wrong with largest()")
    printErr()
    score += 2
    

# q4 - capitalizeVowels(s)
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
    print("\nq4:  Checking capitalizeVowels(" + s + ")")
    sL = ''.join([chr(ord(c)-32) if ord(c) in (97,101,105,111,117) else c for c in s])
    sO = capitalizeVowels(s)
    if sO == sL:
        print("Great!  capitalizeVowels() returns the correct value")
        print("Expected: ",sL)
        print("Returned: ",sO)
        score += 12
    else:
        print("Not quite -- capitalizeVowels() does NOT return the correct value")
        print("Expected: ",sL)
        print("Returned: ",sO)
        score += 8
except:
    print("**Something is wrong with capitalizeVowels()")
    printErr()
    score += 2


# q5 - stateCapitals(capitals,states)
states = ["Michigan", "Texas", "California", "Mississippi", "NorthDakota"]
capitals = ["Austin", "Sacramento", "Lansing", "Jackson", "Bismarck"]
try:
    print("\nq5:  Checking stateCapitals([list] of capitals, [list] of states)")
    stateCapitals(capitals,states)
    print("\nfamiliarStart() might be ok... no way to auto-know; expected output:")
    print("Sacremento/California")
    print("Lansing/Michigan")
    print("Jackson/Mississippi")
    print("Bismarck/NorthDakota")
    print("Austin/Texas")
    score += 12
except:
    print("**Something is wrong with stateCapitals()")
    printErr()
    score += 2


print("\nProgam complete...\n")
print("Estimated highest potential score is: ",score,"/ 60\n")
#END
