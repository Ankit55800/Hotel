from tkinter import*
from PIL import Image,ImageTk 
from tkinter import ttk
from time import strftime
from datetime import datetime
import mysql.connector
import random
from tkinter import messagebox




def main():
    win=Tk()
    app=RoomBooking(win)
    win.mainloop()


class RoomBooking:
        def __init__(self,root):
                        self.root=root
                        self.root.title("Hotel Empire")
                        self.root.geometry("1320x565+205+228")


 #===================================================Variables============================================
                        self.var_contact=StringVar()
                        self.var_checkin=StringVar()
                        self.var_checkout=StringVar()
                        self.var_roomtype=StringVar()
                        self.var_roomNo=StringVar()
                        self.var_meal=StringVar()
                        self.var_days=StringVar()
                        self.var_tax=StringVar()
                        self.var_sub=StringVar()
                        self.var_total=StringVar()

 #==========================================================Title===========================================================================
                        lbl_title=Label(self.root,text="Booking Details" , font=("times new roman",15,"bold"),bg="black",fg="white",bd=4,relief=RIDGE)
                        lbl_title.place(x=0,y=0,width=1310,height=50)


  #=============================================================logo===========================================================================
                        img3=Image.open(r"C:\Users\hp\Desktop\Hotel\images\logo23.png")
                        img3=img3.resize((120,70),Image.ANTIALIAS)
                        self.photoimg3=ImageTk.PhotoImage(img3)
                        lblimg=Label(self.root,image=self.photoimg3,bd=4,relief=RIDGE)
                        lblimg.place(x=5,y=2,width=120,height=50)


#=======================================================================Label Frame=================================================================================

                        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Booking Details",fg='#fca311',font=("times new roman",16,"bold"),padx=2)
                        labelframeleft.place(x=5,y=50,width=425,height=500)
                        labelframeleft.config(bg='#344e41')

