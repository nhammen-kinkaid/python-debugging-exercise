import turtle

# Set up the screen window
window = turtle.Screen()
window.bgcolor("black")

# Create a visible turtle object
my_turtle = turtle.Turtle()
my_turtle.shape("turtle")
my_turtle.color("green")
my_turtle.shapesize(3)

def click_handler(x, y):
  my_turtle.teleport(50, -100)
  my_turtle.setheading(180)
  my_turtle.clear()

  my_turtle.pendown()
  my_turtle.forward(100)
  my_turtle.right(90)
  my_turtle.forward(50)
  my_turtle.right(45)
  my_turtle.forward(100)
  my_turtle.right(9)
  my_turtle.circle(40)
  my_turtle.penup()

my_turtle.onclick(click_handler)

# Keep the window open and listening for events
window.mainloop()
