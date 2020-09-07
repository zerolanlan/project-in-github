dayup,dayfactory=1.0,0.01
for i in range(365):
        if i%7 in[0,1,2]:
            dayup=dayup
        else:
            dayup+=dayup*dayfactory
print("连续学习365天后的能力值为:{}".format(dayup))
