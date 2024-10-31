import turtle

import random

bnd = turtle.Turtle()
bnd.speed('fastest')
bnd.penup()
bnd.setposition(-200,-200)
bnd.pendown()
bnd.color('white')
bnd.fd(400)
bnd.left(90)
bnd.fd(400)
bnd.left(90)
bnd.fd(400)
bnd.left(90)
bnd.fd(400)
bnd.left(90)
bnd.penup()
bnd.setposition(1000,0)

win = turtle.Screen()
win.bgcolor('black')

a = turtle.Turtle()
a.color('red')
a.penup()
a.setposition(-160,0)
a.pendown()

b = turtle.Turtle()
b.color('blue')
b.penup()
b.setposition(0,160)
b.pendown()

c = turtle.Turtle()
c.color('green')
c.penup()
c.setposition(160,0)
c.pendown()

d = turtle.Turtle()
d.color('yellow')
d.penup()
d.setposition(0,-160)
d.pendown()

def randomDirection(aa):
    x = 90*random.randint(0,3)
    aa.setheading(x)

def resetPosition(ab):
    x = 10*random.randint(-19,19)
    y = 10*random.randint(-19,19)
    ab.penup()
    ab.setposition(x,y)
    ab.pendown()

def moveTurtle(ac):
    ac.fd(10)

def posCheck1(ba,bb):
    if -10<=(ba.xcor()-bb.xcor())<=10 and -10<=(ba.ycor()-bb.ycor())<=10:
        resetPosition(ba)
        resetPosition(bb)
#        print(i)
def posCheck2(ad):
    if (ad.xcor() >= 199) or (ad.xcor() <= -199) or (ad.ycor() >= 199) or (ad.ycor() <= -199):
        resetPosition(ad)        

ans = 'n'
#while True:
#    ans = str(input('Press y to start! '))
#    if ans == 'y':
#        break

for i in [a, b, c, d]:
    i.speed('fastest')


while True:
    for i in [a, b, c, d]:
        randomDirection(i)
        moveTurtle(i)
        if i == a:
            posCheck1(i,b)
            posCheck1(i,c)
            posCheck1(i,d)
        if i == b:
            posCheck1(i,a)
            posCheck1(i,c)
            posCheck1(i,d)
        if i == c:
            posCheck1(i,a)
            posCheck1(i,b)
            posCheck1(i,d)
        if i == d:
            posCheck1(i,a)
            posCheck1(i,b)
            posCheck1(i,c)
        posCheck2(i)
        

