height,weight=eval(input("请输入1身高（米）和体重\(公斤)[逗号隔开]："））
bmi=weight/pow(height,2)
who,dom="",""
if bmi<18.5:    #WHO标准
    who="偏瘦"
elif bmi<25:    #18.5<=bmi<25
    who="正常"
