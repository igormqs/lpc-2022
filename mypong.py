import turtle
import os
import pygame
pygame.init()
pygame.mixer.music.set_volume(0.1)
colisao = pygame.mixer.Sound("collision.mpeg")
colisao.set_volume(0.2)
musica = pygame.mixer.music.load("musica fundo.mpeg")
pygame.mixer.music.play(-1)
# draw scanner
screen = turtle.Screen()
screen.title("my pong")
screen.bgcolor("black")
screen.setup(width =800, height=600)
screen.tracer(0)
# table
table=turtle.Turtle()
table.shape("square")
table.color("green")
table.shapesize(stretch_wid=25,stretch_len=40)
table.penup()
table.goto(0,0)
# line
line = turtle.Turtle()
line.shape("square")
line.color("white")
line.shapesize(stretch_wid=25, stretch_len=0.5)
line.penup()
line.goto(0,0)

# draw  paddle 1
paddle_1 = turtle.Turtle()
paddle_1.speed(0)
paddle_1.shape("square")
paddle_1.color("blue")
paddle_1.shapesize(stretch_wid=5, stretch_len=1)
paddle_1.penup()
paddle_1.goto(-350,0)
# draw paddle 2
paddle_2 = turtle.Turtle()
paddle_2.speed(0)
paddle_2.shape("square")
paddle_2.color("red")
paddle_2.shapesize(stretch_wid=5, stretch_len=1)
paddle_2.penup()
paddle_2.goto(350,0)
# draw ball
ball=turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("blue")
ball.penup()
ball.goto(0,0)
ball.dx = 0.5
ball.dy =0.5
# score
score_1=0
score_2=0
#head-up display
hud=turtle.Turtle()
hud.speed(0)
hud.shape("square")
hud.color("white")
hud.penup()
hud.hideturtle()
hud.goto(0,260)
hud.write("0 : 0",align="center", font=("Press Start 2P",24,"normal"))

def paddle_1_up():
    y = paddle_1.ycor()
    if y < 250:
        y += 10
    else:
        y=250
    paddle_1.sety(y)
def paddle_1_down():
    y = paddle_1.ycor()
    if y>-250:
        y+=-10
    else:
        y=-250
    paddle_1.sety(y)
def paddle_2_up():
    y=paddle_2.ycor()
    if y<250:
        y+=10
    else:
        y=250
    paddle_2.sety(y)
def paddle_2_down():
    y=paddle_2.ycor()
    if y>-250:
        y+=-10
    else:
        y=-250
    paddle_2.sety(y)
screen.listen()
screen.onkeypress(paddle_1_up,"w")
screen.onkeypress(paddle_1_down,"s")
screen.onkeypress(paddle_2_up,"Up")
screen.onkeypress(paddle_2_down,"Down")

while True:
    screen.update()
    #ball movement
    ball.sety(ball.ycor() + ball.dy)
    ball.setx(ball.xcor()+ball.dx)
#    ball.sety(ball.ycor()+ball.dy)

    #collision with the upper wall
    if ball.ycor()>290:
        colisao.play()
        ball.sety(290)
        ball.dy*=-1
    #collision with the lower wall
    if ball.ycor()<-290:
        colisao.play()
        ball.sety(-290)
        ball.dy*=-1
    #colission with the left wall
    if ball.xcor()<-390:
        colisao.play()
        score_2+=1
        hud.clear()
        hud.write("{}:{}".format(score_1, score_2), align="center", font=("Press Start 2P",24,"normal"))
       # ball.goto(0,0)
        ball.dx*=-1
    #collision with the right wall
    if ball.xcor() > 390:
        colisao.play()
        score_1+=1
        hud.clear()
        hud.write("{}:{}".format(score_1, score_2), align="center", font=("Press Start 2P",24,"normal"))
        #ball.goto(0,0)
        ball.dx*= -1
    #collision with the paddle 1
    if (ball.xcor() <- 330 and ball.ycor() < paddle_1.ycor() + 50 and ball.ycor() > paddle_1.ycor() - 50):
        ball.dx*=-1
        colisao.play()
        ball.color("blue")
    #collision with the paddle 2
    if (ball.xcor() > 330 and ball.ycor() < paddle_2.ycor() + 50 and ball.ycor() > paddle_2.ycor() - 50):
        ball.dx*=-1
        colisao.play()
        ball.color("red")
