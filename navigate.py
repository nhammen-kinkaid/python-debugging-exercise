import turtle

# Set up the screen window
window = turtle.Screen()
window.setup(width=900, height=600)
window.bgpic("maze.gif")

# Create a visible turtle object
my_turtle = turtle.Turtle()
my_turtle.shape("turtle")
my_turtle.color("green")
my_turtle.shapesize(2)

def move_slowly(steps):
  for i in range(200):
    my_turtle.forward(1)

def click_handler(x, y):
  my_turtle.teleport(100, -200)
  my_turtle.setheading(180)
  my_turtle.clear()

  my_turtle.pendown()
  move_slowly(200)
  my_turtle.right(90)
  move_slowly(100)
  my_turtle.right(45)
  move_slowly(200)
  my_turtle.left(9)
  my_turtle.circle(-90)
  my_turtle.penup()

my_turtle.teleport(100, -200)
my_turtle.onclick(click_handler)

# Keep the window open and listening for events
window.mainloop()
