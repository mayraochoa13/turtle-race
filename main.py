#import libraries
from turtle import *
import turtle
from random import randint 

penup()
goto(-100, 180)
write("TURTLE RACE", font=("Arial", 20, "bold"))

wn = turtle.Screen()
wn.bgcolor("#b3ffb3")

speed(8)
penup()
goto(-140, 140)

# This for loop helps us draw the dashed track lines
for step in range(15):
  color('#004d00')
  write(step+1, align='center')
  right(90)
  for num in range(10):
    penup()
    forward(10)
    pendown()
    forward(10)
  penup()
  backward(200)
  left(90)
  forward(20)

#creating our turtle
blue = Turtle()
blue.shape('turtle')
blue.color('#33cccc')

#sending our turtle to the starting line
blue.penup()
blue.goto(-160,100)
blue.pendown()

#Making your turtle twirl
for num in range(60):
  blue.right(6)

#creating our second turtle
yellow = Turtle()
yellow.shape('turtle')
yellow.color('yellow')
yellow.penup()
yellow.goto(-160,70)
yellow.pendown()
for num in range(60):
  yellow.left(6)

#Make turtles race
for turn in range(100):
  blue.forward(randint(1,5))
  yellow.forward(randint(1,5))