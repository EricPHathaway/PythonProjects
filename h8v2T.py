import turtle
ab = turtle.Turtle()
import random
import math
m =  math.sqrt(3)
ab.speed('fastest')
for x in range(0,5):
    for y in range(0,5):
        for z in range(0,5):
                ab.setposition(0,0)
                ab.setheading(0)
                ab.fd(x-((y/2)+(z/2)))
                ab.right(90)
                ab.fd(((y-z)/2)*m)
                ab.pendown()
                if ab.ycor() > (2)*ab.xcor() + (9) or ab.ycor() < (-2)*ab.xcor() + -(10) or (ab.ycor() > m*10) or (ab.ycor() < m*-10) or ab.ycor() < (2)*ab.xcor() + -(10) or ab.ycor() > (-2)*ab.xcor() + (10):
                    print('err')
                    break
        else:
            print(y)
            print(x)
else:
    print('done')
