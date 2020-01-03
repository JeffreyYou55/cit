from turtle import *

speed(5)

def square(length, x, y): # input(parameter) : length
    penup()
    setx(x)
    sety(y)
    pendown()
    forward(length)
    left(90)
    forward(length)
    left(90)
    forward(length)
    left(90)
    forward(length)
    left(90)

# square(50)
# square(100)
# square(150)
# square(200)
# square(250)
# square(300)
# square(350)
# square(400)


# for i in range(401):
#     if (i%50 == 0):
#         square(i)

# for i in range(8):
#         square(i * 50 + 50)

square(200, 0,0)
square(30, 10,50)
square(100, -80,-50)
square(400, -70,90)

done()
