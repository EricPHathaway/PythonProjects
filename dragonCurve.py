import turtle
import math

fractal = turtle.Turtle()
fractal.speed('fastest')
fractalColor = '#ff0000'

fractal.color(fractalColor)
fractal.penup()

win = turtle.Screen()
win.bgcolor('black')

def turnGenerator(num):
    turnList = []
    if(num > 0):
        turnList = turnAdder(turnGenerator(num-1))
    return turnList
    


def turnAdder(turnListA):
    turnListB = []
    turnListB = turnListA + ['r'] + turnInverse(turnListA)
    return turnListB

def turnInverse(turnListA):
    turnListB = []
    for i in range(len(turnListA)):
        if(turnListA[-1-i] == 'r'):
            turnListB = turnListB + ['l']
        elif(turnListA[-1-i] == 'l'):
            turnListB = turnListB + ['r']
        elif(turnListA[-1-i] == 'a'):
            turnListB = turnListB + ['a']
    return turnListB
        


def fractalMaker(depth):
    startPos = [0, 0]
    currentPos = [0, 0]
    leftPos = 0
    rightPos = 0
    upPos = 0
    downPos = 0

    directions = turnGenerator(depth)

    heading = 1

    print(len(directions))

    for i in range(len(directions)):
        if(heading == 1):
            currentPos[0] += 1
            if(currentPos[0] > upPos):
                upPos = currentPos[0]
        elif(heading == 3):
            currentPos[0] -= 1
            if(currentPos[0] < downPos):
                downPos = currentPos[0]
        elif(heading == 2):
            currentPos[1] += 1
            if(currentPos[1]>  rightPos):
                rightPos = currentPos[1]
        elif(heading == 4):
            currentPos[1] -= 1
            if(currentPos[1] < leftPos):
                leftPos = currentPos[1]
        if(directions[i] == 'r'):
            heading += 1
            if(heading == 5):
                heading = 1
        elif(directions[i] == 'l'):
            heading -= 1
            if(heading == 0):
                heading = 4

    maxAcross = 0

    if(abs(rightPos - leftPos) > abs(upPos - downPos)):
            maxAcross = abs(rightPos - leftPos)
    else:
            maxAcross = abs(upPos - downPos)

    res = math.floor(1200 /maxAcross)

    startX = (-(rightPos + leftPos)/2) * res
    startY = (-(upPos + downPos)/2) * res


    
        
    fractal.setposition(startX, startY)

    runFractal(depth, res)

def hexConverter(num):
    if(num >= 256):
        num = 255
    elif(num < 0):
        num = 0
    digit1 = math.floor(num/16)
    digit2 = math.floor(num%16)

    if(digit1 >= 10):
        digit1 = chr(97 + (digit1 - 10))
    if(digit2 >= 10):
        digit2 = chr(97 + (digit2 - 10))
    value = str(digit1) + str(digit2)
    return(value)
               
def runFractal(depth, res):

    
    fractal.pencolor('red')
    turtle.tracer(0, 0)
    
    directions = turnGenerator(depth)

    halfDirections = math.ceil((len(directions)+1)/2)
    halfProgress = 0

    fractal.pendown()
    fractal.setheading(90)
    print(halfDirections)

    for i in range(len(directions)+1):
        fractal.fd(res)

        if(i < len(directions)):
            if(directions[i] == 'r'):
                fractal.setheading(fractal.heading() - 90)
            elif(directions[i] == 'l'):
                fractal.setheading(fractal.heading() + 90)

        halfProgress += 1
        if(halfProgress >= halfDirections):
            halfProgress = 0
            halfDirections = math.ceil(halfDirections / 2)
            if(fractal.pencolor() == 'red'):
                fractal.pencolor('orange')
            elif(fractal.pencolor()  == 'orange'):
                fractal.pencolor('yellow')
            elif(fractal.pencolor() == 'yellow'):
                fractal.pencolor('green')
            elif(fractal.pencolor() == 'green'):
                fractal.pencolor('blue')
            elif(fractal.pencolor() == 'blue'):
                fractal.pencolor('purple')
            elif(fractal.pencolor() == 'purple'):
                fractal.pencolor('red')

    fractal.penup()
    fractal.setposition(1500, 1500)

fractalMaker(18)
    
        



