from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
from time import strftime
from datetime import datetime
from student import *

class Face_Recognition:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")

        #title
        title_lbl = Label(self.root,text = "FACE RECOGNITION PROCESS",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        img_left = Image.open(r"Images\learnData.png")
        img_left = img_left.resize((1530,780))
        self.Photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(self.root,image=self.Photoimg_left)
        f_lbl.place(x=0,y=45,width=1530,height=780)

        btn1_1 = Button(self.root,text="Face Recognition",command=self.face_recog,cursor="hand2",font=("times new roman",30,"bold"),bg="darkblue",fg="white")
        btn1_1.place(x=630,y=100,width=280,height=48)
    # ****************attendance**********************
    def mark_attendance(self,i,r,n,d):
        with open("attendance.csv","r+",newline="\n") as f:
            myDataList = f.readlines()
            name_List=[] 
            for line in myDataList:
                entry=line.split((","))
                name_List.append(entry[0])
            if((i not in name_List) and (r not in name_List) and (n not in name_List) and (d not in name_List)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString = now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Present")

    
    #*****************face recognition****************

    def face_recog(self):
        def draw_boundary(img,classifier,scaleFactor,minNeighbours,color,text,clf):
            gray_image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image,scaleFactor,minNeighbours)

            coord=[]

            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))

                conn=mysql.connector.connect(host="localhost",username="root",password="prajapati@1998",database="face_recognition")
                my_cursor=conn.cursor()

                my_cursor.execute("select Name from student where Student_id="+str(id))
                n = my_cursor.fetchone()
                if n is not None:
                    n = "+".join(n)
                else:
                    n="Unknown"
                
                my_cursor.execute("select RollNo from student where Student_id="+str(id))
                r = my_cursor.fetchone()
                if r is not None:
                    r = "+".join(r)
                else:
                    r = "Unknown"

                my_cursor.execute("select Dep from student where Student_id="+str(id))
                d = my_cursor.fetchone()
                if d is not None:
                    d = "+".join(d)
                else:
                    d = "Unknown"
                
                my_cursor.execute("select Student_id from student where Student_id="+str(id))
                i = my_cursor.fetchone()
                if i is not None:
                    i = "+".join(i)
                else:
                    i = "Unknown"

                if confidence>77:

                    cv2.putText(img,f"Id:{i}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"RollNo:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_attendance(i,r,n,d)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                coord = [x,y,w,h]

            return coord
        
        def recognize(img,clf,faceCascade):
            coord=draw_boundary(img,faceCascade,1.1,10,(255,255,255),"Face",clf)
            return img
        
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        videoCap=cv2.VideoCapture(0)

        while True:
            success,img=videoCap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome to face recognition",img)

            if cv2.waitKey(1)== 13:
                break
        videoCap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()