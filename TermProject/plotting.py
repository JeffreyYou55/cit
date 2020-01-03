from turtle import *
import coordinates
import square
import linear

border = {
"width" : 615,
"height" : 615
}

square.draw_square(border["width"], border["height"], -300, -300)
penup()
setx(0)
sety(0)
pendown()
coordinates.draw_coordinate()
linear.linear()

done()
