from turtle import *

speed(3.5)

penup()
setx(-300)
pendown()
forward(600)
penup()
setx(0)
sety(-300)
left(90)
pendown()
forward(600)

point = [-150,200]
angle = -60

penup()
setx(point[0])
sety(point[1])
pendown()
left(-90 + angle)
forward(1000)
backward(2000)
forward(3000)

done()

# two point method

# penup()
# setx(point1[0])
# sety(point1[1])
# pendown()
# goto(point2[0], point2[1])
# forward(1000)
# backward(1000)
