from turtle import*

#we want to paint a house
#step 1: draw a square

width(7)
color("green")
begin_fill()
forward(200)
left(90)


forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
end_fill()
#end of squere
#drawing a door
forward(70)
begin_fill()
color("yellow")
left(90)

forward(60)
right(20)

right(70)
forward(45)

right(90)
forward(60)
end_fill()
penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

# we want to draw windows
penup()
begin_fill()
color("blue")
left(80)
forward(30)
left(40)
forward(10)
pendown()

forward(40)
right(90)
forward(40)
right(90)
forward(40)
right(90)
forward(40)

end_fill()

penup()
right(90)
forward(80)
pendown()
begin_fill()
forward(40)
right(90)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
end_fill()










exitonclick()     
