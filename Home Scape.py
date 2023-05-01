# File: HomeScape.py
# Darling Ngoh
# Description of Program:
'''
This program is intended to generate an awesome dream house. Displaying a beautiful house on a warm sunny cloudy day.
'''

import turtle
import math


#function to make setting turtle position easier
def go_to(x,y):
    turtle.penup()
    turtle.setpos(x,y)
    turtle.pendown()


#setting turtle spped
turtle.speed(0)

#setting blue sky background
go_to(-960,0)
turtle.color('light blue')
turtle.begin_fill()
turtle.forward(2000)
turtle.left(90)
turtle.forward(1000)
turtle.left(90)
turtle.forward(2000)
turtle.left(90)
turtle.forward(1000)
turtle.left(90)
turtle.end_fill()

#setting green grass background
turtle.color('light green')
turtle.begin_fill()
turtle.forward(2000)
turtle.right(90)
turtle.forward(1000)
turtle.right(90)
turtle.forward(2000)
turtle.right(90)
turtle.forward(1000)
turtle.right(90)
turtle.end_fill()


#creating distant mountain view
turtle.color ('black')
turtle.begin_fill()
go_to(-960,0)
turtle.left(45)
turtle.forward(150)
turtle.right(90)
turtle.forward(150)
turtle.left(45)
turtle.backward(45)
turtle.left(45)
turtle.forward(240)
turtle.right(90)
turtle.forward(240)
turtle.left(45)
turtle.end_fill()


#drawing main frame of house
turtle.color ('dark blue')
go_to(700,-80)

turtle.begin_fill()
count = 0
while count < 4:
    turtle.right(90)
    turtle.forward(300)
    count = count + 1
turtle.end_fill()

#drawing roof
turtle.color ('brown')
turtle.begin_fill()
turtle.left(135)
turtle.forward(300/math.sqrt(2))
turtle.left(90)
turtle.forward(300/math.sqrt(2))
turtle.end_fill()

turtle.up()
turtle.left(135)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.down()

current = turtle.pos()


def window ():
    count = 0
    while count < 4:
        turtle.right(90)
        turtle.forward(60)
        count = count + 1

    turtle.up()
    turtle.backward(30)
    turtle.right(90)
    turtle.down()
    turtle.forward(60)

    turtle.up()
    turtle.backward(30)
    turtle.right(90)
    turtle.backward(30)
    turtle.down()
    turtle.forward(60)
    turtle.right(90)
    turtle.forward(30)

#first window
turtle.color('blue')
turtle.begin_fill()
window()
turtle.end_fill()
turtle.color('black')
go_to(current[0],current[1]+60)
window()

#second window
go_to(turtle.pos()[0]+150, turtle.pos()[1])
turtle.color('blue')
turtle.begin_fill()
window()
turtle.end_fill()
turtle.color('black')
window()


go_to(turtle.pos()[0]-150,turtle.pos()[1] - 120)


#door
turtle.color('red')
turtle.begin_fill()

turtle.forward(80)
turtle.backward(80)
turtle.right(90)
turtle.forward(40)
turtle.left(90)
turtle.forward(80)
turtle.left(90)
turtle.forward(40)
turtle.end_fill()

#create clouds
go_to(700,200)
turtle.color("gray","white")
turtle.setheading(90)
turtle.begin_fill()
turtle.circle(60,180)
turtle.end_fill()
go_to(640,200)
turtle.setheading(90)
turtle.begin_fill()
turtle.circle(80,180)
turtle.end_fill()

go_to(100,450)
turtle.color("gray","white")
turtle.setheading(90)
turtle.begin_fill()
turtle.circle(60,180)
turtle.end_fill()
go_to(40,450)
turtle.setheading(90)
turtle.begin_fill()
turtle.circle(80,180)
turtle.end_fill()

#create circle of sun
go_to(-700,410)
turtle.color("yellow","yellow")
turtle.begin_fill()
turtle.circle(50)
turtle.end_fill()

#create sunrays
go_to(-650,410)
turtle.pensize(5)
for i in range(12):
        turtle.forward(80)
        turtle.backward(80)
        turtle.left(30)
        
go_to(0,0)

#flowers
def flower(y):
    current = turtle.pos()
    turtle.left(90)
    turtle.color("black","yellow")
    turtle.pensize(5) 
    turtle.fillcolor(y) 
    turtle.begin_fill() 

    for i in range(4):
        turtle.circle(60, 50)
        turtle.circle(10, 180)
        turtle.left(180)
        turtle.circle(10, 180)
        turtle.circle(60, 50)
        turtle.left(180)
    turtle.end_fill() 

    turtle.penup()
    turtle.goto(current[0]+10, current[1]-10)
    turtle.pendown()
    turtle.right(90)
    turtle.circle(-100, 80)


flower("yellow")

go_to(-200,-100)
turtle.left(45)
flower("red")
go_to(-500,-300)
turtle.left(45)
flower("purple")


#grass

go_to(-200,-200)
turtle.left(120)
def grass():
    turtle.color("black","green")
    turtle.begin_fill()
    turtle.left(60)
    turtle.forward(10)
    turtle.right(120)
    turtle.forward(10)
    turtle.left(45)

    turtle.left(60)
    turtle.forward(10)
    turtle.right(120)
    turtle.forward(10)
    turtle.left(45)

    turtle.left(60)
    turtle.forward(10)
    turtle.right(120)
    turtle.forward(10)
    turtle.left(45)

    turtle.end_fill()

grass()

go_to(-500,-100)
turtle.left(45)
grass()

go_to(-800,-100)
turtle.left(45)
grass()

go_to(-800,-400)
turtle.left(45)
grass()

go_to(-850,-350)
turtle.left(45)
grass()

go_to(-700,-400)
turtle.left(45)
grass()

go_to(800,-400)
turtle.left(45)
grass()

go_to(900,-250)
turtle.left(45)
grass()

go_to(870,-50)
turtle.left(45)
grass()

go_to(-100,-50)
turtle.left(45)
grass()

go_to(-90,-150)
turtle.left(45)
grass()

turtle.done()
