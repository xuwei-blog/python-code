import turtle as t
t.penup()
t.goto(-200,-50)
t.pendown()
t.begin_fill()
t.color('red')
t.circle(40,steps=3)    # 三角形
t.end_fill()


t.penup()
t.goto(-100,-50)
t.pendown()
t.begin_fill()
t.color('blue')
t.circle(40,steps=4)    # 四边形
t.end_fill()


t.penup()
t.goto(0,-50)
t.pendown()
t.begin_fill()
t.color('green')
t.circle(40,steps=5)    # 五边形
t.end_fill()

t.penup()
t.goto(100,-50)
t.pendown()
t.begin_fill()
t.color('purple')
t.circle(40,180)    #   半圆
t.end_fill()


t.hideturtle()