#=============================================================Labels & Entry==========================================================


                        lblcust_contact = Label(labelframeleft,bg="#344e41",fg="white", font=('arial',12,'bold'), text="Customer Contact:",padx=1)
                        lblcust_contact.grid(row=0,column=0, sticky=W)
                        entcust_contact = Entry(labelframeleft,textvariable=self.var_contact,font=('arial',12,'bold'), width=18)
                        entcust_contact.grid(row=0,column=1,pady=3,padx=20)

                #fetch data
                        btnFetch=Button(labelframeleft,command=self.Fetch_contact,text="Fetch Data",width=8,font=("arial",10,"bold"),bg="black",fg="white")
                        btnFetch.place(x=340,y=2)


                        lblDateIn = Label(labelframeleft, font=('arial',12,'bold'),bg="#344e41",fg="white", text="Check In Date:",padx=1)
                        lblDateIn.grid(row=1,column=0, sticky=W)
                        entDateIn = Entry(labelframeleft,textvariable=self.var_checkin, font=('arial',12,'bold'), width=18)
                        entDateIn.grid(row=1,column=1,pady=3,padx=20)

                        lblDateOut = Label(labelframeleft, font=('arial',12,'bold'),bg="#344e41",fg="white", text="Check Out Date:",padx=1)
                        lblDateOut.grid(row=2,column=0, sticky=W)
                        entDateOut = Entry(labelframeleft,textvariable=self.var_checkout, font=('arial',12,'bold'), width=18)
                        entDateOut.grid(row=2,column=1,pady=3,padx=20)


                        lblRoomType = Label(labelframeleft, font=('arial',12,'bold'),bg="#344e41",fg="white", text="Room Type:",padx=2,pady=2)
                        lblRoomType.grid(row=3,column=0, sticky=W)
                        CboRoomType = ttk.Combobox(labelframeleft,textvariable=self.var_roomtype, state='readonly',font=('arial',12,'bold'), width=16)
                        CboRoomType ['value'] = ('Select Room Type ', 'Standard | Rs.2500/-', 'Deluxe | Rs.4000/-', 'Suite | Rs.5000/-')
                        CboRoomType.current(0)
                        CboRoomType.grid(row=3, column=1, pady=3, padx=2)


                        lblRoomNo = Label(labelframeleft, font=('arial',12,'bold'),bg="#344e41",fg="white", text="Room No.:",padx=2,pady=2)
                        lblRoomNo.grid(row=4,column=0, sticky=W)
                        CboRoomNo = ttk.Combobox(labelframeleft,textvariable=self.var_roomNo, state='readonly',font=('arial',12,'bold'), width=16)
                        CboRoomNo ['value'] = (' ', '001', '002', '003','004','005','006','101', '102', '103','104','105','106','201', '202', '203','204','205','206')
                        CboRoomNo.current(0)
                        CboRoomNo.grid(row=4, column=1, pady=3, padx=2)



                        lblMeal = Label(labelframeleft, font=('arial',12,'bold'),bg="#344e41",fg="white", text="Meal:",padx=2,pady=2)
                        lblMeal.grid(row=6,column=0, sticky=W)
                        CboMeal = ttk.Combobox(labelframeleft,textvariable=self.var_meal, state='readonly',font=('arial',12,'bold'), width=16)
                        CboMeal ['value'] = (' ', 'Breakfast', 'Lunch', 'Dinner')
                        CboMeal.current(0)
                        CboMeal.grid(row=6, column=1, pady=3, padx=2)


                        lblNoofDays = Label(labelframeleft, font=('arial',12,'bold'),bg="#344e41",fg="white", text="No. Of Days:",padx=1)
                        lblNoofDays.grid(row=7,column=0, sticky=W)
                        entNoofDays = Entry(labelframeleft,textvariable=self.var_days, font=('arial',12,'bold'), width=18)
                        entNoofDays.grid(row=7,column=1,pady=3,padx=20)


                        lblTax = Label(labelframeleft, font=('arial',12,'bold'),bg="#344e41",fg="white", text="Paid Tax:",padx=1)
                        lblTax.grid(row=8,column=0, sticky=W)
                        entTax = Entry(labelframeleft,textvariable=self.var_tax, font=('arial',12,'bold'), width=18)
                        entTax.grid(row=8,column=1,pady=3,padx=20)


                        lblSub = Label(labelframeleft, font=('arial',12,'bold'),bg="#344e41",fg="white", text="Sub Total:",padx=1)
                        lblSub.grid(row=9,column=0, sticky=W)
                        entSub = Entry(labelframeleft,textvariable=self.var_sub, font=('arial',12,'bold'), width=18)
                        entSub.grid(row=9,column=1,pady=3,padx=20)


                        lblTotal = Label(labelframeleft, font=('arial',12,'bold'),bg="#344e41",fg="white", text="Total Cost:",padx=1)
                        lblTotal.grid(row=10,column=0, sticky=W)
                        entTotal = Entry(labelframeleft,textvariable=self.var_total, font=('arial',12,'bold'), width=18)
                        entTotal.grid(row=10,column=1,pady=3,padx=20)


                        #BILLBUTTON
                        btnBill=Button(labelframeleft,text="Generate Bill",width=18,font=("arial",12,"bold"),bg="#003049",fg="white")
                        btnBill.grid(row=11,column=0,padx=1,sticky=W)
                        btnBill.place(x=170,y=335)

                #added a img
                        img4=Image.open(r"C:\Users\hp\Desktop\Hotel\images\logo1.jpg")
                        img4=img4.resize((140,120),Image.ANTIALIAS)
                        self.photoimg4=ImageTk.PhotoImage(img4)
                        lblimg=Label(self.root,image=self.photoimg4,bd=4,relief=RIDGE)
                        lblimg.place(x=30,y=380,width=110,height=80)
                        lblimg.config(bg='red')


#==============================================================Buttons===========================================================================

                        btnFrame=Frame(labelframeleft,bd=2,relief=RIDGE)
                        btnFrame.place(x=0,y=400,width=412,height=40)
                        btnFrame.config(bg='black')

                        btnAdd=Button(btnFrame,text="Add",command=self.add_data,width=10,font=("arial",11,"bold"),bg="black",fg="white")
                        btnAdd.grid(row=0,column=0,padx=1)

                        btnUpdate=Button(btnFrame,text="Update",command=self.update,width=10,font=("arial",11,"bold"),bg="black",fg="white")
                        btnUpdate.grid(row=0,column=1,padx=1)

                        btnDelete=Button(btnFrame,text="Delete",command=self.delete,width=10,font=("arial",11,"bold"),bg="black",fg="white")
                        btnDelete.grid(row=0,column=2,padx=1)

                        btnReset=Button(btnFrame,text="Reset",command=self.reset,width=10,font=("arial",11,"bold"),bg="black",fg="white")
                        btnReset.grid(row=0,column=3,padx=1)

                #RightSide Img

                        img5=Image.open(r"C:\Users\hp\Desktop\Hotel\images\bed1.jpg")
                        img5=img5.resize((500,230),Image.ANTIALIAS)
                        self.photoimg5=ImageTk.PhotoImage(img5)
                        lblimg=Label(self.root,image=self.photoimg5,bd=4,relief=RIDGE)
                        lblimg.place(x=800,y=60,width=500,height=230)
                        lblimg.config(bg='red')


