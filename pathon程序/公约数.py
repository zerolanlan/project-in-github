print("请输入两个不同的整数：")
a=eval(input("请输入第一个整数："))
b=eval(input("请输入第二个整数："))
x=a
y=b
if(a<b):
    temp=x
    x=y
    y=temp
while y!=0:
    c=x%y
    x=y
    y=c
min=a*b/x
print("最小公倍数：{:.2f}".format(min))
print("最大公约数为:{:.2f}".format(x))
