import random
num = random.randint(0,100)
n=0

while True:
        guess=eval(input("请输入你的猜测"))
        n+=1
        if guess > num:
                print("遗憾，比预设数大！")
        elif guess < num:
                print ("遗憾，比预设数小！")
        else:
            print ("预测的次数为:{}次，你猜中了！".format(n))


 
