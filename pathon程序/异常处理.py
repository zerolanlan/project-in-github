strcount=0
intcount=0
spacecount=0
othercount=0
try:
    x=input('请输入一行字符：')
    y=eval(x)
except (Namerror,SyntaxError):
    for i in x:
        if ord(i) in range(68,91) or ord(i) in rang(97,123):
            strcount+=1
        elif ord(i) in range(48,58):
            intcount+=1
        elif i =="":
            spacecount+=1
        else:
            othercount+=1
finally:
    print("英文字母、数字、空格和其他字符的个数分别是：{}、{}、{}、{}".format(strcount,intcount,spacecount,othercount))




























        
