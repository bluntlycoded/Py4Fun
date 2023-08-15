import colorsys
import turtle
t=turtle.Turtle()
t.speed(0)
s=turtle.Screen()
s.bgcolor("black")
s.title("Spiral Design")
n=36
h=0
for i in range(1000):
    h+=1
    if h==360:
        h=0
    t.pencolor(colorsys.hsv_to_rgb(i/360,1.0,1.0))
    t.circle(i)
    t.left(n)
    t.width(2)
    t.hideturtle()
    t.penup()
    t.goto(0,0)
    t.pendown()
    t.left(1)
t.done()
