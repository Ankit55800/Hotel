from tkinter import*
from PIL import Image,ImageTk 
from tkinter import ttk
import mysql.connector
from tkinter import messagebox



class Service:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Empire")
        self.root.geometry("1320x700+205+120")
        self.root.config(bg='#344e41')





#==========================================================Title===========================================================================
        lbl_title=Label(self.root,text="Services & Facilities" , font=("times new roman",25,"bold"),bg="black",fg="white",relief=RIDGE)
        lbl_title.place(x=520,y=0,width=300,height=50)
        


#=====================================================ButtonFrame==========================================================================

        btn_frame=Frame(self.root,bd=4,relief=RIDGE)
        btn_frame.place(x=0,y=60,width=1350,height=58)

        btn1=Button(btn_frame,text="Water",width=12,height=2,font=("times new roman",13,"bold"),bg="white",fg="black",bd=0,cursor="hand1")
        btn1.grid(row=0,column=0,pady=2)

        btn2=Button(btn_frame,text="Laundry",width=12,height=2,font=("times new roman",13,"bold"),bg="white",fg="black",bd=0,cursor="hand1")
        btn2.grid(row=0,column=1,pady=2)

        btn3=Button(btn_frame,text="Mattresses",width=12,height=2,font=("times new roman",13,"bold"),bg="white",fg="black",bd=0,cursor="hand1")
        btn3.grid(row=0,column=2,pady=2)

        btn4=Button(btn_frame,text="Furnitures",width=12,height=2,font=("times new roman",13,"bold"),bg="white",fg="black",bd=0,cursor="hand1")
        btn4.grid(row=0,column=3,pady=2)


        btn5=Button(btn_frame,text="Laundry",width=12,height=2,font=("times new roman",13,"bold"),bg="white",fg="black",bd=0,cursor="hand1")
        btn5.grid(row=0,column=4,pady=2)

        btn6=Button(btn_frame,text="Mattresses",width=12,height=2,font=("times new roman",13,"bold"),bg="white",fg="black",bd=0,cursor="hand1")
        btn6.grid(row=0,column=5,pady=2)

        btn7=Button(btn_frame,text="Water heaters",width=12,height=2,font=("times new roman",13,"bold"),bg="white",fg="black",bd=0,cursor="hand1")
        btn7.grid(row=0,column=6,pady=2)

        btn8=Button(btn_frame,text="Electrcity",width=12,height=2,font=("times new roman",13,"bold"),bg="white",fg="black",bd=0,cursor="hand1")
        btn8.grid(row=0,column=7,pady=2)

        btn9=Button(btn_frame,text="Internet",width=12,height=2,font=("times new roman",13,"bold"),bg="white",fg="black",bd=0,cursor="hand1")
        btn9.grid(row=0,column=8,pady=2)

        btn9=Button(btn_frame,text="Utensils",width=12,height=2,font=("times new roman",13,"bold"),bg="white",fg="black",bd=0,cursor="hand1")
        btn9.grid(row=0,column=9,pady=2)


        btn10=Button(btn_frame,text="X",width=5,height=2,font=("times new roman",13,"bold"),bg="red",fg="black",bd=0,cursor="hand1")
        btn10.grid(row=0,column=10,pady=2)



        img1=Image.open(r"C:\Users\hp\Desktop\Hotel\images\m11.jpg")
        img1=img1.resize((400,250),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        lblimg=Label(self.root,image=self.photoimg1,relief=RIDGE)
        lblimg.place(x=40,y=150,width=400,height=250)

        img2=Image.open(r"C:\Users\hp\Desktop\Hotel\images\m2.jpg")
        img2=img2.resize((400,250),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        lblimg=Label(self.root,image=self.photoimg2,relief=RIDGE)
        lblimg.place(x=460,y=150,width=400,height=250)

        img3=Image.open(r"C:\Users\hp\Desktop\Hotel\images\m3.jpg")
        img3=img3.resize((400,250),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        lblimg=Label(self.root,image=self.photoimg3,relief=RIDGE)
        lblimg.place(x=880,y=150,width=400,height=250)


        img4=Image.open(r"C:\Users\hp\Desktop\Hotel\images\m4.jpg")
        img4=img4.resize((400,250),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        lblimg=Label(self.root,image=self.photoimg4,relief=RIDGE)
        lblimg.place(x=40,y=425,width=400,height=250)

        img5=Image.open(r"C:\Users\hp\Desktop\Hotel\images\m5.jpg")
        img5=img5.resize((400,250),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)
        lblimg=Label(self.root,image=self.photoimg5,relief=RIDGE)
        lblimg.place(x=460,y=425,width=400,height=250)

        img6=Image.open(r"C:\Users\hp\Desktop\Hotel\images\m6.jpg")
        img6=img6.resize((400,250),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)
        lblimg=Label(self.root,image=self.photoimg6,relief=RIDGE)
        lblimg.place(x=880,y=425,width=400,height=250)














if __name__ == "__main__":
    root=Tk()
    obj=Service(root)
    root.mainloop()