#==========================================================================
# PROGRAM PURPOSE:... C6 Turtle Game
# AUTHOR:............ Thompson, Nick
# COURSE:............ CSC 131-004
# TERM:.............. Fall 2017
# COLLABORATION:..... Boucing Ball program for edges and angles; Andrew
# WORK TIME(h:mm):... 12:00
#==========================================================================
# imports
import turtle
import random
import time

def cN():
    return random.randint(0, 255)

# screen region
def atLeftEdge(turtle, screen_width):
    if turtle.xcor() < -screen_width / 2:
        return True
    else:
        return False

def atRightEdge(turtle, screen_width):
    if turtle.xcor() > screen_width / 2:
        return True
    
    else:
        return False

def atTopEdge(turtle, screen_height):
    if turtle.ycor() > screen_height / 2:
        return True
    else:
        return False

def atBottomEdge(turtle, screen_height):
    if turtle.ycor() < -screen_height / 2:       
        return True
    else:
        return False

# create play area
def drawBox():
        boxTurtle = turtle.Turtle()
        boxTurtle.shape('turtle')
        boxTurtle.fillcolor(0, 0, 255)
        boxTurtle.speed(8)
        boxTurtle.pencolor(0, 0, 255)
        boxTurtle.pensize(5)
        boxTurtle.penup()
        boxTurtle.setposition(-400, -400)
        boxTurtle.pendown()
        boxTurtle.setposition(-400, 400)
        boxTurtle.setposition(400, 400)
        boxTurtle.setposition(400, -400)
        boxTurtle.setposition(-400, -400)
        boxTurtle.hideturtle()
    
# turn at edge
def turnTurtle(turtle, new_direction):
    if new_direction == 'left' or new_direction == 'right':
        new_heading = 180 - turtle.heading()
    elif new_direction == 'down' or new_direction == 'up':
        new_heading =  360 - turtle.heading()

    return new_heading

# flash shredder when on screen edge
def ShredderOnEdge(death):
    death += 1
    shredder.speed(0)
    shredder.setposition(0, 0)
    shredder.hideturtle()
    time.sleep(.1)
    shredder.showturtle()
    time.sleep(.1)
    shredder.hideturtle()
    time.sleep(.1)
    shredder.showturtle()
    time.sleep(.1)
    shredder.hideturtle()
    time.sleep(.1)
    shredder.showturtle()
    shredder.hideturtle()
    time.sleep(.1)
    shredder.showturtle()
    shredder.hideturtle()
    time.sleep(.1)
    shredder.showturtle()
    return death

# movement
def getCoordsX():
    return random.randint(-400, 400)

def getCoordsY():
    return random.randint(-400, 400)

def getHeading():
    return random.randint(0,360)

# get turtles
def getTurtles(numTurtles):
    turtles = []    
    for i in range(0, numTurtles):
        newTurtle = turtle.Turtle()
        newTurtle.shape('turtle')
        newTurtle.fillcolor(cN(), cN(), cN())
        newTurtle.speed(0)
        newTurtle.penup()
        newTurtle.setposition(getCoordsX(), getCoordsY())
        turtles.append(newTurtle)
    return turtles

# init screen size
screen_width = 800
screen_height = 800
turtle.setup(900, 900)

# instructions
print("The goal of the game is to eat all of the turtles.")
print("If you eat all of them, you win")
print("If you touch the wall, you lose a life.")
print("If you lose three lives, you lose.")
print("Note: Game performance will decrease as the number of turtles increases.")
print("Good luck!")

# window setup
window = turtle.Screen()
window.title("Turtle crusher")
turtle.colormode(255)
drawBox()

# shredder setup
shredder = turtle.Turtle()
shredder.shape('circle')
shredder.penup()
death = 0

# create turtles
while True:
    try:
        numTurtles = int(input("How many turtles do you want to try to eat? (>0): "))
        if numTurtles <= 0:
            raise ValueError
    except ValueError:
        print("Please enter an integer greater than zero!")
    else:
        break
    
turtles = getTurtles(numTurtles)

# begin game
terminate = False

# game over
while not terminate:
    for i in range(0,len(turtles)):
        turtles[i].setheading(getHeading())
        window.onclick(shredder.goto)
        shredder.speed(2)
        turtles[i].forward(50)
 
        # turn turtles back to play area
        if atLeftEdge(turtles[i], screen_width):
            turtles[i].setheading(turnTurtle(turtles[i],'right'))
            turtles[i].forward(100)
        elif atRightEdge(turtles[i], screen_width):
            turtles[i].setheading(turnTurtle(turtles[i],'left'))
            turtles[i].forward(100)
        elif atTopEdge(turtles[i], screen_height):
            turtles[i].setheading(turnTurtle(turtles[i],'down'))
            turtles[i].forward(100)
        elif atBottomEdge(turtles[i], screen_height):
            turtles[i].setheading(turnTurtle(turtles[i],'up'))
            turtles[i].forward(100)

        # force shredder in play area   
        if atLeftEdge(shredder, screen_width):
            death = ShredderOnEdge(death)
        elif atRightEdge(shredder, screen_width):
            death = ShredderOnEdge(death)
        elif atTopEdge(shredder, screen_height):
            death = ShredderOnEdge(death)
        elif atBottomEdge(shredder, screen_height):
            death = ShredderOnEdge(death)

        if int(turtles[i].xcor() - shredder.xcor()) in range(-50, 50) and int(turtles[i].ycor() - shredder.ycor()) in range(-50, 50):
            turtles[i].hideturtle()

        # lose
        if death == 3:
            terminate = True
            turtle.exitonclick()
            print("Game Over! You Lose!")

        # win
        canTerminate = True
        for currentTurtle in turtles:
            if currentTurtle.isvisible():
                canTerminate = False
        if canTerminate == True:
            terminate = True
            turtle.exitonclick()
            print("Game Over! You Win!")
