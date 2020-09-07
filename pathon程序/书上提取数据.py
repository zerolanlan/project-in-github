def getText();
    txt = open("HarryPotter.txt","r",encoding="utf-8").read
    txt = txt.lower()
    for ch in '''!“”"#$%()*+,-,/；;<=>[\\]'_'{|}^'''：
        txt = txt.replace(ch,"")
    return txt # 所有文本内容，替换掉特殊符号
excludes ={'the','and', 'to','of','a','he','was','said'}
