from turtle import *
# turtle tutorial
# https://github.com/asweigart/simple-turtle-tutorial-for-python/blob/master/simple_turtle_tutorial.md
speed(0)
width(3)
pencolor("blue")

print(   range(5)   ) # range(5) == [0, 1, 2, 3, 4]

for i in range(500): # this "for" loop will repeat these functions 500 times
    forward(i)
    left(91)
    # left(2 * i)

done()
