from turtle import *
bgcolor('red')
begin_fill()
color('white')
circle(100)
end_fill()

goto(50,0)
begin_fill()
color('red')
circle(100)
end_fill()

goto(25,75)
color('white', 'white')
begin_fill()
points=1
while points<=5:
    forward(100)
    left(144)
    points = points +1
end_fill()
done()
