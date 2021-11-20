from tkinter import *
from PIL import Image,ImageTk

from tkinter import Tk, font
import mysql
import mysql.connector
from tkinter import messagebox
from Main import Mainpage
from login import Login
from tkinter import ttk




class Homepage:


        def __init__(self,root):

                self.root=root
                self.root.title('HOME')
                self.root.geometry("1920x1080+0+0")

        



#=======================================Background
    #create main frame
                frame=Frame(self.root,bd=4,relief=RIDGE)
                frame.place(x=0,y=0,width=1920,height=1280)  
                #frame.pack(fill=BOTH, expand=1 ) 

                #add scrollbar to canvas
                


                img=Image.open(r"C:\Users\hp\Desktop\Hotel\images\bg12.jpg")
                img=img.resize((1920,1080),Image.ANTIALIAS)
                self.photoimg=ImageTk.PhotoImage(img)
                imglbl=Label(frame,image=self.photoimg, height=1080, width=1920)
                imglbl.place(x=0,y=0,relwidth=1,relheight=1)

        
        

#=======================================Title


                lbl_title=Label(self.root,text="Hotel Empire" , font=("times new roman",40,"bold"),bg="black",fg="white",padx=650)
                lbl_title.place(x=0,y=0,height=120)

#=======================================Scroll
        
        #scroll = Scrollbar(frame)
        #scroll.pack(side=RIGHT, fill=Y)
        
        
#=======================================Contents

                L_aboutus = Label(frame, text="ABOUT HOTEL EMPIRE",  font=('times new roman',26), bg="#0077b6", fg="#e3f2fd",padx=600).place(x=0,y=170)
                L_aboutus = Label(frame,
                                text="""Founded by J. Willard and Alice Marriott, and guided by family leadership since 1927,
        their principles remain embedded in the company’s culture and in everythingwe do today. 
        Diversity and inclusion is fundamental to our core values and strategicbusiness goals. 
        Taking care of people and their well-being is our most precious cultural inheritance.
Guided by our sustainability and social impact platform, Serve 360: Doing Good in Every Direction, 
Hotel Empire commits to creating positive and sustainable impact wherever we do business.""",  
                                font=('times new roman',20), 
                                bg="#0077b6", 
                                fg="#e3f2fd",
                                padx=300).place(x=0,y=250)
                

#=======================================Buttons

                btn1=Button(frame,text="Book Rooms   >>",font=("Times new roman",15),bg="black",command=self.Booking,fg="white",borderwidth=15,padx=10,pady=5,bd=4,cursor="hand1")     
                btn1.place(x=650, y=480)

        def Booking(self):
                messagebox.showinfo("LOGIN NEEDED","Please login to continue, redirecting you to the login page!",parent=self.root)
                self.new_window=Toplevel(self.root)
                self.app=Login(self.new_window)



                
                


if __name__ == "__main__":
    root=Tk()
   
    obj=Homepage(root)
    
    root.mainloop()