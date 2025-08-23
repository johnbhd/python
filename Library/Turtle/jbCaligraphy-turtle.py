#JB python

import turtle

t = turtle.Turtle()


t.penup()
#t.goto(100, 0) 


t.goto(0, 200)   
t.color("red")
t.pensize(30)
t.speed(10)

#J
t.pendown()
t.setheading(270)

t.forward(250)
t.forward(100)
 
t.circle(-150, 180)
t.penup()
t.pendown()

#new position
t.penup()
t.goto(100, 200)
t.pendown()


#B
t.setheading(270)
t.forward(250)
t.penup()
t.goto(100, 75)
t.pendown()
t.circle(150, 289)

t.forward(80)
t.goto(100, -50)
t.pendown()
t.forward(-50)
t.circle(180, -230)
t.pendown()

t.goto(100, 0)

#end
turtle.done()