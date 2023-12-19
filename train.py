from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np

class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")


        #title
        title_lbl = Label(self.root,text = "TRAIN DATA SET",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)



        img_left = Image.open(r"Images\learnData.png")
        img_left = img_left.resize((1530,780))
        self.Photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(self.root,image=self.Photoimg_left)
        f_lbl.place(x=0,y=45,width=1530,height=780)

        btn1_1 = Button(self.root,text="TRAIN DATA",command=self.train_classifier,cursor="hand2",font=("times new roman",30,"bold"),bg="darkblue",fg="white")
        btn1_1.place(x=630,y=100,width=280,height=48)

    def train_classifier(self):
        data_dir = ("data")
        path = [os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            img = Image.open(image).convert('L')  #gray scale image
            imageNp = np.array(img,'uint8')
            id = int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids = np.array(ids)

        #****************** Train the classifier and save************************    
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training datasets completed!!")

if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()