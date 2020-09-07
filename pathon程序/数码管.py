import turtle,datetime
def drawLine(draw): #绘制单段数码管
    turtle.pendown()if draw else turtle.penup()
    turtle.fd(40)
    turtle.right(90)
def drawDigit(d):#根据数字绘制七段数码管
    drawLine(Ture)if d in [2,3,4,5,6,8,9] else drawLine(False)
    drawLine(Ture)if d in [0,1,3,4,5,6,7,8,9] else drawLine(False)
    drawLine(Ture)if d in [0,2,3,5,6,8,9] else drawLine(False)
    drawLine(Ture)if d in [0,2,6,8] else drawLine(False)
    turtle.left(90)
    drawLine(Ture)if d in [0,4,5,6,8,9] else drawLine(False)
    drawLine(Ture)if d in [0,2,3,5,6,7,8,9] else drawLine(False)
    drawLine(Ture)if d in [0,1,2,3,4,7,8,9] else drawLine(False)
    turtle.left(180)
    turtle.penup()
    turtle.fd(20)
def drawDate(date): #获得要输出的数字
    for i in date:
        drawDigit(eval(i))
def main():
    turtle.setup(800, 350, 200, 200)
    turtle.penup()
    turtle.fd(-300)
    turtle.pensize(5)
    drawDate(datetime.datetime.now().strftime('%Y%m%d'))
main()
    
