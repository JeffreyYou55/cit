from turtle import *
# draw conditions

speed(3.5)
width(3)

# rectangular Coordinates

space = 5

# x coordinate :for
penup()
setx(-300)
for i in range(61):
    if(i%space == 0 and i != 30):
        write(i-30)
        # drawing small lines
        forward(10)
        right(90)
        pendown()
        forward(5)
        backward(5)
        penup()
        left(90)
        backward(10)
    forward(10)
backward(600)
pendown()
forward(600)
# y coordinate : while
penup()
setx(5)
sety(-300)
left(90)
yValue = -30
while(yValue<=30):
    # if(yValue%5==0):
    #     write(yValue)
    #     yValue=yValue+1
    # else:
    #     yValue=yValue+1
    if(yValue%5==0):
        write(yValue)
    yValue=yValue+1
    forward(10)
backward(600)
setx(0)
pendown()
forward(600)


# draw linear function
# point = [-150,200]
# angle = -60
#
# penup()
# setx(point[0])
# sety(point[1])
# pendown()
# left(-90 + angle)
# forward(1000)
# backward(2000)
# forward(3000)

done()
