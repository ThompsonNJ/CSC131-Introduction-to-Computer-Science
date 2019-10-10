#==========================================================================
# PROGRAM PURPOSE:... C11 Recursion
# AUTHOR:............ Thompson, Nick
# COURSE:............ CSC 131-004
# TERM:.............. Fall 2017
# COLLABORATION:.....                     
# WORK TIME(h:mm):... 2:00
#==========================================================================
'''The purpose of this program is to allow a user to input a lower and upper
limit and a magic number between said limits.
The program will then guess
the magic number.'''

# imports
from copy import deepcopy

# functions
def guessMN(guess, mn, lower, upper):
    '''GuessMN requires four arguments to be passed into it in the following order:
guess, magic number, lower limit, and upper limit. This function uses integer
division to guess the magic number.'''
    if guess == mn:
        print(guess, ": Correct!")
    elif guess < mn:
        print(guess, ": Higher!")
        lower = deepcopy(guess)
        guess = (guess+upper) // 2
        return guessMN(guess, mn, lower, upper)
    elif guess > mn:
        print(guess, ": Lower!")
        upper = deepcopy(guess)
        guess = (lower+guess) // 2
        return guessMN(guess, mn, lower, upper)
    
# input catch
while True:
    try:
        lower = int(input("Please enter the lower limit: "))
        break

    except:
        print("**INVALID ENTRY!")
    
while True:        
    try:
        upper = int(input("Please enter the upper limit: "))
        if upper < lower:
            print("The upper limit must be greater than or equal to the lower limit")
            raise ValueError
        else:
            break
    except:
        print("**INVALID ENTRY!")

while True:
    try:
        print("Please enter the magic number. Your input must be between")
        mn = int(input("or include the lower and upper limits you created: "))
        if mn < lower or mn > upper
            raise ValueError
        else:
            break
    except:
        print("**INVALID ENTRY!")   

# init
guess = (lower+upper) // 2
guessMN(guess, mn, lower, upper)

# END
