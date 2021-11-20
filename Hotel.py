from tkinter import*
from PIL import Image,ImageTk
#from tkinter import ttk
#from tkinter import messagebox
from room import RoomBooking
from details import Detailsroom
from employee import Employee
from meals import Meals
from service import Service
from feedback import Feedback
from complain import Complaints




class HotelEmpire:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Empire")
        self.root.geometry("1550x800+0+0")
        self.root.config(bg='#344e41')




#============================================logo===========================================================================================
        img1=Image.open(r"C:\Users\hp\Desktop\Hotel\images\logo23.png")
        img1=img1.resize((230,140),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        lblimg=Label(self.root,image=self.photoimg1,relief=RIDGE)
        lblimg.place(x=0,y=0,width=230,height=140)

#==========================================================Title===========================================================================
        lbl_title=Label(self.root,text="Hotel Empire" , font=("times new roman",40,"bold"),bg="black",fg="white",bd=4,relief=RIDGE)
        lbl_title.place(x=235,y=0,width=1300,height=140)
        
        logout_btn=Button(self.root,text="LOGOUT",command=self.logout,width=8,height=1,font=("times new roman",12,"bold"),bg="red",fg="black",cursor="hand1")
        logout_btn.grid(row=9,column=0,pady=2)
        logout_btn.place(x=1445,y=144)


#========================================================MainFrame==========================================================================
        main_frame=Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=190,width=1530,height=650)



        self.img1=ImageTk.PhotoImage(file=r"C:\Users\hp\Desktop\Hotel\images\p2.jpg")
        lblimg1=Label(main_frame,image=self.img1)
        lblimg1.place(x=190,y=0,width=1330,height=620)


#======================================================Menu================================================================================
        lbl_menu=Label(main_frame,text="Menu" , font=("times new roman",30,"bold"),bg="black",fg="white",bd=6,relief=RIDGE)
        lbl_menu.place(x=0,y=0,width=190)


#=====================================================ButtonFrame==========================================================================

        btn_frame=Frame(main_frame,bd=4,relief=RIDGE)
        btn_frame.place(x=0,y=60,width=190,height=580)

        cust_btn=Button(btn_frame,text="EMPLOYEES",command=self.employee,width=14,height=1,font=("times new roman",15,"bold"),bg="black",fg="white",bd=0,cursor="hand1")
        cust_btn.grid(row=0,column=0,pady=2)

        room_btn=Button(btn_frame,text="ROOMS",command=self.roombooking,width=14,height=1,font=("times new roman",15,"bold"),bg="black",fg="white",bd=0,cursor="hand1")
        room_btn.grid(row=1,column=0,pady=2)

        details_btn=Button(btn_frame,text="DETAILS",command=self.details,width=14,height=1,font=("times new roman",15,"bold"),bg="black",fg="white",bd=0,cursor="hand1")
        details_btn.grid(row=2,column=0,pady=2)

        services_btn=Button(btn_frame,text="SERVICES",command=self.service,width=14,height=1,font=("times new roman",15,"bold"),bg="black",fg="white",bd=0,cursor="hand1")
        services_btn.grid(row=3,column=0,pady=2)

        meals_btn=Button(btn_frame,text="MEALS",command=self.meals,width=14,height=1,font=("times new roman",15,"bold"),bg="black",fg="white",bd=0,cursor="hand1")
        meals_btn.grid(row=4,column=0,pady=2)

        complaint_btn=Button(btn_frame,text="COMPLAINTS",command=self.complain,width=14,height=1,font=("times new roman",15,"bold"),bg="black",fg="white",bd=0,cursor="hand1")
        complaint_btn.grid(row=6,column=0,pady=2)

        feedback_btn=Button(btn_frame,text="FEEDBACKS",command=self.feedback,width=14,height=1,font=("times new roman",15,"bold"),bg="black",fg="white",bd=0,cursor="hand1")
        feedback_btn.grid(row=7,column=0,pady=2)



    def employee(self):
        self.new_window=Toplevel(self.root)
        self.app=Employee(self.new_window)

    def roombooking(self):
        self.new_window=Toplevel(self.root)
        self.app=RoomBooking(self.new_window)

    def details(self):
        self.new_window=Toplevel(self.root)
        self.app=Detailsroom(self.new_window)

    def meals(self):
        self.new_window=Toplevel(self.root)
        self.app=Meals(self.new_window)

    def service(self):
        self.new_window=Toplevel(self.root)
        self.app=Service(self.new_window)

    def feedback(self):
        self.new_window=Toplevel(self.root)
        self.app=Feedback(self.new_window)

    def complain(self):
        self.new_window=Toplevel(self.root)
        self.app=Complaints(self.new_window)


    def logout(self):
        self.root.destroy()




if __name__ == "__main__":
    root=Tk()
    obj=HotelEmpire(root)
    root.mainloop()