import turtle
import os

# Creating window
win = turtle.Screen()
win.title('Pong by @annieC')
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)
# this prevents the window from auto updating and makes the game faster - we can update the window manually now.

# Score Variables
score_a = 0
score_b = 0

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

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
# This is near the top border
pen.write("Player A : 0     Player B : 0", align="center", font=("Courier", 24, "normal"))


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

# Main game loop
while max(score_a, score_b) <= 20 :
    win.update()
    #   Updates the screen every time the loop runs / executes
    #   Inside the screen, (0,0) is at the center and 400px to the right and 400px to the left from (0,0)
    #   make up the width and 300px from the top and 300 px from the bottom make up the height of the window.

    pongBall.setx(pongBall.xcor() + pongBall.dx)
    pongBall.sety(pongBall.ycor() + pongBall.dy)

    # Move ball done

    # Border checking starts

    # For the top and down borders

    if pongBall.ycor() > 290 :  # as the max positive y coord. is 300
        pongBall.sety(290)  # we set the ball's y coord. as maximum
        pongBall.dy *= -1  # and then change it's direction

    if pongBall.ycor() < -290 :
        pongBall.sety(-290)
        pongBall.dy *= -1

    # For the left and right borders

    if pongBall.xcor() > 390 :
        pongBall.goto(0, 0)
        pongBall.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A : {}     Player B : {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    if pongBall.xcor() < -390 :
        pongBall.goto(0, 0)
        pongBall.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A : {}     Player B : {}".format(score_a, score_b), align="center",
                  font=("Courier", 24, "normal"))

    # Paddle and ball collisions

    if (340 < pongBall.xcor() < 350) and (paddle_b.ycor() + 50 > pongBall.ycor() > paddle_b.ycor() - 50) :
        pongBall.setx(330)
        pongBall.dx *= -1
        os.system("aplay ball_bounce.wav&")

    if (-340 > pongBall.xcor() > -350) and (paddle_a.ycor() + 50 > pongBall.ycor() > paddle_a.ycor() - 50) :
        pongBall.setx(-330)
        pongBall.dx *= -1
        os.system("aplay ball_bounce.wav&")
