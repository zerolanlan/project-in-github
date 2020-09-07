dayup,dayfactor=1.0,0.01
for i in range(365):
    if i%16 in [3,4,5,6,10,11,12,13]:
        dayup=dayup*(1+dayfactor)
    else:
        dayup=dayup
print("ability：{}".format(dayup))

                            
