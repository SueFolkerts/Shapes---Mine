import random
import turtle


turtle.title("My Turtle Game")
turtle.bgcolor("grey")
turtle.setup(600,600)
turtle.shape("turtle")
screen = turtle.Screen()
sally = turtle.Turtle()

def star(length, color, x, y):
  sally.penup()
  sally.setpos(x, y)
  sally.pendown()
  sally.fillcolor(color)
  sally.begin_fill()
  x = 0
  while x < 5:
    sally.forward(int(length))
    sally.right(144)
    x = x+1
  sally.end_fill()
def triangle(length, color, x, y):
  sally.penup()
  sally.setpos(x, y)
  sally.pendown()
  sally.fillcolor(color)
  sally.begin_fill()
  x = 0
  while x < 3:
    sally.forward(int(length))
    sally.right(120)
    x = x+1
  sally.end_fill()
def square(length, color, x, y):
  sally.penup()
  sally.setpos(x, y)
  sally.pendown()
  sally.fillcolor(color)
  sally.begin_fill()
  x = 0
  while x < 4:
    sally.forward(int(length))
    sally.right(90)
    x = x+1
  sally.end_fill()
def circle(length, color, x, y):
  sally.penup()
  sally.setpos(x, y)
  sally.pendown()
  sally.fillcolor(color)
  sally.begin_fill()
  sally.circle(int(length))
  sally.end_fill()

choice = input("Type R for random shapes  ")

if choice == 'R':
  for x in range(6):
    shape = random.randint(0,3)
    input_length = random.randint(10,200)
    input_color = "#"+''.join([random.choice('ABCDEF0123456789') for i in range(6)])
    print( input_color)
    input_x = float(random.randint(-200, 200))
    input_y = float(random.randint(-200, 200))
    if shape == 0:
      star(input_length,input_color, input_x, input_y)
    elif shape == 1:
      triangle(input_length,input_color, input_x, input_y)
    elif shape == 2:
      square(input_length,input_color, input_x, input_y)
    elif shape == 3:
      circle(input_length,input_color, input_x, input_y)

while True:
  input_shape = input ("What shape you want to draw? or none to quit  ")
  if input_shape == '':
    break
  input_length = input ("Choose how big: ")
  input_x = float(input ("What is X: "))
  input_y = float(input ("What is Y: "))
  input_color = input ("Choose color: ")

 
  if input_shape == 'triangle':
    triangle(input_length,input_color, input_x, input_y)
  elif input_shape == 'circle':
    circle(input_length,input_color, input_x, input_y)
  elif input_shape == 'star':
    star(input_length,input_color, input_x, input_y)
  elif input_shape == 'square':
    square(input_length, input_color, input_x, input_y)


