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


