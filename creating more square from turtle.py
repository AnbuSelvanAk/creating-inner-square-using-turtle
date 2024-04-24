from turtle import *
a=Screen()
x=Turtle()
def test(s):
    for i in range(4):
        x.fd(s)
        x.left(90)
        s=s-5
test(150)
test(130)
test(110)