import os
import PIL
from PIL import Image,ImageTk,ImageDraw,ImageFont
from tkinter import *
from tkinter import filedialog,font
from aip import AipFace
import base64
import imghdr
import math
import warnings
import copy

def pointRotate(x,y,rx0,ry0,r):
    x0 = (x-rx0)*math.cos(r*math.pi/180) - (y-ry0)*math.sin(r*math.pi/180) + rx0
    y0 = (x-rx0)*math.sin(r*math.pi/180) + (y-ry0)*math.cos(r*math.pi/180) + ry0
    return x0,y0
def rectwithRotation(left,top,width,height,rotate):
    x1,y1 =left,top
    a2=left+width
    b2=top
    a3=left+width
    b3=top+height
    a4=left
    b4=top+height
    x2,y2 = pointRotate(a2,b2,x1,y1,rotate)
    x3,y3 = pointRotate(a3,b3,x1,y1,rotate)
    x4,y4 = pointRotate(a4,b4,x1,y1,rotate)
    return x1,y1,x2,y2,x3,y3,x4,y4
def isPic(fileDir):
    fileType = imghdr.what(fileDir)
    picTypes = ['jpg','jpeg','png','bmp','tiff','ico']
    if fileType in picTypes:
        return True
    else:
        return False
def formatSize(size):
    strSize = ''
    if size<1024:
        strSize = '{}B'.format(size)
    elif size<1048576:
        strSize = '{:.2f}KB'.format(size/1024)
    elif size<1073741824:
        strSize = '{:.2f}MB'.format(size/1048576)
    return strSize
def browseFile():
    global imageEntry,originImage,label_imgo,infoLabel,originFrame
    warnings.simplefilter('ignore', PIL.Image.DecompressionBombWarning)
    fileDir = filedialog.askopenfilename(initialdir =os.curdir)
    if fileDir!='':            
        if isPic(fileDir=fileDir):                
            imageEntry.config(state=NORMAL)
            imageEntry.delete(0,END)
            imageEntry.insert(0,fileDir)
            imageEntry.config(state=DISABLED)
            img = PIL.Image.open(fileDir)
            img.thumbnail((500,500))
            originImage = ImageTk.PhotoImage(img)
            label_imgo = Label(originFrame,image=originImage)
            label_imgo.place(x=250,y=250,anchor = CENTER)
            size = os.path.getsize(fileDir)
            infoLabel['text']='图片大小：'+ formatSize(size=size)
        else:
            infoLabel['fg']='red'
            infoLabel['text']='错误：图片格式不正确!(支持格式：jpg,jpeg,png,bmp,tiff,ico)'

def detect():
    global imageEntry,resultImage,label_img,infoLabel
    fileDir = imageEntry.get()
    APP_ID = '11275370'
    API_KEY = '181Wzp3m6V6mrDwDjLg4qcS5'
    SECRET_KEY = 'vuVpNOck5CpIDjv9Z9w5AyPohhjfBGTK'

    client = AipFace(APP_ID, API_KEY, SECRET_KEY)
    options = {}
    options["face_field"] = "age,beauty,gender,glasses"
    options["max_face_num"] = 10
    options["face_type"] = "LIVE"

    imageUrl = fileDir
    file = open(imageUrl, 'rb').read()
    bs = base64.b64encode(file)
    image = bytes.decode(bs)
    imageType = "BASE64"
    result = client.detect(image, imageType,options)
    print(result)
    filepath,shotname,extension = get_filePath_fileName_fileExt(imageUrl)
    error_code = result['error_code']
    error_msg = result['error_msg']
    if error_code==0:
        face_num = result['result']['face_num']
        face_list = result['result']['face_list']
        img = PIL.Image.open(imageUrl)
        draw=ImageDraw.Draw(img)
        font = ImageFont.truetype("AdobeFangsongStd-Regular.otf",20)
        for i in range(face_num):        
            face_probability = '%.2f' % face_list[i]['face_probability']
            age = face_list[i]['age']
            beauty = '%.2f' % face_list[i]['beauty']
            gender = face_list[i]['gender']['type']
            glasses = face_list[i]['glasses']['type']
            print("{}号人脸置信度：{} 年龄：{} 颜值：{} 性别：{} 眼镜：{}".format(i+1,face_probability,age,beauty,gender,glasses))
            if float(face_probability)>=0.5:            
                left = face_list[i]['location']['left']
                top = face_list[i]['location']['top']
                width = face_list[i]['location']['width']
                height = face_list[i]['location']['height']
                rotation = face_list[i]['location']['rotation']
                draw.polygon(rectwithRotation(left,top,width,height,rotation),outline="red")
                x = left
                y = top + height
                draw.rectangle((left,top+height,left+100,top+height+100),fill='white')
                draw.text((x,y),"年龄:"+str(age),fill='black', font=font)
                draw.text((x,y+20),"性别:"+str(gender),fill='black', font=font)
                draw.text((x,y+40),"颜值:"+str(beauty),fill='black', font=font)
                draw.text((x,y+60),"眼镜:"+str(glasses),fill='black', font=font)
                draw.text((x,y+80),"置信:"+str(face_probability),fill='black', font=font)
        img.save(os.curdir+'/new'+shotname+extension)
        thumb = copy.copy(img)
        thumb.thumbnail((500,500))
        resultImage = ImageTk.PhotoImage(thumb)
        label_img = Label(resultFrame,image=resultImage)
        imgW = thumb.size[0]
        imgH = thumb.size[1]
        imgX = (500-imgW)/2
        imgY = (500-imgH)/2
        label_img.place(x=imgX,y=imgY)
        infoLabel['fg']='black'
        infoLabel['text']='图片分析完毕'

        
    else:
        print("图片解析错误！错误码：{} 错误信息：{}".format(error_code,error_msg))
        
def get_filePath_fileName_fileExt(filename):  
    (filepath,tempfilename) = os.path.split(filename)
    (shotname,extension) = os.path.splitext(tempfilename)
    return filepath,shotname,extension


root = Tk()
root.resizable(0,0)  
root.title("人脸检测")
root.iconbitmap('b13.ico')
root.geometry('1080x620')

menu = Menu(root)
menu.add_command(label='颜值排行榜')
root['menu']= menu

originFrameBorder = Frame(root,height=500,width=500,bd =2,relief=GROOVE)
originFrameBorder.grid(row=1,column=0,sticky=W,padx=20,pady=10)

originFrame = Frame(originFrameBorder,height=500,width=500)
originFrame.pack()


resultFrameBorder = Frame(root,height=500,width=500,bd =2,relief=GROOVE)
resultFrameBorder.grid(row=1,column=1,sticky=E,padx=20,pady=10)

resultFrame = Frame(resultFrameBorder,height=500,width=500)
resultFrame.pack()

selectFrame = Frame(root,height=20,width=500)
selectFrame.grid(row=2,column=0)
        
infoFrame =  Frame(root,height=20,width=500)
infoFrame.grid(row=2,column=1)        
infoLabel =  Label(infoFrame,text='')
infoLabel.pack()

imageLabel = Label(selectFrame,text='图片路径：')
imageLabel.grid(row=0,column=0)
imageEntry = Entry(selectFrame,width=60)
imageEntry.config(state=DISABLED)
imageEntry.grid(row=0,column=1)

selectFileButton = Button(root,width=20,height=1,text="选择图片",command=browseFile, relief=RIDGE)
selectFileButton.grid(row=3,column=0,pady=10)
detectButton = Button(root,width=20,height=1,text="检测", command=detect, relief=RIDGE)
detectButton.grid(row=3,column=1,pady=10)

root.mainloop()
