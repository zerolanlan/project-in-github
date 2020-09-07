locationInfo={'510800':'成都市','510601':'市辖区','510821':'成华区'}
def  getIdInfo(idNum):
    birthday = list(idNum[6:14])
    sex = idNum[-2]
    location = [num[:6]]
    if int(sex)%2==0:
        gender = '女'
    else:
        gender = '男'
        return birthday,gender,locatin

myId='510821199901277456'
tuplel =getIdInfo(myId)
print(tuptel)
