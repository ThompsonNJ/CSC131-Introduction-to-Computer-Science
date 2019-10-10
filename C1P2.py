#==========================================================================
# PROGRAM PURPOSE:... Ch1 P2
# AUTHOR:............ Thompson, Nick
# COURSE:............ CSC 131-004
# TERM:.............. Fall 2017
# COLLABORATION:..... 
# WORK TIME(h:mm):... 1:15
#==========================================================================
print ("Welcome!")
num=int(input("Please enter a power of 2: "))
power=2**num
print ("2 to the power of %s is %s." % (num, power))
while True:
    num=int(input("Please enter another power of 2: "))
    power=2**num
    print ("2 to the power of %s is %s." % (num, power))
