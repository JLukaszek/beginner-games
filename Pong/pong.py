import turtle

import winsound

window = turtle.Screen()
window.title("Pong Game")
window.bgcolor("black")
window.setup(width= 800, height= 600)
window.tracer(0)

# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape('square')
paddle_a.color('white')
paddle_a.shapesize(stretch_wid=7.0, stretch_len=0.5)
paddle_a.penup()
paddle_a.goto(-380, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape('square')
paddle_b.color('white')
paddle_b.shapesize(stretch_wid=7.0, stretch_len=0.5)
paddle_b.penup()
paddle_b.goto(380, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape('circle')
ball.color('white')
ball.penup()
ball.goto(0, 0)
ball.dx = 0.20
ball.dy = 0.20 

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write(f"Player A: {score_a}  Player B: {score_b}", align = 'center',font = ('Corier', 16, 'normal'))

# Functions
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


# Keyboard binding
window.listen()

window.onkeypress(paddle_a_up, 'w')
window.onkeypress(paddle_a_down, 's')

window.onkeypress(paddle_b_up, 'Up')
window.onkeypress(paddle_b_down, 'Down')

# Main game loop
while True:
    window.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
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
        pen.write(f"Player A: {score_a}  Player B: {score_b}", align = 'center',font = ('Corier', 16, 'normal'))
        winsound.PlaySound("pew.wav", winsound.SND_ASYNC)

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write(f"Player A: {score_a}  Player B: {score_b}", align = 'center',font = ('Corier', 16, 'normal'))
        winsound.PlaySound("pew.wav", winsound.SND_ASYNC)

    # Bounce
    if ball.xcor() > 340 and (ball.ycor() < paddle_b.ycor() + 55 and ball.ycor() > paddle_b.ycor() - 55):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    elif ball.xcor() < -340 and (ball.ycor() < paddle_a.ycor() + 60 and ball.ycor() > paddle_a.ycor() - 60):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)