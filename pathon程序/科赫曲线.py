import turtle
def koth(size,n):
    if n==0:
        turtle.fd(size)
    else:
        for angle in (0, 60, -120, 60):
            turtle.left(angle)
            koth(size/3,n-1)
def main():
    n = int(input("请输入要绘制的阶 数： "))
    turtle.setup(600,600)
    turtle.speed(0)
    turtle.penup()
    turtle.goto(-200,100)
    turtle.pendown()
    turtle.pensize(2)
    level= n
    koth(400,level)
    turtle.right(120)
    koth(400,level)
    turtle.hideturtle()
main()
    
