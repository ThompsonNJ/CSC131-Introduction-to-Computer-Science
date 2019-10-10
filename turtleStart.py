import turtle as t

t.setup(800,600)

win = t.Screen()
win.title("Random crow fly . . . ")

tt = t.getturtle()

tt.penup()
tt.setheading(270)
tt.forward(200)
tt.pendown()
tt.left(90)
tt.forward(200)
tt.left(90)
tt.forward(200)
tt.left(90)
tt.forward(200)
tt.left(90)
tt.forward(200)
##tt.setposition(-300,200)
##tt.setposition(300,200)
##tt.setposition(300,-200)
##tt.setposition(-300,-200)

t.exitonclick()
