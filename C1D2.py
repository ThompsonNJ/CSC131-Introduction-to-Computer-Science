#==========================================================================
# PROGRAM PURPOSE:... Ch1 D2
# AUTHOR:............ Thompson, Nick
# COURSE:............ CSC 131-004
# TERM:.............. Fall 2017
# COLLABORATION:..... 
# WORK TIME(h:mm):... 2:45
#==========================================================================
# imports
from time import sleep
import sys,time,random

print ("Welcome!")
# quesion
Q = int(input("How many years do you think it would take for all possible chess games to be played if 7,000,000,000 people played one unique chess game per day? "))
# display information
print ("Did you know that there are approximately 10^120 possible chess games that can be played?")
sleep(3)

print ("To put it into perspective...")
sleep(3)

print ("There are approximately 10^80 atoms in the observable universe and it would take an estimated 3 x 10^90 grains of sand to fill the universe solid.")
sleep(4)

print ("Thus, there are more possible chess games that can be played than the amount of grains of sand it would take to fill the entire universe solid!")
sleep(4)

# calculate result
ans = 10**120// 7000000000 * 2
ans = str(ans)
print ("But wait... chess is a two player game! This means the time it would take to play every possible chess game is doubled!")
sleep(3)

print ("It would take approximately...")
sleep(.1)

def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.1)
        
print_slow(ans)
print (" days for 7,000,000,000 people playing one unique chess game per day to play every possible chess game!")
sleep(.1)

print ("So how close were you?")
sleep(3)

ans = int(ans)
D = str(ans-Q)
print ("You were approximately...")
sleep(.1)

print_slow(D)
sleep(.1)

print (" days off.")
sleep(5)

