import os
import PIL
from PIL import Image,ImageTk,ImageDraw,ImageFont
from tkinter import *
from tkinter import filedialog,font
import imghdr
from aip import AipFace
import base64
import tkinter.messagebox
import math
import threading
import warnings
import copy
import time
class imgRecog(object):
    
    def __init__(self):
        self.topList = []
        self.topListImgs=[]
        self.allListImgs=[]
        self.root = Tk()
        self.root.resizable(0,0)  
        self.root.title("人脸检测")
        self.root.iconbitmap('b13.ico')
        self.root.geometry('1080x620')

        self.menu = Menu(self.root)
        self.menu.add_command(label='颜值排行榜',command=self.showTopList)
        self.root['menu']=self.menu

        originFrameBorder = Frame(self.root,height=500,width=500,bd =2,relief=GROOVE)
        originFrameBorder.grid(row=1,column=0,sticky=W,padx=20,pady=10)
        
        self.originFrame = Frame(originFrameBorder,height=500,width=500)
        self.originFrame.pack()


        resultFrameBorder = Frame(self.root,height=500,width=500,bd =2,relief=GROOVE)
        resultFrameBorder.grid(row=1,column=1,sticky=E,padx=20,pady=10)
        
        self.resultFrame = Frame(resultFrameBorder,height=500,width=500)
        self.resultFrame.pack()

        self.selectFrame = Frame(self.root,height=20,width=500)
        self.selectFrame.grid(row=2,column=0)
                
        self.infoFrame =  Frame(self.root,height=20,width=500)
        self.infoFrame.grid(row=2,column=1)        
        self.infoLabel =  Label(self.infoFrame,text='')
        self.infoLabel.pack()

        self.imageLabel = Label(self.selectFrame,text='图片路径：')
        self.imageLabel.grid(row=0,column=0)
        self.imageEntry = Entry(self.selectFrame,width=60)
        self.imageEntry.config(state=DISABLED)
        self.imageEntry.grid(row=0,column=1)

        self.selectFileButton = Button(self.root,width=20,height=1,text="选择图片",command=self.browseFile, relief=RIDGE)
        self.selectFileButton.grid(row=3,column=0,pady=10)
        self.detectButton = Button(self.root,width=20,height=1,text="检测", command=self.detect, relief=RIDGE)
        self.detectButton.grid(row=3,column=1,pady=10)

        self.tl = Toplevel()
        self.tl.withdraw()
        self.tl.title('颜值排行榜Top10')  
        self.tl.geometry('400x680')        
        self.tl.iconbitmap('b13.ico')
        self.tl.resizable(0,0)
        self.tl.protocol('WM_DELETE_WINDOW', self.closeTopList)
        self.frameList = []


        ft = font.Font(size=18)
        topListTitle = Label(self.tl,text="排行榜Top10",font=ft)
        topListTitle.pack()
        
        canvas=Canvas(self.tl,width=400,height=600,scrollregion=(0,0,450,1600)) #创建canvas
        canvas.pack() #放置canvas的位置
        
        topListButton = Button(self.tl,width=20,height=1,text="查看所有",relief=RIDGE,command=self.showAllList)
        topListButton.pack(pady=10)
        
        self.contentFrame=Frame(canvas) #把frame放在canvas里
        self.contentFrame.pack() #frame的长宽，和canvas差不多的
        vbar=Scrollbar(canvas,orient=VERTICAL) #竖直滚动条
        vbar.place(x = 380,width=20,height=600)
        vbar.configure(command=canvas.yview)
        canvas.config(yscrollcommand=vbar.set) #设置  
        canvas.create_window((0,0), window=self.contentFrame,anchor=N+W)  #create_window

        
        self.allList= Toplevel()
        self.allList.withdraw()
        self.allList.title('颜值排行榜(全)')  
        self.allList.geometry('800x640')        
        self.allList.iconbitmap('b13.ico')        
        self.allList.resizable(0,0)
        self.allList.protocol('WM_DELETE_WINDOW', self.closeAllList)

        ft = font.Font(size=18)
        allListTitle = Label(self.allList,text="所有榜单",font=ft)
        allListTitle.pack()

        
        
        self.root.mainloop()

    def closeTopList(self):
        self.tl.withdraw()
    def closeAllList(self):
        self.allList.withdraw()

    def showAllList(self):
        self.allList.destroy()
        self.allList= Toplevel()
        self.allList.title('颜值排行榜(全)')  
        self.allList.geometry('800x680')        
        self.allList.iconbitmap('b13.ico')        
        self.allList.resizable(0,0)
        self.allList.protocol('WM_DELETE_WINDOW', self.closeAllList)

        ft = font.Font(size=18)
        allListTitle = Label(self.allList,text="所有榜单",font=ft)
        allListTitle.pack()
        self.allListImgs=[]
        canvas2=Canvas(self.allList,width=800,height=640,scrollregion=(0,0,800,(len(self.topList)//4)*300+300)) #创建canvas
        canvas2.pack() #放置canvas的位置
        
        self.contentFrame2=Frame(canvas2) #把frame放在canvas里
        self.contentFrame2.pack() #frame的长宽，和canvas差不多的
        vbar=Scrollbar(canvas2,orient=VERTICAL) #竖直滚动条
        vbar.place(x = 780,width=20,height=640)
        vbar.configure(command=canvas2.yview)
        canvas2.config(yscrollcommand=vbar.set) #设置  
        canvas2.create_window((0,0), window=self.contentFrame2,anchor=N+W)  #create_window
        for i in range(len(self.topList)):
            frame = Frame(self.contentFrame2,height=250,width=170,bg='white',bd =2,relief=GROOVE)
            frame.grid(row=i//4,column=i%4,padx=10,pady=20)
            rank = Label(frame,text='第{}名'.format(i+1),bg='white')
            rank.place(x=65,y=0)
        for i in range(len(self.topList)):
            
            frame = Frame(self.contentFrame2,height=250,width=170,bg='white',bd =2,relief=GROOVE)
            frame.grid(row=i//4,column=i%4,padx=10,pady=20)
            
            item = self.topList[i]
            img = PIL.Image.open(item['img'])
            img.thumbnail((80,80))
            self.allListImgs.append(ImageTk.PhotoImage(img))
            photolabel = Label(frame,image=self.allListImgs[i])
            photolabel.pack()        
            beautylabel = Label(frame,text='颜值：'+str(item['beauty']),bg='white')
            beautylabel.pack() 
            agelabel = Label(frame,text='年龄：'+str(item['age']),bg='white')
            agelabel.pack() 
            genderlabel = Label(frame,text='性别：'+item['gender'],bg='white')
            genderlabel.pack() 
            glasseslabel=Label(frame,text='眼镜：'+item['glasses'],bg='white')
            glasseslabel.pack() 
            face_probabilitylabel = Label(frame,text='置信度：'+str(item['face_probability']),bg='white')
            face_probabilitylabel.pack() 

            
    def showTopList(self):
        self.tl.deiconify()
        
        self.topListImgs=[]
        for i in range(10):
            frame = Frame(self.contentFrame,height=250,width=170,bg='white',bd =2,relief=GROOVE)
            frame.grid(row=i//2,column=i%2,padx=10,pady=20)
            rank = Label(frame,text='第{}名'.format(i+1),bg='white')
            rank.place(x=65,y=0)

        for i in range(len(self.topList) if len(self.topList)<10 else 10):
            
            frame = Frame(self.contentFrame,height=250,width=170,bg='white',bd =2,relief=GROOVE)
            frame.grid(row=i//2,column=i%2,padx=10,pady=20)
            
            item = self.topList[i]
            img = PIL.Image.open(item['img'])
            img.thumbnail((80,80))
            self.topListImgs.append(ImageTk.PhotoImage(img))
            photolabel = Label(frame,image=self.topListImgs[i])
            photolabel.pack()        
            beautylabel = Label(frame,text='颜值：'+str(item['beauty']),bg='white')
            beautylabel.pack() 
            agelabel = Label(frame,text='年龄：'+str(item['age']),bg='white')
            agelabel.pack() 
            genderlabel = Label(frame,text='性别：'+item['gender'],bg='white')
            genderlabel.pack() 
            glasseslabel=Label(frame,text='眼镜：'+item['glasses'],bg='white')
            glasseslabel.pack() 
            face_probabilitylabel = Label(frame,text='置信度：'+str(item['face_probability']),bg='white')
            face_probabilitylabel.pack() 
            
    def browseFile(self):
        
        warnings.simplefilter('ignore', PIL.Image.DecompressionBombWarning)
        fileDir = filedialog.askopenfilename(initialdir =os.curdir)
        if fileDir!='':            
            if self.isPic(fileDir=fileDir):                
                self.imageEntry.config(state=NORMAL)
                self.imageEntry.delete(0,END)
                self.imageEntry.insert(0,fileDir)
                self.imageEntry.config(state=DISABLED)
                img = PIL.Image.open(fileDir)
                img.thumbnail((500,500))
                self.originImage = ImageTk.PhotoImage(img)
                self.label_imgo = Label(self.originFrame,image=self.originImage)
                self.label_imgo.place(x=250,y=250,anchor = CENTER)
                size = os.path.getsize(fileDir)
                self.infoLabel['text']='图片大小：'+ self.formatSize(size=size)
            else:
                self.infoLabel['fg']='red'
                self.infoLabel['text']='错误：图片格式不正确!(支持格式：jpg,jpeg,png,bmp,tiff)'
                
    def detect(self):
        if self.imageEntry.get()=='':
            self.infoLabel['fg']='red'
            self.infoLabel['text']='错误：请选择一张图片!'
        elif self.isPic(fileDir=self.imageEntry.get()):
            fileDir = self.imageEntry.get()
            if os.path.getsize(fileDir)>=10485760:
                if tkinter.messagebox.askokcancel('提示', '图片太大，需压缩至10MB以下，点击确定执行自动压缩'):                    
                    th1 = threading.Thread(target = self.resizeTo10,args=(fileDir,))
                    th1.start()
            else:
                self.infoLabel['fg']='black'
                self.infoLabel['text']='正在分析图片'
                th1 = threading.Thread(target=self.analyseImage,args=(fileDir,))
                th1.start()
    def isPic(self,fileDir):
        fileType = imghdr.what(fileDir)
        picTypes = ['jpg','jpeg','png','bmp','tiff']
        if fileType in picTypes:
            return True
        else:
            return False
        
    def formatSize(self,size):
        strSize = ''
        if size<1024:
            strSize = '{}B'.format(size)
        elif size<1048576:
            strSize = '{:.2f}KB'.format(size/1024)
        elif size<1073741824:
            strSize = '{:.2f}MB'.format(size/1048576)
        return strSize
    
    def analyseImage(self,fileDir):
        try:       
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
            error_code = result['error_code']
            error_msg = result['error_msg']
            if error_code==0:
                face_num = result['result']['face_num']
                face_list = result['result']['face_list']
                img = PIL.Image.open(fileDir)
                draw=ImageDraw.Draw(img)
                font = ImageFont.truetype("AdobeFangsongStd-Regular.otf",20)
                if not os.path.exists(os.curdir+'/temp'):
                    os.makedirs(os.curdir+'/temp')
                currentTime = time.strftime("%Y-%m-%d-%H-%M-%S",time.localtime(time.time()))
                if not os.path.exists(os.curdir+'/temp/topList/'+currentTime):
                    os.makedirs(os.curdir+'/temp/topList/'+currentTime)
                print(fileDir)
                filepath,shotname,extension =self.get_filePath_fileName_fileExt(filename=fileDir)
                for i in range(face_num):
                    #获取参数
                    face_probability = '%.2f' % face_list[i]['face_probability']
                    age = face_list[i]['age']
                    beauty = '%.2f' % face_list[i]['beauty']
                    gender = '男' if face_list[i]['gender']['type']=='male' else '女'
                    face_token = face_list[i]['face_token']
                    left = face_list[i]['location']['left']
                    top = face_list[i]['location']['top']
                    width = face_list[i]['location']['width']
                    height = face_list[i]['location']['height']
                    rotation = face_list[i]['location']['rotation']
                    if face_list[i]['glasses']['type']=='common':
                        glasses = '普通镜' 
                    elif face_list[i]['glasses']['type']=='sun':
                        glasses = '墨镜'
                    else :
                        glasses = '无眼镜'
                    #添加到toplist
                    topListExist=False
                    for j in self.topList:
                        if face_token==j['face_token']:
                            topListExist=True
                    if not topListExist:                    
                        region=(left-50,top-50,left+width+50,top+height+50)
                        cropImg = img.crop(region)
                        print(os.curdir)
                        print(shotname)
                        print(extension)
                        print(os.curdir+'/temp/topList/'+currentTime+'/'+shotname+'-'+str(i)+extension)
                        cropImg.save(os.curdir+'/temp/topList/'+currentTime+'/'+shotname+'-'+str(i)+extension)
                        self.topList.append({
                            'face_token':face_token,
                            'age':age,
                            'beauty':float(beauty),
                            'gender':gender,
                            'face_probability':face_probability,
                            'glasses':glasses,
                            'img':os.curdir+'/temp/topList/'+currentTime+'/'+shotname+'-'+str(i)+extension
                             })
                    #绘制方框    
                    draw.polygon(self.rectwithRotation(left,top,width,height,rotation),outline="red")
                    x = left
                    y = top + height
                    draw.rectangle((left,top+height,left+110,top+height+100),fill='white')
                    draw.text((x,y),"年龄:"+str(age),fill='black', font=font)
                    draw.text((x,y+20),"性别:"+str(gender),fill='black', font=font)
                    draw.text((x,y+40),"颜值:"+str(beauty),fill='black', font=font)
                    draw.text((x,y+60),"眼镜:"+str(glasses),fill='black', font=font)
                    draw.text((x,y+80),"置信:"+str(face_probability),fill='black', font=font)      
                self.topList.sort(key=lambda x: x['beauty'],reverse=True)
                img.save(os.curdir+'/temp/new'+shotname+extension)
                self.img = PIL.Image.open(os.curdir+'/temp/new'+shotname+extension)
                self.scale=1
                thumb = copy.copy(self.img)
                thumb.thumbnail((500,500))
                self.resultImage = ImageTk.PhotoImage(thumb)
                self.label_img = Label(self.resultFrame,image=self.resultImage)
                imgW = thumb.size[0]
                imgH = thumb.size[1]
                self.imgX = (500-imgW)/2
                self.imgY = (500-imgH)/2
                self.label_img.place(x=self.imgX,y=self.imgY)
                self.label_img.bind("<MouseWheel>", self.processWheel)
                self.label_img.bind("<Button-1>", self.processMousedown)
                self.label_img.bind("<B1-Motion>", self.processMotion)
                self.infoLabel['fg']='black'
                self.infoLabel['text']='图片分析完毕'
            else:
                self.infoLabel['fg']='red'
                self.infoLabel['text']='错误：'+error_msg+' 错误码：'+str(error_code)
        except:
            self.infoLabel['fg']='red'
            self.infoLabel['text']='图片分析出错，请重新尝试'
        return result
    def processWheel(self,event):
        if event.delta>0:
            self.scale*=1.1
            thumb = copy.copy(self.img)
            thumb.thumbnail((500*self.scale,500*self.scale))
            self.resultImage = ImageTk.PhotoImage(thumb)
            self.label_img['image'] = self.resultImage
            self.label_img.place(x=self.imgX,y=self.imgY)
            self.label_img.bind("<MouseWheel>", self.processWheel)
            self.label_img.bind("<Button-1>", self.processMousedown)
            self.label_img.bind("<B1-Motion>", self.processMotion)
            print('放大')
        else:
            self.scale/=1.1
            thumb = copy.copy(self.img)
            thumb.thumbnail((500*self.scale,500*self.scale))
            self.resultImage = ImageTk.PhotoImage(thumb)
            self.label_img['image'] = self.resultImage
            self.label_img.place(x=self.imgX,y=self.imgY)
            self.label_img.bind("<MouseWheel>", self.processWheel)
            self.label_img.bind("<Button-1>", self.processMousedown)
            self.label_img.bind("<B1-Motion>", self.processMotion)
            print('缩小')
    def processMousedown(self,event):
        self.lastX=event.x
        self.lastY=event.y
    def processMotion(self,event):
        moveX = event.x-self.lastX
        moveY = event.y-self.lastY
        self.imgX += moveX
        self.imgY += moveY
        self.label_img.place(x=self.imgX,y=self.imgY)
        self.lastX=event.x
        self.lastY=event.y
    def resizeTo10(self,imagePath):
        a=os.path.getsize(imagePath)        
        self.infoLabel['fg']='black'
        self.infoLabel['text']='正在压缩图片'+self.formatSize(a)
        image = PIL.Image.open(imagePath)
        b=image.size
        reimage=image.resize((int(b[0]*0.9),int(b[1]*0.9)))
        filepath,shotname,extension = self.get_filePath_fileName_fileExt(filename=imagePath)
        if not os.path.exists(os.curdir+'/temp'):
            os.makedirs(os.curdir+'/temp') 
        newpath = os.curdir+'/temp/'+shotname+'Resized'+extension
        reimage.save(newpath)
        print(os.path.getsize(newpath))
        while os.path.getsize(newpath)>10485760:
            print(os.path.getsize(newpath))
            a = os.path.getsize(newpath)
            self.infoLabel['fg']='black'
            self.infoLabel['text']='正在压缩图片'+self.formatSize(a)
            photo=PIL.Image.open(newpath)
            c=photo.size
            rephoto=photo.resize((int(c[0]*0.9),int(c[1]*0.9)))
            rephoto.save(newpath)
        self.infoLabel['fg']='black'
        self.infoLabel['text']='压缩成功,正在分析图片,图片大小:'+self.formatSize(os.path.getsize(newpath))
        th2 = threading.Thread(target=self.analyseImage,args=(newpath,))
        th2.start()
        return newpath
    def get_filePath_fileName_fileExt(self,filename):  
        (filepath,tempfilename) = os.path.split(filename);  
        (shotname,extension) = os.path.splitext(tempfilename);  
        return filepath,shotname,extension
    
    def pointRotate(self,x,y,rx0,ry0,r):
        x0 = (x-rx0)*math.cos(r*math.pi/180) - (y-ry0)*math.sin(r*math.pi/180) + rx0
        y0 = (x-rx0)*math.sin(r*math.pi/180) + (y-ry0)*math.cos(r*math.pi/180) + ry0
        return x0,y0
    
    def rectwithRotation(self,left,top,width,height,rotate):
        x1,y1 =left,top
        a2=left+width
        b2=top
        a3=left+width
        b3=top+height
        a4=left
        b4=top+height
        x2,y2 = self.pointRotate(a2,b2,x1,y1,rotate)
        x3,y3 = self.pointRotate(a3,b3,x1,y1,rotate)
        x4,y4 = self.pointRotate(a4,b4,x1,y1,rotate)
        return x1,y1,x2,y2,x3,y3,x4,y4

if __name__ == '__main__':
    imgRecog()
    
