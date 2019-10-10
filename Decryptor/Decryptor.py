#==========================================================================
# PROGRAM PURPOSE:... C8 Decrypts txt based on letter frequency
# AUTHOR:............ Thompson, Nick
# COURSE:............ CSC 131-004
# TERM:.............. Fall 2017
# COLLABORATION:..... 
# WORK TIME(h:mm):... 6:00
#==========================================================================
'''The purpose of this program is to decrypt text files based on the frequency
each letter appears. After the initial decryption, the user can swap letters
until the file is fully decrypted. To end the program, the user must press
return when prompted for input. The decrypted file will be saved in the same
directory as the encrypted file renamed to reflect its new status.'''

# imports
import collections
import string
from operator import itemgetter
from csc131Helper import getFile

# variables
fname, file = getFile()
wname = fname.replace('.','_decrypted.')
standardLetters = list("etaoinshrdlcumwfgypbvkjxqz")
countedList = []
alphaList = []
wfile = open(wname, 'w')
etext = file.read()
print()

# init
if etext != '':
    alphabet = string.ascii_lowercase
    count = collections.Counter(c for c in etext if c in alphabet)

for letter in alphabet:
    countedList.append(count[letter])
    alphaList.append(letter)

combined = list(zip(alphaList, countedList))
combined.sort(key = itemgetter(1), reverse = True)
appearedLetters = [x[0] for x in combined]
appearedLetters = str(appearedLetters)
standardLetters = str(standardLetters)

print("This is the alphabet sorted by how often each letter appears in the text.")
print(appearedLetters+"\n")


print("Most common letters in the English language:")
print(standardLetters+"\n")


# main
if etext != '':
    decrypted = etext.maketrans(appearedLetters, standardLetters)
    decryptedText = etext.translate(decrypted)
    print(decryptedText)

#can't set to while not terminate because it tries to finish the loop? 
while True:    
        swapLettersI = input("\nPlease input a letter that you believe to be incorrect: ").lower()
        while swapLettersI not in string.ascii_lowercase:
            print("\nInvalid Entry!")  
            swapLettersI = input("Please input a letter that you believe to be incorrect: ").lower()
                        
        if swapLettersI is '':
            break

        swapLettersC = input("\nPlease input a letter you want to swap the incorrect letter with: ").lower()
        while swapLettersC not in string.ascii_lowercase:
            print("\nInvalid Entry!")  
            swapLettersC = input("Please input a letter you want to swap the incorrect letter with: ").lower()            

        if swapLettersC == '':
            break
        
        placeHolder = '55555'
            
        if etext != '':
            decryptedText = decryptedText.replace(swapLettersI, placeHolder)
            decryptedText = decryptedText.replace(swapLettersC, swapLettersI)
            decryptedText = decryptedText.replace(placeHolder, swapLettersC)
            print(decryptedText)
            print()
            print("Please press return when you are finished decrypting.")

wfile.write(decryptedText)
file.close()
wfile.close()
