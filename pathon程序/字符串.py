months="JanFebMarAprMayJunJulAugSepOctNovDec"
monthid=eval(input("请输入月份数字（1-12）："))
pos=(monthid-1)*3
print(months[pos:pos+3])
