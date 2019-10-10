#=========================================================================#
# *********************************************************************** #
# ************************** PRACTICE EXAM 2 **************************** #
# *********************************************************************** #
#=========================================================================#
# Bouncing Balls Simulation Program
#==========================================================================
# PROGRAM PURPOSE:... q1, Exam2, test ability to modify program w/ objects
# AUTHOR:............ Last, First
# COURSE:............ CSC 131-004
# TERM:.............. Fall 2017
# COLLABORATION:..... None
# WORK TIME(h:mm):... 1:30
#==========================================================================
#==========================================================================
# q1 - modify this file to meet the following requirements:
#    - add a docstring for the module (none required for the functions)
#    - do not request user input
#    - run the simulation for 10 sec
#    - create exactly 3 balls
#    - change balls to a new shape whenever they hit a wall
#    NOTE:  this program has been modified to be used as a module.  All the
#       "main" code has been placed in a function named startItUp(). That
#       function will be called from the primary exam file.  Do NOT add any
#       code to the bottom of this file.  Only modify within the 7 functions
#       whatever code is necessary to meet the problem requirements.
#==========================================================================

'''docstring'''
import turtle
import random
import time



def atLeftEdge(ball, screen_width):
    if ball.xcor() < -screen_width / 2:
        ball.shape('turtle')
        return True
    else:
        return False

def atRightEdge(ball, screen_width):
    if ball.xcor() > screen_width / 2:
        ball.shape('triangle')
        return True
    else:
        return False

def atTopEdge(ball, screen_height):
    if ball.ycor() > screen_height / 2:
        ball.shape('square')
        return True
    else:
        return False

def atBottomEdge(ball, screen_height):
    if ball.ycor() < -screen_height / 2:
        ball.shape('arrow')
        return True
    else:
        return False

def bounceBall(ball, new_direction):
    if new_direction == 'left' or new_direction == 'right':
        new_heading = 180 - ball.heading()
    elif new_direction == 'down' or new_direction == 'up':
        new_heading =  360 - ball.heading()

    return new_heading

def createBalls(num_balls):
    balls = []
    for k in range(0, num_balls):
        new_ball = turtle.Turtle()
        new_ball.shape('circle')
        new_ball.fillcolor('black')
        new_ball.speed(0)
        new_ball.penup()
        new_ball.setheading(random.randint(1,359))
        balls.append(new_ball)

    return balls

def startItUp():
    # ---- (formerly) main
    # init screen size
    screen_width = 800
    screen_height = 600
    turtle.setup(screen_width,screen_height)

    # create turtle window
    window = turtle.Screen()
    window.title('Bouncing Balls')

    # prompt user for execution time and number of balls
    num_seconds = 0
    num_balls = 3

    # create balls
    balls = createBalls(num_balls)

    # set start time
    start_time = time.time()

    # begin simulation

    terminate = False

    while not terminate:
        for k in range(0,len(balls)):
            balls[k].forward(15)
            if atLeftEdge(balls[k], screen_width):
                balls[k].setheading(bounceBall(balls[k],'right'))
            elif atRightEdge(balls[k], screen_width):
                balls[k].setheading(bounceBall(balls[k],'left'))
            elif atTopEdge(balls[k], screen_height):
                balls[k].setheading(bounceBall(balls[k],'down'))
            elif atBottomEdge(balls[k], screen_height):
                balls[k].setheading(bounceBall(balls[k],'up'))

        if time.time() - start_time > num_seconds:
            terminate = True

    #turtle.goto(0,0)
    turtle.write("Simulation complete - click to exit")
    # exit on close window
    turtle.exitonclick()
#==========================================================================
# *************************************************************************
# ******************* DO NOT ADD CODE BELOW THIS POINT ********************
# *************************************************************************
#==========================================================================
