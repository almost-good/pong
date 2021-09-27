import turtle
import winsound

wn = turtle.Screen() # create screen
wn.title("Pong by @almost_good")
wn.bgcolor("#333")
wn.setup(width=800, height=600)
wn.tracer(0) # stops the window from updating, this basically speeds up the game

# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0) # speed of animation, sets the speed to the max
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=0.5)
paddle_a.penup() 
paddle_a.goto(-350, 0) # start od paddle

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0) 
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=0.5)
paddle_b.penup() 
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0) 
ball.shape("circle")
ball.color("white")
ball.penup() 
ball.goto(0, 0)
ball.dx = 0.3
ball.dy = -0.3

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Breki_loser: 0 Maja_queen: 0", align="center", font=("Courier", 24, "normal"))

# Function move paddle a up
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

# Function move paddle a down
def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

# Function move paddle b up
def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

# Function move paddle b down
def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

# Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# Main game loop
while True:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1 # reverses the direction
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
    
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Breki_loser: {} Maja_queen: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
    
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Breki_loser: {} Maja_queen: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
    
    # Paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -40):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
