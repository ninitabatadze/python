from turtle import *
width(7)
speed(30)
color("green")
#xazi 1
forward(200)
left(90)

#xazi 2
forward(200)
left(90)

#xazi 3
forward(200)
left(90)

#xazi 4
forward(200)
left(90)

#karebi

forward(70)
color("yellow")
begin_fill()
left(90)

forward(120)
right(90)

forward(60)
right(90)

forward(120)
end_fill()

#saxuravi
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

#windows
color("green")
left(30)
forward(30)

color("green")
forward(60)
left(90)

forward(40)
left(90)

forward(40)
left(90)


forward(40)
right(90)
exitonclick()