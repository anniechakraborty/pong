import turtle

# Creating window
win = turtle.Screen()
win.title('Pong by @annieC')
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)
# this prevents the window from auto updating and makes the game faster - we can update the window manually now.

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
# sets the speed of the animation not the speed at which the paddle moves
paddle_a.shape("square")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
# stretches the width 5 times of the default size (which is 20px X 20px)
paddle_a.color("white")
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.shape("square")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.speed(0)
paddle_b.color("white")
paddle_b.penup()
paddle_b.goto(350, 0)

# Pong - Ball
pongBall = turtle.Turtle()
pongBall.speed(0)
pongBall.goto(0, 0)
pongBall.shape("circle")
pongBall.color("white")
pongBall.penup()
pongBall.dx = 0.032
pongBall.dy = 0.032


# Functions to move paddles

def paddleAUp() :
    y = paddle_a.ycor()
    # ycor() is a turtle method which returns the y coordinate of a turtle object
    y += 20
    # Adding 20 px to the y coordinate
    paddle_a.sety(y)
    # setting 20 px to the y coordinate of the paddle a


def paddleADown() :
    y = paddle_a.ycor()
    # ycor() is a turtle method which returns the y coordinate of a turtle object
    y -= 20
    # Subtracting 20 px from the y coordinate
    paddle_a.sety(y)
    # setting 20 px to the y coordinate of the paddle a


def paddleBUp() :
    y = paddle_b.ycor()
    # ycor() is a turtle method which returns the y coordinate of a turtle object
    y += 20
    # Adding 20 px to the y coordinate
    paddle_b.sety(y)
    # setting 20 px to the y coordinate of the paddle b


def paddleBDown() :
    y = paddle_b.ycor()
    # ycor() is a turtle method which returns the y coordinate of a turtle object
    y -= 20
    # Subtracting 20 px from the y coordinate
    paddle_b.sety(y)
    # setting 20 px to the y coordinate of the paddle b


# Keyboard binding
win.listen()  # listens for keyboard inputs

win.onkeypress(paddleAUp, "w")
# after the listen() makes the window wait for the keyboard input, the above onkeypress() calls the paddleBUp()
# when the small w key is pressed
win.onkeypress(paddleADown, "s")
# after the listen() makes the window wait for the keyboard input, the above onkeypress() calls the paddleBDown()
# when the small s key is pressed

win.onkeypress(paddleBUp, "Up")
# after the listen() makes the window wait for the keyboard input, the above onkeypress() calls the paddleBUp()
# when the Up arrow key is pressed
win.onkeypress(paddleBDown, "Down")
# after the listen() makes the window wait for the keyboard input, the above onkeypress() calls the paddleBDown()
# when the Down arrow key is pressed
