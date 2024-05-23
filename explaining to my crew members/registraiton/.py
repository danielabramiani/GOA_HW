from turtle import *

#we want to paint a house

#step1 draw a square
speed(1)
color("black")
width(7)
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of the square

#drawing a door
forward(70)
color("green")
left(90)
forward(100)
right(90)
forward(60)
right(90)
forward(100)

#drawing a triangle
penup()
goto(200,200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()
#end of the triangle

#drawing a window
penup()
color("blue")
begin_fill()
goto(140,140)
pendown()

left(120)
forward(40)

left(90)
forward(40)

left(90)
forward(40)
right(90)
end_fill()

#second window
penup()
forward(80)
pendown()

color("blue")
begin_fill()
forward(40)
right(90)

forward(40)
right(90)

forward(40)
right(90)

forward(40)
right(90)
end_fill()

exitonclick()

name = "Nikoloz"
surname = "Egriselashvili"
age = 11

print(name + ' ' + surname + ' ' + age)

#string "Daniel" "i bought a new thing"
#integer-int 11,16
#float 2.02