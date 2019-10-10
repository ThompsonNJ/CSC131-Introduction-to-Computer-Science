def pX2(x):
    print("x is", x,"in pX2")
    x += 100
    print("x is", x,"out pX2")

def pX1(x):
    print("x is", x,"in pX1")
    x += 10
    print("x is", x,"mid pX1")
    pX2(x)
    print("x is", x,"out pX1")

x = 1
print("x is", x,"at the start")
pX1(x)
print("x is", x,"in the end")

print("------------------------------------------------------")

def pX2(x2):
    print("x2 is", x2,"in pX2",id(x2))
    x2 += 100
    print("x2 is", x2,"out pX2",id(x2))

def pX1(x1):
    print("x1 is", x1,"in pX1",id(x1))
    x1 += 10
    print("x1 is", x1,"mid pX1",id(x1))
    pX2(x1)
    print("x1 is", x1,"out pX1",id(x1))

x = 1
print("x is", x,"at the start",id(x))
pX1(x)
print("x is", x,"in the end",id(x))

