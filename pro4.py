import turtle
counter = 0
turtle.shape('turtle')
num = int(input("몇각형입니까?"))
r = int(input("한변의길이는몇입니가?"))
for i in range(num):
    turtle.forward(r)
    turtle.right(360/num)
turtle.exitonclick()