#==============================================================TableFrame=========================================================================================

                        TableFrame=LabelFrame(self.root,bd=2,relief=RIDGE,text="Search System",font=("times new roman",14,"bold"),padx=2)
                        TableFrame.place(x=435,y=300,width=850,height=250)
                        TableFrame.config(bg='#84a98c')

                        lblSearchby = Label(TableFrame, font=('arial',12,'bold'), text="Search By:",bg="red",fg="white")
                        lblSearchby.grid(row=0,column=0, sticky=W,padx=2)

                        self.search_var=StringVar()
                        CboSearch = ttk.Combobox(TableFrame,textvariable=self.search_var,state='readonly',font=('arial',12,'bold'), width=13)
                        CboSearch ['value'] = (' ','Contact', 'Room','IdNo.')
                        CboSearch.current(0)
                        CboSearch.grid(row=0, column=1,padx=2)

                        self.txt_search=StringVar()
                        entSearch= Entry(TableFrame,textvariable=self.txt_search, font=('arial',12,'bold'), width=24)
                        entSearch.grid(row=0,column=2,padx=2)


                        btnSearch=Button(TableFrame,text="Search",command=self.search,width=10,font=("arial",11,"bold"),bg="black",fg="white")
                        btnSearch.grid(row=0,column=3,padx=2)

                        btnShowAll=Button(TableFrame,text="Show All",command=self.fetch_data,width=10,font=("arial",11,"bold"),bg="black",fg="white")
                        btnShowAll.grid(row=0,column=4,padx=2)



