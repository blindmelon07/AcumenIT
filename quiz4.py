import turtle

# Setup
t = turtle.Turtle()
t.speed(3)
t.pensize(5)

# Starting point
t.penup()
t.goto(-100, 100)
t.pendown()

# Draw the top horizontal line
t.forward(200)

# Move to  vertical line
t.penup()
t.goto(0, 300)
t.setheading(500)  #point down
t.pendown()

# Draw the vertical line of T
t.forward(200)

# Keep window open
turtle.done()