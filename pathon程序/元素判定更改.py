 吧                                                                                                                                                                                                                                                                                                                                                                                def testlist():
    list=[]
    ls=input("请输入一个元素(直接输入回车退出)：")
    while ls!="":
        list.append(ls)
        ls=input("请输入一个元素(直接输入回车退出)：")
    S=set(list)
    if len(S)==len(list):
        print('False')
    else:
        print('Ture')
print("请输入若干元素以组成一个列表，如果列表里有重复元素则显示Ture，反之显示False")
testlist()
