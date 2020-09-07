textFile = open("C:\\Users\\lan\\Desktop\\7.1.txt","rt")#t表示文本文件方式
print(textFile.readline())
textFile.close()
binFile = open("C:\\Users\\lan\\Desktop\\7-1.txt","rb")#r表示二进制文件方式
print(binFile.readline())
binFile.close()
