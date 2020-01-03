from turtle import *

speed(5)
width(8.5)

def square(height, width, x, y, color = "white"): # input(parameter) : length
    penup()
    setx(x)
    sety(y)
    pendown()
    fillcolor(color)
    begin_fill()
    for _ in ["Elsa", "Anna"]:
        forward(width)
        left(90)
        forward(height)
        left(90)
    end_fill()


square(50,100,-200,-200, "blue")
square(50,100,-200,-150)
square(100,150,-100,-200)
square(100,150,50,-200, "yellow")
square(300,250,-200,-100, "red")
square(250,150,50,-100)
square(50,100,50,150)
square(50,50,150,150, "blue")

done()
