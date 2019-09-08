#Simple Game Ping Pong with Python3 Programming
#Coded By @sulton.exe
#TOLONG JANGAN RECODE YA :) HARGAI SI PEMBUAT TERIMA KASIH :D

import turtle
import os

#Set Screen
wn = turtle.Screen()
wn.title("Ping Pong Game By @sulton.exe")
wn.bgcolor("black")
wn.setup(width=700, height=500)
wn.tracer(0)


#Score
score_a = 0
score_b = 0

#paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-300, 0)

#paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(300, 0)

#ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("blue")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.4
ball.dy = -0.4

#Pen 
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 210)
pen.write("Player A: 0   Player B: 0", align="center", font=("courier", 24, "normal"))

#Function
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

#Keyboard Control
wn.listen()
wn.onkeypress(paddle_a_up, "z")
wn.onkeypress(paddle_a_down, "x")
wn.onkeypress(paddle_b_up, "n")
wn.onkeypress(paddle_b_down, "m")        

#Main Game Loop
while True:
    wn.update()

    #Move The Ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #border checking
    if ball.ycor() > 240:
        ball.sety(240)
        ball.dy *= -1
        os.system("aplay /home/sultonexe/Documents/Project/PythonPong/jumping.wav&")

    if ball.ycor() < -240:
        ball.sety(-240)
        ball.dy *= -1
        os.system("aplay /home/sultonexe/Documents/Project/PythonPong/jumping.wav&")

    if ball.xcor() > 340:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}   Player B: {}".format(score_a, score_b), align="center", font=("courier", 24, "normal"))

    if ball.xcor() < -340:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}   Player B: {}".format(score_a, score_b), align="center", font=("courier", 24, "normal"))

    #paddle and ball collisions
    if (ball.xcor() > 290 and ball.xcor() < 300) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(290)
        ball.dx *= -1
        os.system("aplay /home/sultonexe/Documents/Project/PythonPong/bounce1.wav&")

    if (ball.xcor() < -290 and ball.xcor() > -300) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-290)
        ball.dx *= -1
        os.system("aplay /home/sultonexe/Documents/Project/PythonPong/bounce1.wav&")