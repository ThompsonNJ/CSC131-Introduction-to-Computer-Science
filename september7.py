p = [["first", "last", "num"],["George", "Washington", 1],["John", "Adams" ,2], ["Thomas", "Jefferson", 3]]
x = 0
while x < len(p):
	print(format(p[x][0],"<10"),
              format(p[x][1],"<15"),
            p[x][2])
	x += 1
	

