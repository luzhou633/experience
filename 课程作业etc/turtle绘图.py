import math
import turtle
def one_angle(l):
    pen.left(72)
    pen.forward(l)
    pen.right(144)
    pen.forward(l)
def one_star(x,y,sa,r): #sa：偏转角
    L=(r*math.cos(math.radians(18)))/(1+math.sin(math.radians(18))) #通过外接圆半径算五角星边长
    pen.setheading(0) #初始画笔默认朝右
    pen.goto(x, y)
    pen.left(90-sa)   #旋转角度
    pen.forward(r)
    pen.pendown()
    pen.begin_fill()
    pen.right(162)
    pen.forward(L)
    for i in range(4):
        one_angle(L) #画五角星的四个角
    pen.left(72)
    pen.forward(L)
    pen.end_fill() #收笔
    pen.penup()
screen=turtle.Screen()
screen.setup(width=660,height=440)
screen.title("五星红旗")
pen=turtle.Turtle()
pen.speed(0)
pen.penup()
pen.color("red")
pen.begin_fill()
pen.goto(-300,200)
pen.pendown()
pen.goto(300,200)
pen.goto(300,-200)
pen.goto(-300,-200)
pen.goto(-300,200)
pen.end_fill()
pen.penup()
pen.color("yellow")
one_star(-200,100,0,60)#-300+5*(-300)/15,200-5*(200)/10 大五角星
one_star(-100,160,18,20)#第一颗小五角星
one_star(-60,120,-18,20)#第二颗小五角星
one_star(-60,60,0,20)#第三颗小五角星
one_star(-100,20,18,20)#第四颗小五角星
pen.hideturtle()
turtle.done()
