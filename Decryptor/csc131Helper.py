#==========================================================================
# PROGRAM PURPOSE:... C7 Helper Program
# AUTHOR:............ Thompson, Nick
# COURSE:............ CSC 131-004
# TERM:.............. Fall 2017
# COLLABORATION:..... 
# WORK TIME(h:mm):... 2:00
#==========================================================================
'''Contains functions that help with previous and future homeworks.'''

def makeGrid(width, height, block, x):
    '''Makes a grid given the width, height, block size and turtle.'''
    x.hideturtle()
    x.speed(0)
    x.penup()
    x.setposition(width // -2, height // -2)
    x.pendown()
    x.setposition(width // -2, height // 2)
    x.setposition(width // 2, height // 2)
    x.setposition(width // 2, height // -2)
    x.setposition(width // -2, height // -2)
    x.setheading(90)
    x.forward(height)

    while int(x.xcor()) in range(width // -2, (width // 2) - block):
            x.right(90)
            x.forward(block)
            x.right(90)
            x.forward(height)
            x.left(90)
            x.forward(block)
            x.left(90)
            x.forward(height)
        
    x.penup()
    x.setposition(width // -2, height // -2)
    x.setheading(90)
    x.pendown()
    
    while int(x.ycor()) in range(height // -2, (height // 2) - block):
        x.forward(block)
        x.right(90)
        x.forward(width)
        x.left(90)
        x.forward(block)
        x.left(90)
        x.forward(width)
        x.right(90)

def userInputInt(lower, upper):
    '''Returns a user-inputted integer including and between a given range ("lower" and "upper")'''
    while True:
        try:
            userInput = int(input("Please enter an integer including and between {} and {}: ".format(lower, upper)))

            if userInput in range(lower, upper + 1):
                return userInput
            else:
                raise ValueError
            
        except ValueError:
            print("Invalid Entry!")

def getFile():
    '''Asks for input of a file name (fname) and opens that file in read mode (file). Returns fname, file.'''
    try:
        fname = input("Please enter a file name: ")
        file = open(fname, 'r')
        return fname, file
    
    except FileNotFoundError:
        print("Could not find file!")
        getFile()
