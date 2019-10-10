#==========================================================================
# PROGRAM PURPOSE:... C7 Palindrome Checker (requires stack.py and letterCount.py)
# AUTHOR:............ Thompson, Nick
# COURSE:............ CSC 131-004
# TERM:.............. Fall 2017
# COLLABORATION:..... 
# WORK TIME(h:mm):... 1:00
#==========================================================================
# Program for Determining Palindromes

import stack
from letterCount import countLetters

print ('This program can determine if a given string is a palindrome')
print ('(Enter return to exit)')

# init
char_stack = stack.getStack()
empty_string = ''

# get string from user
chars = input('Enter string to check: ')
longest = None

while chars != empty_string:
    if len(chars) == 1:
        print('A one letter word is by definition a palindrome\n')
    else:
        # init
        is_palindrome = True
        
        # determine half of length. excluding any middle character
        compare_length = len(chars) // 2

        # push second half of input string on stack
        for k in range(compare_length, len(chars)):
            stack.push(char_stack, chars[k])

        # pop chars and compare to first half of string
        k = 0
        while k < compare_length and is_palindrome:
            ch = stack.pop(char_stack)
            if chars[k].lower() != ch.lower():
                is_palindrome = False
                
            k += 1
            
        # display results
        if is_palindrome:
            print ()
            print (chars, 'is a palindrome')
            if longest is None:
                longest = chars
                print ("{} is the longest palindrome entered so far.".format(longest))
                print ()
            elif countLetters(chars) > countLetters(longest):
                longest = chars
                print ("{} is the longest palindrome entered so far.".format(longest))
                print ()
                
        else:
            print ()
            print (chars, 'is NOT a palindrome\n')

    # get string from user
    chars = input('Enter string to check: ')
