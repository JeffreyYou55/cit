from turtle import *
import coordinates
import square
import linear
import quadratic

border = {
"width" : 620,
"height" : 620
}

# draw square and coordinate
print("< Jeffrey's Plotting Software >")
print("drawing rectangular coordinates...")
square.draw_square(border["width"], border["height"], -310, -300)
penup()
setx(0)
sety(0)
pendown()
coordinates.draw_coordinate()

draw_finished = False
while not draw_finished :
    function_type = int( input("linear : 1, quadratic : 2 ") )
    if(function_type == 1) :
        slope = int( input("type the slope : ") )
        y_incpt = int( input("type the y intercept : ") )
        linear.linear(slope, y_incpt)
    if(function_type == 2) :
        a = float( input("type a : ") )
        b = int( input("type b : ") )
        c = int( input("type c : ") )
        quadratic.quadratic(a,b,c)
    draw_ends = input("press N to finish drawing. ")
    if (draw_ends == "N" ):
        draw_finished = True


done()
