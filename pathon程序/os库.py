import os
print(os.path.getsize("7.1.txt"))
textFile = open(os.path.abspath("7.1.txt"),"rt")
text = textFile.read()
print(text)
textFile.close()

binFile = open(os.path.abspath("7.1.txt"),"rb")
text = binFile.read()
print(text)
binFile.close()