#===================================================================Show Data Table===================================================================================

                        detailsTable=Frame(TableFrame,bd=2,relief=RIDGE)
                        detailsTable.place(x=0,y=50,width=870,height=140)


                        scroll_x=ttk.Scrollbar(detailsTable,orient=HORIZONTAL)
                        scroll_y=ttk.Scrollbar(detailsTable,orient=VERTICAL)

                        self.room_table=ttk.Treeview(detailsTable,column=("contact","checkin","checkout",
                        "roomtype","roomNo","meal","days"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

                        scroll_x.pack(side=BOTTOM,fill=X)
                        scroll_y.pack(side=RIGHT,fill=Y)

                        scroll_x.config(command=self.room_table.xview)
                        scroll_y.config(command=self.room_table.yview)

                        self.room_table.heading("contact",text="Contact")
                        self.room_table.heading("checkin",text="Check In")
                        self.room_table.heading("checkout",text="Check Out")
                        self.room_table.heading("roomtype",text="Room Type")
                        self.room_table.heading("roomNo",text="Room No.")
                        self.room_table.heading("meal",text="Meal")
                        self.room_table.heading("days",text="No. Of Days")

                        self.room_table["show"]="headings"


                        self.room_table.column("contact",width=100)
                        self.room_table.column("checkin",width=100)
                        self.room_table.column("checkout",width=100)
                        self.room_table.column("roomtype",width=100)
                        self.room_table.column("roomNo",width=100)
                        self.room_table.column("meal",width=100)
                        self.room_table.column("days",width=100)

                        self.room_table.pack(fill=BOTH,expand=1)

                        self.room_table.bind("<ButtonRelease-1>",self.get_cursor)
                        self.fetch_data()

#Add data

        def add_data(self):
                if self.var_contact.get()=="" or self.var_checkin.get()=="":
                        messagebox.showerror("Error!","All fields are mandatory",parent=self.root)
                else:
                        try:
                                conn=mysql.connector.connect(host="localhost", user="root",password="#Sooraj@1939",database="sys")
                                my_cursor=conn.cursor()
                                my_cursor.execute("insert into room values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                        self.var_contact.get(),
                                                                                        self.var_checkin.get(),
                                                                                        self.var_checkout.get(),
                                                                                        self.var_roomtype.get(),
                                                                                        self.var_roomNo.get(),
                                                                                        self.var_meal.get(),
                                                                                        self.var_days.get()
                                                                                           
                                                                                    ))
                                conn.commit()
                                
                                self.fetch_data()
                                conn.close()                                            
                                messagebox.showinfo("Success","Room Booked",parent=self.root)
                        except Exception as es:
                                messagebox.showwarning("Warning!",f"Something went wrong:{str(es)}",parent=self.root)

#fetch data
        def fetch_data(self):
                conn=mysql.connector.connect(host="localhost",user="root",password="#Sooraj@1939",database="sys")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from room")
                rows=my_cursor.fetchall()
                if len(rows)!=0:
                    self.room_table.delete(*self.room_table.get_children())
                for i in rows:
                    self.room_table.insert("",END,values=i)
                conn.commit()
                conn.close()


#get cursor
        def get_cursor(self,event=""):
                cursor_row=self.room_table.focus()
                content=self.room_table.item(cursor_row)
                row=content["values"]

                self.var_contact.set(row[0]),
                self.var_checkin.set(row[1]),
                self.var_checkout.set(row[2]),
                self.var_roomtype.set(row[3]),
                self.var_roomNo.set(row[4]),
                self.var_meal.set(row[5]),
                self.var_days.set(row[6])

#UPDATE FUNCTION
        def update(self):
                if self.var_contact.get()=="":
                        messagebox.showerror("Error!","Please Enter Contact No.",parent=self.root)
                else:
                        conn=mysql.connector.connect(host="localhost",user="root",password="#Sooraj@1939",database="sys")
                        my_cursor=conn.cursor()
                        my_cursor.execute("update room set checkin=%s,checkout=%s,roomtype=%s,roomNo=%s,meal=%s,days=%s where Contact=%s",(
                                                                                                                                                                                
                                                                                                                                                                                self.var_checkin.get(),
                                                                                                                                                                                self.var_checkout.get(),
                                                                                                                                                                                self.var_roomtype.get(),
                                                                                                                                                                                self.var_roomNo.get(),
                                                                                                                                                                                self.var_meal.get(),
                                                                                                                                                                                self.var_days.get(),
                                                                                                                                                                                self.var_contact.get()


                                                                                                                                                                        ))

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Update","Room details has been updated successfully.",parent=self.root)

        #DELETE FUNCTION
        def delete(self):
                delete=messagebox.askyesno("Hotel Management System","Do you want to delete this room ?",parent=self.root)
                if delete>0:
                        conn=mysql.connector.connect(host="localhost",user="root",password="#Sooraj@1939",database="sys")
                        my_cursor=conn.cursor()
                        query="delete from room where Contact=%s"
                        value=(self.var_contact.get(),)
                        my_cursor.execute(query,value)
                else:
                        if not delete:
                                return
                conn.commit()
                self.fetch_data()
                conn.close()

        #RESET FUNCTION
        def reset(self):
                self.var_contact.set(""),
                self.var_checkin.set(""),
                self.var_checkout.set(""),
                self.var_roomtype.set(""),
                self.var_roomNo.set(""),
                self.var_meal.set(""),
                self.var_days.set(""),
                self.var_tax.set(""),
                self.var_sub.set(""),
                self.var_total.set("")

#=========================================Fetching Data=============================================================================

        def Fetch_contact(self):
                if self.var_contact.get()=="":
                        messagebox.showerror("Error!","Please Enter Contact No.",parent=self.root)
                else:
                
                        conn=mysql.connector.connect(host="localhost",user="root",password="#Sooraj@1939",database="sys")
                        my_cursor=conn.cursor()
                        query=("select Name from customer where Mobile=%s")
                        value=(self.var_contact.get(),)
                        my_cursor.execute(query,value)
                        row=my_cursor.fetchone()

                if row==None:
                        messagebox.showerror("Error!","This number is not Found",parent=self.root)
                else:
                        conn.commit()
                        conn.close()

                        showDataframe=Frame(self.root,bd=4,relief=RIDGE,padx=2)
                        showDataframe.place(x=450,y=55,width=300,height=180)
                        #FNameShow
                        lblFName=Label(showDataframe,text="FName:",font=("arial",12,"bold"))
                        lblFName.place(x=0,y=0)
                        lbl=Label(showDataframe,text=row,font=("arial",12,"bold"))
                        lbl.place(x=90,y=0)

                        #LNameShow
                        conn=mysql.connector.connect(host="localhost",user="root",password="#Sooraj@1939",database="sys")
                        my_cursor=conn.cursor()
                        query=("select LName from customer where Mobile=%s")
                        value=(self.var_contact.get(),)
                        my_cursor.execute(query,value)
                        row=my_cursor.fetchone()

                        lblLName=Label(showDataframe,text="LName:",font=("arial",12,"bold"))
                        lblLName.place(x=0,y=30)
                        lbl2=Label(showDataframe,text=row,font=("arial",12,"bold"))
                        lbl2.place(x=90,y=30)


                        #GenderShow
                        conn=mysql.connector.connect(host="localhost",user="root",password="#Sooraj@1939",database="sys")
                        my_cursor=conn.cursor()
                        query=("select Gender from customer where Mobile=%s")
                        value=(self.var_contact.get(),)
                        my_cursor.execute(query,value)
                        row=my_cursor.fetchone()

                        lblGender=Label(showDataframe,text="Gender:",font=("arial",12,"bold"))
                        lblGender.place(x=0,y=60)
                        lbl3=Label(showDataframe,text=row,font=("arial",12,"bold"))
                        lbl3.place(x=90,y=60)

                        #EmailShow

                        conn=mysql.connector.connect(host="localhost",user="root",password="#Sooraj@1939",database="sys")
                        my_cursor=conn.cursor()
                        query=("select Email from customer where Mobile=%s")
                        value=(self.var_contact.get(),)
                        my_cursor.execute(query,value)
                        row=my_cursor.fetchone()

                        lblEmail=Label(showDataframe,text="Email:",font=("arial",12,"bold"))
                        lblEmail.place(x=0,y=90)
                        lbl4=Label(showDataframe,text=row,font=("arial",12,"bold"))
                        lbl4.place(x=90,y=90)


                        #AddressShow
                        conn=mysql.connector.connect(host="localhost",user="root",password="#Sooraj@1939",database="sys")
                        my_cursor=conn.cursor()
                        query=("select Address from customer where Mobile=%s")
                        value=(self.var_contact.get(),)
                        my_cursor.execute(query,value)
                        row=my_cursor.fetchone()

                        lblAddress=Label(showDataframe,text="Address:",font=("arial",12,"bold"))
                        lblAddress.place(x=0,y=120)
                        lbl5=Label(showDataframe,text=row,font=("arial",12,"bold"))
                        lbl5.place(x=90,y=120)

#search system

#SEARCH FUNCTION
        def search(self):
                conn=mysql.connector.connect(host="localhost",user="root",password="#Sooraj@1939",database="sys")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from room where"+str(self.search_var.get())+"LIKE'%"+str(self.txt_search.get())+"%'")
                rows=my_cursor.fetchall()
                if len (rows)!=0:
                        self.room_table.delete(*self.room_table.get_children())
                        for i in rows:
                                self.room_table.insert("",END,values=i)
                        conn.commit()
                conn.close()




        def total(self):
                inDate=self.var_checkin.get()
                outDate=self.var_checkout.get()
                inDate=datetime.strptime(inDate,"%d/%m/%Y")
                outDate=datetime.strptime(outDate,"%d/%m/%Y")
                self.var_days.set(abs(outDate-inDate).days)

                if (self.var_meal.get()=="Breakfast" and self.var_roomtype.get()=="Suite"):
                        q1=float(300)
                        q2=float(5000)
                        q3=float(self.var_days.get())
                        q4=float(q1+q2)
                        q5=float(q3+q4)
                        Tax="Rs."+str("%.2f"%((q5)*0.1))
                        SubTax="Rs."+str("%.2f"%((q5)))
                        ToTax="Rs."+str("%.2f"%(q5+((q5)*0.1)))
                        self.var_tax.set(Tax)
                        self.var_sub.set(SubTax)
                        self.var_total.set(ToTax)


                elif (self.var_meal.get()=="Breakfast" and self.var_roomtype.get()=="Standard"):
                        q1=float(300)
                        q2=float(2500)
                        q3=float(self.var_days.get())
                        q4=float(q1+q2)
                        q5=float(q3+q4)
                        Tax="Rs."+str("%.2f"%((q5)*0.1))
                        SubTax="Rs."+str("%.2f"%((q5)))
                        ToTax="Rs."+str("%.2f"%(q5+((q5)*0.1)))
                        self.var_tax.set(Tax)
                        self.var_sub.set(SubTax)
                        self.var_total.set(ToTax)

                elif (self.var_meal.get()=="Breakfast" and self.var_roomtype.get()=="Deluxe"):
                        q1=float(300)
                        q2=float(4000)
                        q3=float(self.var_days.get())
                        q4=float(q1+q2)
                        q5=float(q3+q4)
                        Tax="Rs."+str("%.2f"%((q5)*0.1))
                        SubTax="Rs."+str("%.2f"%((q5)))
                        ToTax="Rs."+str("%.2f"%(q5+((q5)*0.1)))
                        self.var_tax.set(Tax)
                        self.var_sub.set(SubTax)
                        self.var_total.set(ToTax)

                elif (self.var_meal.get()=="Lunch" and self.var_roomtype.get()=="Deluxe"):
                        q1=float(300)
                        q2=float(4000)
                        q3=float(self.var_days.get())
                        q4=float(q1+q2)
                        q5=float(q3+q4)
                        Tax="Rs."+str("%.2f"%((q5)*0.1))
                        SubTax="Rs."+str("%.2f"%((q5)))
                        ToTax="Rs."+str("%.2f"%(q5+((q5)*0.1)))
                        self.var_tax.set(Tax)
                        self.var_sub.set(SubTax)
                        self.var_total.set(ToTax)


                elif (self.var_meal.get()=="Lunch" and self.var_roomtype.get()=="Suite"):
                        q1=float(300)
                        q2=float(5000)
                        q3=float(self.var_days.get())
                        q4=float(q1+q2)
                        q5=float(q3+q4)
                        Tax="Rs."+str("%.2f"%((q5)*0.1))
                        SubTax="Rs."+str("%.2f"%((q5)))
                        ToTax="Rs."+str("%.2f"%(q5+((q5)*0.1)))
                        self.var_tax.set(Tax)
                        self.var_sub.set(SubTax)
                        self.var_total.set(ToTax)

                elif (self.var_meal.get()=="Lunch" and self.var_roomtype.get()=="Standard"):
                        q1=float(300)
                        q2=float(2500)
                        q3=float(self.var_days.get())
                        q4=float(q1+q2)
                        q5=float(q3+q4)
                        Tax="Rs."+str("%.2f"%((q5)*0.1))
                        SubTax="Rs."+str("%.2f"%((q5)))
                        ToTax="Rs."+str("%.2f"%(q5+((q5)*0.1)))
                        self.var_tax.set(Tax)
                        self.var_sub.set(SubTax)
                        self.var_total.set(ToTax)

                elif (self.var_meal.get()=="Dinner" and self.var_roomtype.get()=="Deluxe"):
                        q1=float(300)
                        q2=float(4000)
                        q3=float(self.var_days.get())
                        q4=float(q1+q2)
                        q5=float(q3+q4)
                        Tax="Rs."+str("%.2f"%((q5)*0.1))
                        SubTax="Rs."+str("%.2f"%((q5)))
                        ToTax="Rs."+str("%.2f"%(q5+((q5)*0.1)))
                        self.var_tax.set(Tax)
                        self.var_sub.set(SubTax)
                        self.var_total.set(ToTax)


                elif (self.var_meal.get()=="Dinner" and self.var_roomtype.get()=="Standard"):
                        q1=float(300)
                        q2=float(2500)
                        q3=float(self.var_days.get())
                        q4=float(q1+q2)
                        q5=float(q3+q4)
                        Tax="Rs."+str("%.2f"%((q5)*0.1))
                        SubTax="Rs."+str("%.2f"%((q5)))
                        ToTax="Rs."+str("%.2f"%(q5+((q5)*0.1)))
                        self.var_tax.set(Tax)
                        self.var_sub.set(SubTax)
                        self.var_total.set(ToTax)


                elif (self.var_meal.get()=="Dinner" and self.var_roomtype.get()=="Suite"):
                        q1=float(300)
                        q2=float(5000)
                        q3=float(self.var_days.get())
                        q4=float(q1+q2)
                        q5=float(q3+q4)
                        Tax="Rs."+str("%.2f"%((q5)*0.1))
                        SubTax="Rs."+str("%.2f"%((q5)))
                        ToTax="Rs."+str("%.2f"%(q5+((q5)*0.1)))
                        self.var_tax.set(Tax)
                        self.var_sub.set(SubTax)
                        self.var_total.set(ToTax)




#Bill.py

class Bill:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Empire")
        self.root.geometry("500x350+700+250")


#========================================================Label Frame=================================================================================

        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Payment",font=("times new roman",14,"bold"),padx=2)
        labelframeleft.place(x=0,y=0,width=500,height=350)
        labelframeleft.config(bg='cyan')

#=====================================================Variables====================================================

        self.billno=StringVar()
        x=random.randint(1000,9999)
        self.billno.set(str(x))

        self.var_empid=StringVar()
        self.bonus=IntVar()
        self.amount=IntVar()
        self.amt=StringVar()
        self.name=StringVar()
        self.desig=StringVar()
        self.dept=StringVar()
        self.payment=StringVar()
        self.chequeno=StringVar()

        
        

#========================================================Label & Enterys=================================================================================

        lblBill = Label(labelframeleft, font=('arial',15,'bold'), text="Bill No")
        lblBill.config(bg='cyan')
        lblBill.place(x=410,y=0)
        entBill = Entry(labelframeleft,textvariable=self.billno,font=('arial',12,'bold'),state='readonly', width=7)
        entBill.place(x=415,y=30)



        lblEmpId = Label(labelframeleft, font=('arial',12,'bold'), text="Employee ID:",padx=1)
        lblEmpId.grid(row=1,column=0, sticky=W)
        entEmpId = Entry(labelframeleft,textvariable=self.var_empid, font=('arial',12,'bold'), width=18)
        entEmpId.grid(row=1,column=1,pady=3,padx=20)


        lblEmpname = Label(labelframeleft, font=('arial',12,'bold'), text="Employee Name:",padx=1)
        lblEmpname.grid(row=2,column=0, sticky=W)
        entEmpname = Entry(labelframeleft,textvariable=self.name, font=('arial',12,'bold'), width=18)
        entEmpname.grid(row=2,column=1,pady=3,padx=20)


        lbldept = Label(labelframeleft, font=('arial',12,'bold'), text="Department:",padx=1)
        lbldept.grid(row=3,column=0, sticky=W)
        entdept = Entry(labelframeleft,textvariable=self.dept, font=('arial',12,'bold'), width=18)
        entdept.grid(row=3,column=1,pady=3,padx=20)


        lbldesig = Label(labelframeleft, font=('arial',12,'bold'), text="Designation:",padx=1)
        lbldesig.grid(row=4,column=0, sticky=W)
        entdesig = Entry(labelframeleft,textvariable=self.desig, font=('arial',12,'bold'), width=18)
        entdesig.grid(row=4,column=1,pady=3,padx=20)

        lblAmount = Label(labelframeleft, font=('arial',12,'bold'), text="Amount to pay:",padx=1)
        lblAmount.grid(row=5,column=0, sticky=W)
        entAmount = Entry(labelframeleft,textvariable=self.amount,font=('arial',12,'bold'), width=18)
        entAmount.grid(row=5,column=1,pady=3,padx=20)

        lblBns = Label(labelframeleft, font=('arial',12,'bold'), text="Bonus:",padx=1)
        lblBns.grid(row=6,column=0, sticky=W)
        entBns = Entry(labelframeleft,textvariable=self.bonus,font=('arial',12,'bold'), width=18)
        entBns.grid(row=6,column=1,pady=3,padx=20)

        #lblAmt = Label(labelframeleft,font=('arial',12,'bold'),padx=1,width=18)
        #lblAmt.grid(row=4,column=1, sticky=W)
        entAmt = Entry(labelframeleft,textvariable=self.amt, font=('arial',12,'bold') , width=18)
        entAmt.place(x=156,y=184)


        lblPay = Label(labelframeleft, font=('arial',12,'bold'), text="Payment Mode:",padx=2,pady=2)
        lblPay.place(x=0, y=220)
        CboPay = ttk.Combobox(labelframeleft,textvariable=self.payment,state='readonly',font=('arial',12,'bold'), width=16, height=15)
        CboPay ['value'] = (' ', 'Online', 'Cheque', 'Cash')
        CboPay.current(0)
        CboPay.place(x=156, y=220)


        lblcheque = Label(labelframeleft, font=('arial',12,'bold'), text="Cheque No.:",padx=1)
        lblcheque.place(x=0,y=250)
        entcheque = Entry(labelframeleft,textvariable=self.chequeno,font=('arial',12,'bold'), width=18)
        entcheque.place(x=156,y=250)
        #entcheque.config(state="normal")

    
        







#==============================================================Buttons===========================================================================

        #btn1=Button(labelframeleft,text="Save",command=self.save,width=10,font=("arial",11,"bold"),bg="orange",fg="black")
        #btn1.place(x=0,y=290)
        btn2=Button(labelframeleft,text="Print",command=self.print,width=10,font=("arial",11,"bold"),bg="orange",fg="black")
        btn2.place(x=190,y=290)
        btn3=Button(labelframeleft,text="Exit",command=self.cancel,width=10,font=("arial",11,"bold"),bg="red",fg="black")
        btn3.place(x=390,y=290)
        btn4=Button(labelframeleft,text="Pay",command=self.pay,width=10,font=("arial",11,"bold"),bg="red",fg="black")
        btn4.place(x=390,y=100)
        btn5=Button(labelframeleft,text="Total",command=self.total,width=15,font=("arial",11,"bold"),bg="red",fg="black")
        btn5.place(x=0,y=180)
        btn5=Button(labelframeleft,text="Search",command=self.searchemp,width=10,font=("arial",13,"bold"),bg="red",fg="black")
        btn5.place(x=0,y=290)   #----- made changes

        self.textarea=Text(labelframeleft)
#SAVE       #----- made changes 
   # def save(self):
    #    p=messagebox.askyesno("Save","Do you want to save the Bill.")
     #   if p>0:
      #      self.bill=self.textarea.get(1.0,END)
       #     f1=open('bills/'+str(self.billno.get())+".txt",'w').write(self.bill)
        #    p=messagebox.showinfo("Saved",f"Bill No:{self.billno.get()} saved successfully.")
         #   f1.close()

#PRINT        #----- made changes, // make textarea for printing reciept 
    def print(self):
        return

#CANCEL
    def cancel(self):
        self.root.destroy()

#total    #----- made changes
    def total(self):  
        amount=self.amount.get()
        bonus=self.bonus.get()  
        tot=amount+bonus
        self.amt.set(tot)
        #input_text.set(tot)

#PAY
    def pay(self):
        #self.amount=messagebox.askyesno("Save","Do you want to save the Bill.")
        if self.payment.get()=='Online':
            if self.amt.get()!="":
                messagebox.showinfo("Successful","Payment will be processed within 2-3 business days.",parent=self.root)
            
            else:
                messagebox.showerror("Error!","Please Enter the amount to pay.",parent=self.root)
            
        elif self.payment.get()=='Cheque':
            
            if self.amt.get()!="" and self.chequeno.get()!="":
                messagebox.showinfo("Successful","Payment will be processed within 5-7 business days.",parent=self.root)
            
            else:
                messagebox.showerror("Error!","Please check if the amount to pay and cheque number have been entered.",parent=self.root)

        else:
            y= messagebox.showinfo("Success","Payment Successful!",parent=self.root)
            
#SEARCH             #----- made changes  // resolve the error for executing multiple statements
    def searchemp(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="#Sooraj@1939",database="sys")
        my_cursor=conn.cursor(buffered=True)
        query="select empid from employee where empid = %s"
        empname="select FName from employee where empid = %s"
        empdesig="select Desig from employee where empid = %s"
        empdept="select Dept from employee where empid = %s"
        
        val=(self.empid.get(),)

        my_cursor.execute(query,val)
        emp=my_cursor.fetchone()
        my_cursor.execute(empname,val)
        nam=my_cursor.fetchone()
        my_cursor.execute(empdesig,val)
    
        des=my_cursor.fetchone()
        my_cursor.execute(empdept,val)
        dep=my_cursor.fetchone()
        rows=my_cursor.fetchall()
        
        if (val==emp):
            self.name.set(my_cursor.execute(empname,val)),
            self.desig.set(my_cursor.execute(empdesig,val)),
            self.dept.set(my_cursor.execute(empdept,val))
        else:
            messagebox.showerror("ERROR","No employee record found",parent=self.root)

        conn.commit()
        conn.close()

 














if __name__ == "__main__":
    main()
