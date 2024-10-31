import turtle

import random

import math

a = math.sqrt(3)

t = turtle.Turtle()

t.penup()
t.pensize(5)
t.color('red')
t.speed('fastest')

win = turtle.Screen()
win.bgcolor('black')

def drawShape(n):
        for i in range(0,n):                
                xp=random.randint(-250,250)
                yp=random.randint(-250,250)
                t.setposition(xp,yp)
                t.penup()
                t.left(90)
                t.fd(10*a)
                t.right(150)
                t.pendown()
                t.fd(20)
                t.right(60)
                t.fd(20)
                t.right(120)
                t.fd(20)
                t.right(60)
                t.fd(20)
                t.right(120)
                t.penup()
                t.left(60)

z = int(input('How many shapes would you like to make? '))

drawShape(z)


