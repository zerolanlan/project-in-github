
for i in range(11):
    if i % 5 == 0:
        for j in range(11):
            if j % 5 == 0:
                if j == 10:
                    print("+")
                else:
                    print("+",end="")
            else:
                print("-",end="")
    else:
        for k in range(11):
            if k % 5 == 0:
                if k == 10:
                    print("|")
                else:
                    print("|",end="")
            else:
                print(" ",end="")
