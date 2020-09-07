
def is_Print():
	a=int(input("input:"))
	#print(a)
	
	if a>1:#判断是否大于1
		for i in range(2,a):#循环
			if a%i==0:#循环相除
				#print("True")
				return False
			else:
				#print("False")
				return True
	else:#为1输出
		return True
print(is_Print())
