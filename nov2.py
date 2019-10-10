##def fib_nr(n):
##    a = 0
##    b = 1
##    for x in range(0,n):
##        if x <=1:
##            c = x
##        else:
##            c = a + b
##            a = b

##            b = c
##    return c
##
##for f in range(1,101):
##    print(f,": ",fib_nr(f))

########################################
import time

def fib(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)
    
for f in range(1,101):
    print(f,": ",fib(f))

#########################################

def fib(n):
    if n in fDict:
        return fDict[n]
    
    if n == 1:
        a = 0
    elif n == 2:
        a = 1
    else:
        a = fib(n-1) + fib(n-2)
        
    fDict[n] = a
    return a

fDict = {}

for f in range(1,101):
    print(f,": ",fib(f))
