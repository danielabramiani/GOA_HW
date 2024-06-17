from turtle import*

#we want to paint a house


#step 1: draw a square
speed(30)

width(7)
color("purple")

forward (200)
left(90)

forward (200)
left (90)

forward (200)
left(90)

forward (200)
left (90)
#end of square

#drawing a door
begin_fill()
forward (70)
color("yellow")
left(90)
forward(120)  #height of the door
right(90)
forward(60)
right (90)
forward (120)
end_fill()

penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right (150)
forward (200)
left (120)
forward (200)
end_fill()
left(120)
forward(70)
begin_fill()
color ("brown")
right(90)
forward (60)
right(90)
forward (60)
right(90)
forward(60)
right(30)
end_fill()


right(80)
left(20)
forward(60)
penup()
begin_fill()
goto(130, 200) #house window
pendown()
forward(60)
right(90)
color("brown")
forward(60)
right(90)
forward(60)
right(90)
forward(60)
right(90)
forward(60)
end_fill()



exitonclick()