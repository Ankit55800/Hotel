from tkinter import*
from PIL import Image,ImageTk 
from tkinter import ttk


class Meals:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Empire")
        self.root.geometry("1320x565+205+228")
        self.root.configure(bg='#344e41')


#==========================================================Title===========================================================================
        lbl_title=Label(self.root,text="Meals" , font=("times new roman",15,"bold"),bg="black",fg="white",relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1310,height=50)

#========================================================Label Frame=================================================================================

        label_left=LabelFrame(self.root,bd=2,relief=RIDGE,text="Meals",font=("times new roman",14,"bold"),bg='#344e41',fg="white",padx=2)
        label_left.place(x=5,y=50,width=190,height=512)


   #=============================================================logo===========================================================================
        img1=Image.open(r"C:\Users\hp\Desktop\Hotel\images\meal1.jpg") 
        img1=img1.resize((370,230),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        lblimg=Label(self.root,image=self.photoimg1,relief=RIDGE)
        lblimg.place(x=198,y=50,width=370,height=230)

        img2=Image.open(r"C:\Users\hp\Desktop\Hotel\images\meal2.jpg") 
        img2=img2.resize((370,230),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        lblimg=Label(self.root,image=self.photoimg2,relief=RIDGE)
        lblimg.place(x=572,y=50,width=370,height=230)


        img3=Image.open(r"C:\Users\hp\Desktop\Hotel\images\meal3.jpg") 
        img3=img3.resize((370,230),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        lblimg=Label(self.root,image=self.photoimg3,relief=RIDGE)
        lblimg.place(x=945,y=50,width=370,height=230)


        img4=Image.open(r"C:\Users\hp\Desktop\Hotel\images\meal4.jpg") 
        img4=img4.resize((370,230),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        lblimg=Label(self.root,image=self.photoimg4,relief=RIDGE)
        lblimg.place(x=200,y=305,width=370,height=230)


        img5=Image.open(r"C:\Users\hp\Desktop\Hotel\images\meal5.jpg") 
        img5=img5.resize((370,230),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)
        lblimg=Label(self.root,image=self.photoimg5,relief=RIDGE)
        lblimg.place(x=575,y=305,width=370,height=230)

        img6=Image.open(r"C:\Users\hp\Desktop\Hotel\images\meal6.jpg") 
        img6=img6.resize((370,230),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)
        lblimg=Label(self.root,image=self.photoimg6,relief=RIDGE)
        lblimg.place(x=948,y=305,width=370,height=230)


        mealbtn=Button(label_left,text="Breakfast",width=14,height=1,font=("times new roman",15,"bold"),bg="black",fg="white",bd=0,cursor="hand1")
        mealbtn.place(x=0,y=30)
        mealbtn=Button(label_left,text="Lunch",width=14,height=1,font=("times new roman",15,"bold"),bg="black",fg="white",bd=0,cursor="hand1")
        mealbtn.place(x=0,y=85)
        mealbtn=Button(label_left,text="Dinner",width=14,height=1,font=("times new roman",15,"bold"),bg="black",fg="white",bd=0,cursor="hand1")
        mealbtn.place(x=0,y=140)
        mealbtn=Button(label_left,text="Special",width=14,height=1,font=("times new roman",15,"bold"),bg="black",fg="white",bd=0,cursor="hand1")
        mealbtn.place(x=0,y=195)
        mealbtn=Button(label_left,text="BBQ",width=14,height=1,font=("times new roman",15,"bold"),bg="black",fg="white",bd=0,cursor="hand1")
        mealbtn.place(x=0,y=250)





if __name__ == "__main__":
    root=Tk()
    obj=Meals(root)
    root.mainloop()


