from turtle import *

def draw_square(height, width, x, y, color = "white"): # input(parameter) : length
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
