import sys

#==========================================================================
# f1 - modify sortAndCount() to meet the conditions below
#    - accept 1 parameter; a wordlist tuple
#    - sort the wordlist and print to the screen
#    - count the number of words and return the value
#==========================================================================

def sortAndCount(t):
    sac = len(t)
    print(sorted(t))
    return sac
#==========================================================================
# f2 - modify lastLetter() to meet the conditions below
#    - accept 1 parameter; a wordlist tuple
#    - iterate over the wordlist and print to the screen any word
#    --- for which the last letter also appears somewhere in the word
#    - count the number of words that meet the criteria and return the value
#==========================================================================

def lastLetter(t):
      print(t)
      count = 0
      for i in t[0:26][-1]:
          print(i)
          #if i[0:26][-1]:
   

#==========================================================================
# f3 - modify lastLetterCountSort() to meet the conditions below
#    - accept 1 parameter; a wordlist tuple
#    - iterate over the wordlist and create a list of two things:
#    --- count of times the last letter appears in each word
#    --- the word
#    - sort the list by the count and print to the screen
#    - determine the largest count and return that value
#==========================================================================

def lastLetterCountSort(t):
    print(t)

#==========================================================================
# *************************************************************************
# ******************* DO NOT EDIT CODE BELOW THIS POINT *******************
# *************************************************************************
#==========================================================================

wordList = ("parka",
            "bomb",
            "colic",
            "jaded",
            "uncommunicative",
            "staff",
            "bigwig",
            "hippish",
            "piroghi",
            "hajj",
            "skyjack",
            "squall",
            "symptom",
            "nonintervention",
            "oreo",
            "shapeup",
            "qadaq",
            "racecar",
            "thoughtlessness",
            "betterment",
            "seppuku",
            "kalashnikov",
            "wheelbarrow",
            "xerox",
            "syzygy",
            "razzmatazz")


sac = sortAndCount(wordList)
ll = lastLetter(wordList)
llcs = lastLetterCountSort(wordList)

print("\n",sac,"words in the list")

print("\n",ll,"words where last letter appears elsewhere")

print("\n",llcs,"is the largest # of times a letter appears")

#END
