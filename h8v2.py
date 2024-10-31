import turtle

import random

import math
m = math.sqrt(3)

bnd = turtle.Turtle()
bnd.speed('fastest')
bnd.penup()
bnd.setposition(0,-200*m)
bnd.pendown()
bnd.color('white')
bnd.right(180)
bnd.fd(200)
bnd.right(180)
bnd.fd(400)
bnd.left(60)
bnd.fd(400)
bnd.left(60)
bnd.fd(400)
bnd.left(60)
bnd.fd(400)
bnd.left(60)
bnd.fd(400)
bnd.left(60)
bnd.fd(400)
bnd.left(60)
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
b.right(180)
b.fd(80)
b.left(90)
b.fd(80*m)
b.pendown()

c = turtle.Turtle()
c.color('green')
c.penup()
c.setposition(160,0)
c.pendown()

d = turtle.Turtle()
d.color('yellow')
d.penup()
d.right(0)
d.fd(80)
d.left(90)
d.fd(80*m)
d.pendown()

e = turtle.Turtle()
e.color('pink')
e.penup()
e.right(0)
e.fd(80)
e.right(90)
e.fd(80*m)
e.pendown()

f = turtle.Turtle()
f.color('white')
f.penup()
f.right(180)
f.fd(80)
f.right(90)
f.fd(80*m)
f.pendown()


def randomDirection(aa):
    x = 60*random.randint(0,5)
    aa.setheading(x)

def resetPosition(ab):
    q = random.randint(1,3)
    a = 10*random.randint(0,39)
    b = 10*random.randint(1,39)
    if q == 1:
        x = a
        y = b
        z = 0
    elif q == 2:
        x = 0
        y = a
        z = b
    elif q == 3:
        x = b
        y = 0
        z = a
    ab.penup()
    ab.setposition(0,0)
    ab.setheading(0)
    ab.fd(x-((y/2)+(z/2)))
    ab.right(90)
    ab.fd(((y-z)/2)*m)
    ab.pendown()

def moveTurtle(ac):
    ac.fd(10)

def posCheck1(ba,bb):
    if -10<=(ba.xcor()-bb.xcor())<=10 and -10<=(ba.ycor()-bb.ycor())<=10:
        resetPosition(ba)
        resetPosition(bb)
#        print(i)

def posCheck2(ad):
    if abs(ad.ycor()) >= 346 or abs(ad.ycor()) >= (-m)*abs(ad.xcor()) + (692):#or ad.xcor() >= (-1/2)*ad.ycor() + (346) or ad.xcor() >= (1/2)*ad.ycor() + -(346) or ad.xcor() >= (1/2)*ad.ycor() + (346) or ad.xcor() <= (-1/2)*ad.ycor() + -(346) :
        resetPosition(ad)        

for i in [a, b, c, d, e, f]:
    i.speed('fastest')

while True:
    for i in [a, b, c, d, e, f]:
        randomDirection(i)
        moveTurtle(i)
        if i == a:
            posCheck1(i,b)
            posCheck1(i,c)
            posCheck1(i,d)
            posCheck1(i,e)
            posCheck1(i,f)
        elif i == b:
            posCheck1(i,a)
            posCheck1(i,c)
            posCheck1(i,d)
            posCheck1(i,e)
            posCheck1(i,f)
        elif i == c:
            posCheck1(i,a)
            posCheck1(i,b)
            posCheck1(i,d)
            posCheck1(i,e)
            posCheck1(i,f)
        elif i == d:
            posCheck1(i,a)
            posCheck1(i,b)
            posCheck1(i,c)
            posCheck1(i,e)
            posCheck1(i,f)
        elif i == e:
            posCheck1(i,a)
            posCheck1(i,b)
            posCheck1(i,c)
            posCheck1(i,d)
            posCheck1(i,f)
        elif i == f:
            posCheck1(i,a)
            posCheck1(i,b)
            posCheck1(i,c)
            posCheck1(i,e)
            posCheck1(i,d)
        posCheck2(i)
        

