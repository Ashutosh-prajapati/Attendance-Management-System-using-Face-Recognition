from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from student import Student
import os
from train import Train
from face_recognition import Face_Recognition

class Face_Recognition_System:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        
        #background image
        img1 = Image.open(r"C:\Program Files\Python311\face_Detaction_project\Images\background.jpg")
        img1 = img1.resize((1530,790))
        self.backimg = ImageTk.PhotoImage(img1)

        bg_img = Label(self.root,image=self.backimg)
        bg_img.place(x=0,y=0,width=1530,height=790)

        #header Image
        img2 = Image.open(r"C:\Program Files\Python311\face_Detaction_project\Images\headerImg.webp")
        img2 = img2.resize((200,130))
        self.headerimg = ImageTk.PhotoImage(img2)

        f_lbl = Label(bg_img,image=self.headerimg)
        f_lbl.place(x=0,y=0,width=200,height=130)
        
        #title
        title_lbl = Label(bg_img,text = "FACE RECOGNITION ATTENDANCE SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=130,width=1530,height=45)


        #menu items
        m_img1=Image.open(r"C:\Program Files\Python311\face_Detaction_project\Images\profile.jpeg")
        m_img1 = m_img1.resize((220,220))
        self.btnImg1 = ImageTk.PhotoImage(m_img1)

        btn1 = Button(bg_img,image=self.btnImg1,command=self.student_details,cursor="hand2")
        btn1.place(x=230,y=250,width=220,height=220)

        btn1_1 = Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        btn1_1.place(x=230,y=430,width=220,height=40)


        m_img2=Image.open(r"C:\Program Files\Python311\face_Detaction_project\Images\headerImg.webp")
        m_img2 = m_img2.resize((220,220))
        self.btnImg2 = ImageTk.PhotoImage(m_img2)

        btn2 = Button(bg_img,image=self.btnImg2,cursor="hand2",command=self.face_data)
        btn2.place(x=630,y=250,width=220,height=220)


        btn2_2 = Button(bg_img,text="Face Detector",cursor="hand2",command=self.face_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        btn2_2.place(x=630,y=430,width=220,height=40)
        

        m_img3=Image.open(r"C:\Program Files\Python311\face_Detaction_project\Images\attendanceImg.jpg")
        m_img3 = m_img3.resize((220,220))
        self.btnImg3 = ImageTk.PhotoImage(m_img3)

        btn3 = Button(bg_img,image=self.btnImg3,cursor="hand2")
        btn3.place(x=1030,y=250,width=220,height=220)

        btn3_3 = Button(bg_img,text="Attendance",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        btn3_3.place(x=1030,y=430,width=220,height=40)


        m_img5=Image.open(r"C:\Program Files\Python311\face_Detaction_project\Images\trainDataImg.png")
        m_img5 = m_img5.resize((220,220))
        self.btnImg5 = ImageTk.PhotoImage(m_img5)

        btn5 = Button(bg_img,image=self.btnImg5,cursor="hand2",command=self.train_data)
        btn5.place(x=230,y=495,width=220,height=220)

        btn5_5 = Button(bg_img,text="Train Data",command=self.train_data,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        btn5_5.place(x=230,y=675,width=220,height=40)
        

        m_img6=Image.open(r"C:\Program Files\Python311\face_Detaction_project\Images\gallery.jpg")
        m_img6 = m_img6.resize((220,220))
        self.btnImg6 = ImageTk.PhotoImage(m_img6)

        btn6 = Button(bg_img,image=self.btnImg6,cursor="hand2",command=self.open_img)
        btn6.place(x=630,y=495,width=220,height=220)

        btn6_6 = Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        btn6_6.place(x=630,y=675,width=220,height=40)


        m_img7=Image.open(r"C:\Program Files\Python311\face_Detaction_project\Images\exitImg.webp")
        m_img7 = m_img7.resize((220,220))
        self.btnImg7 = ImageTk.PhotoImage(m_img7)

        btn7 = Button(bg_img,image=self.btnImg7,cursor="hand2")
        btn7.place(x=1030,y=495,width=220,height=220)

        btn7_7 = Button(bg_img,text="Exit",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        btn7_7.place(x=1030,y=675,width=220,height=40)



    def open_img(self):
        os.startfile("data")    

#*************************function Button  *******************
        
    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)

    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)
 
    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_Recognition(self.new_window)
        
if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()
