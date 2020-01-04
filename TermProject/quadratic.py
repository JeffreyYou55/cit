from turtle import *

def quadratic(a, b , c):
    penup()
    for x_value in range(61):
        x = x_value-30
        y = a*x**2+ b* x + c
        setposition(x * 10, y*10)
        pendown()
