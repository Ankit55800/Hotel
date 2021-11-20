from tkinter import*
from PIL import Image,ImageTk 
from tkinter import ttk
import mysql.connector
from tkinter import messagebox



class Detailsroom:
        def __init__(self,root):
                        self.root=root
                        self.root.title("Hotel Empire")
                        self.root.geometry("1320x565+205+228")

 #==========================================================Title===========================================================================
                        lbl_title=Label(self.root,text="Booking Details",font=("times new roman",15,"bold"),bg="black",fg="white",bd=4,relief=RIDGE)
                        lbl_title.place(x=0,y=0,width=1310,height=50)

 #=============================================================logo===========================================================================
                        img3=Image.open(r"C:\Users\hp\Desktop\Hotel\images\logo23.png")
                        img3=img3.resize((120,50),Image.ANTIALIAS)
                        self.photoimg3=ImageTk.PhotoImage(img3)
                        lblimg=Label(self.root,image=self.photoimg3,relief=RIDGE)
                        lblimg.place(x=5,y=5,width=100,height=40)


#=======================================================================Label Frame=================================================================================

                        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="New Room Add",font=("times new roman",14,"bold"),padx=2)
                        labelframeleft.place(x=5,y=50,width=540,height=350)


#=============================================================Labels & Entry==========================================================

#floor
                        lbl_floor = Label(labelframeleft, font=('arial',12,'bold'), text="Floor:",padx=1)
                        lbl_floor.grid(row=0,column=0, sticky=W)
                        self.var_floor=StringVar()
                        ent_floor = Entry(labelframeleft,textvariable=self.var_floor,font=('arial',12,'bold'), width=18)
                        ent_floor.grid(row=0,column=1,pady=3,padx=20)

#Room no.

                        lbl_floor = Label(labelframeleft, font=('arial',12,'bold'), text="Room No.:",padx=1)
                        lbl_floor.grid(row=1,column=0, sticky=W)
                        self.var_roomNo=StringVar()
                        ent_floor = Entry(labelframeleft,textvariable=self.var_roomNo,font=('arial',12,'bold'), width=18)
                        ent_floor.grid(row=1,column=1,pady=3,padx=20)

#Room type

                        lbl_floor = Label(labelframeleft, font=('arial',12,'bold'), text="Room Type:",padx=1)
                        lbl_floor.grid(row=2,column=0, sticky=W)
                        self.var_roomType=StringVar()
                        ent_floor = Entry(labelframeleft,textvariable=self.var_roomType,font=('arial',12,'bold'), width=18)
                        ent_floor.grid(row=2,column=1,pady=3,padx=20)

#==============================================================Buttons===========================================================================

                        btnFrame=Frame(labelframeleft,bd=2,relief=RIDGE)
                        btnFrame.place(x=0,y=200,width=412,height=40)

                        btnAdd=Button(btnFrame,text="Add",command=self.add_data,width=10,font=("arial",11,"bold"),bg="black",fg="white")
                        btnAdd.grid(row=0,column=0,padx=1)

                        btnUpdate=Button(btnFrame,text="Update",command=self.update,width=10,font=("arial",11,"bold"),bg="black",fg="white")
                        btnUpdate.grid(row=0,column=1,padx=1)

                        btnDelete=Button(btnFrame,text="Delete",command=self.delete,width=10,font=("arial",11,"bold"),bg="black",fg="white")
                        btnDelete.grid(row=0,column=2,padx=1)

                        btnReset=Button(btnFrame,text="Reset",command=self.reset,width=10,font=("arial",11,"bold"),bg="black",fg="white")
                        btnReset.grid(row=0,column=3,padx=1)

#==============================================================TableFrame=========================================================================================

                        TableFrame=LabelFrame(self.root,bd=2,relief=RIDGE,text="Show room details",font=("times new roman",14,"bold"),padx=2)
                        TableFrame.place(x=600,y=55,width=600,height=350)

                        scroll_x=ttk.Scrollbar(TableFrame,orient=HORIZONTAL)
                        scroll_y=ttk.Scrollbar(TableFrame,orient=VERTICAL)
                        
                        self.room_table=ttk.Treeview(TableFrame,column=("floor","roomno","roomtype"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
                        scroll_x.pack(side=BOTTOM,fill=X)
                        scroll_y.pack(side=RIGHT,fill=Y)

                        scroll_x.config(command=self.room_table.xview)
                        scroll_y.config(command=self.room_table.yview)

                        self.room_table.heading("floor",text="Floor")
                        self.room_table.heading("roomno",text="Room No.")
                        self.room_table.heading("roomtype",text="Room Type")

                        self.room_table["show"]="headings"


                        self.room_table.column("floor",width=100)
                        self.room_table.column("roomno",width=100)
                        self.room_table.column("roomtype",width=100)

                        self.room_table.pack(fill=BOTH,expand=1)
                        self.room_table.bind("<ButtonRelease-1>",self.get_cursor)
                        self.fetch_data()


#Add data

        def add_data(self):
                if self.var_floor.get()=="" or self.var_roomType.get()=="":
                        messagebox.showerror("Error!","All fields are mandatory",parent=self.root)
                else:
                        try:
                                conn=mysql.connector.connect(host="localhost", user="root",password="#Sooraj@1939",database="sys")
                                my_cursor=conn.cursor()
                                my_cursor.execute("insert into details values(%s,%s,%s)",(
                                                                                        self.var_floor.get(),
                                                                                        self.var_roomNo.get(),
                                                                                        self.var_roomType.get()
                                                                                    ))
                                conn.commit()
                                
                                self.fetch_data()
                                conn.close()                                            
                                messagebox.showinfo("Success","New Rooom Added Successfully.",parent=self.root)
                        except Exception as es:
                                messagebox.showwarning("Warning!",f"Something went wrong:{str(es)}",parent=self.root)


#fetch data
        def fetch_data(self):
                conn=mysql.connector.connect(host="localhost",user="root",password="#Sooraj@1939",database="sys")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from details")
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

                self.var_floor.set(row[0]),
                self.var_roomNo.set(row[1]),
                self.var_roomType.set(row[2])


#UPDATE FUNCTION
        def update(self):
                if self.var_contact.get()=="":
                        messagebox.showerror("Error!","Please Enter Floor No.",parent=self.root)
                else:
                        conn=mysql.connector.connect(host="localhost",user="root",password="#Sooraj@1939",database="sys")
                        my_cursor=conn.cursor()
                        my_cursor.execute("update details set Floor=%s,RoomType=%s where RoomNo=%s",(
   
                                                                                                self.var_floor.get(),
                                                                                                self.var_roomType.get(),
                                                                                                self.var_roomNo.get(),
                                                                                                 ))

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Update","Room details has been updated successfully.",parent=self.root)

        #DELETE FUNCTION
        def delete(self):
                delete=messagebox.askyesno("Hotel Management System","Do you want to delete this room details ?",parent=self.root)
                if delete>0:
                        conn=mysql.connector.connect(host="localhost",user="root",password="#Sooraj@1939",database="sys")
                        my_cursor=conn.cursor()
                        query="delete from details where roomNo=%s"
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
                self.var_floor.set(""),
                self.var_roomType.set(""),
                self.var_roomNo.set(""),







if __name__ == "__main__":
    root=Tk()
    obj=Detailsroom(root)
    root.mainloop()   
