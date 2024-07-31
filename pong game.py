
import turtle
wn=turtle.Screen()
wn.title("digital ping pong")
wn.bgcolor("black")
wn.setup(width=800,height=600)
wn.tracer(0)

# Paddle -1 
p1=turtle.Turtle()
p1.speed(0)
p1.shape("square")
p1.color("white")
p1.penup()
p1.goto(-350,0)
p1.shapesize(stretch_wid=5,stretch_len=1)





# Paddle -2
p2=turtle.Turtle()
p2.speed(0)
p2.shape("square")
p2.color("white")
p2.penup()
p2.goto(350,0)
p2.shapesize(stretch_wid=5,stretch_len=1)


# Ball
ball=turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx=0.4
ball.dy=-0.4

# move paddle 1 up
def paddle1up():
    y=p1.ycor()
    y +=20
    p1.sety(y)

def paddle1down():
    y=p1.ycor()
    y-=20
    p1.sety(y)

def paddle2up():
    y=p2.ycor()
    y+=20
    p2.sety(y)

def paddle2down():
    y=p2.ycor()
    y-=20
    p2.sety(y)
def quitgame():
    wn.bye()
#keyboard binding
wn.listen()
wn.onkeypress(paddle1up,"w")
wn.onkeypress(paddle1down,"s")
wn.onkeypress(paddle2up,"Up")
wn.onkeypress(paddle2down,"Down")
wn.onkeypress(quitgame,"q")

while True:
    wn.update()
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # North border check
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1 #reverse direction
    if ball.ycor()<-290:
        ball.sety(-290)
        ball.dy *= -1 #reverse direction

    # x axis is 800 total so -400 to 400
    if ball.xcor()>350:
        ball.goto(0,0)
        ball.dx *= -1
    if ball.xcor()<-350:
        ball.goto(0,0)
        ball.dy *= -1
    

    if (ball.xcor()>340 and ball.xcor()<350) and (ball.ycor()<p2.ycor()+50 and ball.ycor()>p2.ycor()-50):
        ball.setx(340)
        ball.dx *= -1
    
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < p1.ycor() + 50 and ball.ycor() > p1.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1









