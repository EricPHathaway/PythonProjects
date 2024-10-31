import turtle

t = turtle.Turtle()

win = turtle.Screen()
win.bgcolor('skyblue')


sides = float(input('How many sides will your shape have? '))

turn= ((sides-2)*180)/sides

sides=int(sides)

t.speed('fastest')
t.color('lightpink')
t.right(90)
if sides >= 3:
  for x in range (0, sides):
    t.pensize(3)
    t.forward(45)
    for i in range(0,45):
      t.forward(1)
      t.left(1)
    t.left(135)
    t.penup()
    t.color('orange')
    t.pensize(7)
    t.forward(15)
    t.right(30)
    t.pendown()
    t.forward(15)
    t.left(60)
    t.forward(15)
    t.left(120)
    t.forward(15)
    t.left(60)
    t.forward(15)
    t.penup()
    t.right(30)
    t.forward(15)
    t.pendown()
    t.left(135)
    t.color('lightpink')
    t.pensize(3)
    for j in range(0,45):
      t.forward(1)
      t.left(1)
    t.forward(45)      
    t.left(-turn)

else:
  print('There are not enough sides to make a shape from that number.')
