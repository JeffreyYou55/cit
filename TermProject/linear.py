from turtle import *

def linear(slope, y_intercept):
    penup()
    # setx(-300)
    # sety(-300*slope+y_intercept*10)
    # pendown()
    # if (-300<=-300*slope+y_intercept<=300):
    #     setposition(-300,-300*slope+y_intercept*10)
    # else:
    #     setposition(-300/slope-y_intercept/slope,-300)
    # pendown()
    # # setx(300)
    # # sety(300*slope+y_intercept*10)
    # if (-300<=300*slope+y_intercept<=300):
    #     setposition(300, 300*slope+y_intercept*10)
    # else:
    #     setposition(300/slope-y_intercept/slope,300)
    if (-300<=-300*slope+y_intercept<=300):
        setposition(-300,-300*slope+y_intercept*10)
        pendown()
        setposition(300, 300*slope+y_intercept*10)
    else:
        setposition(-300/slope-y_intercept*10/slope,-300)
        pendown()
        setposition(300/slope-y_intercept*10/slope,300)
    pendown()
