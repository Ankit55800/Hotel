from tkinter import*
from PIL import Image,ImageTk 
from tkinter import ttk
import random
import mysql
import mysql.connector
from tkinter import messagebox
from pay import Payment



class Employee:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Empire")
        self.root.geometry("1320x565+205+228")

        self.img1=ImageTk.PhotoImage(file=r"C:\Users\hp\Desktop\Hotel\images\bgg2.jpg")
        lblimg1=Label(self.root,image=self.img1)
        lblimg1.place(x=0,y=0,relwidth=1,relheight=1)
   #===================================================Variables============================================

        self.var_empid=StringVar()
        x=random.randint(1000,9999)
        self.var_empid.set(str(x))


        self.var_fName=StringVar()
        self.var_lName=StringVar()
        self.var_dob=StringVar()
        self.var_loc=StringVar()
        self.var_doj=StringVar()
        self.var_phone=StringVar()
        self.var_email=StringVar()
        self.var_gender=StringVar()
        self.var_dept=StringVar()
        self.var_desig=StringVar()



#==========================================================Title===========================================================================
        lbl_title=Label(self.root,text="Add Employee Details" , font=("times new roman",18,"bold"),bg="black",fg="white",relief=RIDGE)
        lbl_title.place(x=0,y=0,width=425,height=50)

#========================================================Label Frame=================================================================================

        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Employee Details",font=("times new roman",14,"bold"),padx=2)
        labelframeleft.place(x=0,y=60,width=425,height=500)
        labelframeleft.config(bg='#344e41')



#========================================================Label & Enterys=================================================================================


        lblEmpId = Label(labelframeleft, font=('arial',12,'bold'),bg="#344e41",fg="white", text="Employee ID:",padx=1,pady=2)
        lblEmpId.grid(row=0,column=0, sticky=W)
        entEmpId = Entry(labelframeleft,textvariable=self.var_empid,font=('arial',12,'bold'), width=18,state='readonly')
        entEmpId.grid(row=0,column=1,pady=5,padx=20)


        lblFirstname = Label(labelframeleft, font=('arial',12,'bold'),bg="#344e41",fg="white", text="Firstname:",padx=1)
        lblFirstname.grid(row=1,column=0, sticky=W)
        enttFirstname = Entry(labelframeleft,textvariable=self.var_fName, font=('arial',12,'bold'), width=18)
        enttFirstname.grid(row=1,column=1,pady=3,padx=20)

        lblLastname = Label(labelframeleft, font=('arial',12,'bold'),bg="#344e41",fg="white", text="Lastname:",padx=1)
        lblLastname.grid(row=2,column=0, sticky=W)
        entLastname = Entry(labelframeleft,textvariable=self.var_lName, font=('arial',12,'bold'), width=18)
        entLastname.grid(row=2,column=1,pady=3,padx=20)


        lblDOB = Label(labelframeleft, font=('arial',12,'bold'),bg="#344e41",fg="white", text="DOB:",padx=1)
        lblDOB.grid(row=3,column=0, sticky=W)
        entDOB = Entry(labelframeleft,textvariable=self.var_dob, font=('arial',12,'bold'), width=18)
        entDOB.grid(row=3,column=1,pady=3,padx=20)

        
        lblloc = Label(labelframeleft, font=('arial',12,'bold'),bg="#344e41",fg="white", text="Location:",padx=1)
        lblloc.grid(row=4,column=0, sticky=W)
        entloc = Entry(labelframeleft,textvariable=self.var_loc, font=('arial',12,'bold'), width=18)
        entloc.grid(row=4,column=1,pady=3,padx=20)

        lblDOJ = Label(labelframeleft, font=('arial',12,'bold'),bg="#344e41",fg="white", text="DOJ:",padx=1)
        lblDOJ.grid(row=5,column=0, sticky=W)
        entDOJ = Entry(labelframeleft,textvariable=self.var_doj,font=('arial',12,'bold'), width=18)
        entDOJ.grid(row=5,column=1,pady=3,padx=20)


        lblphone = Label(labelframeleft, font=('arial',12,'bold'),bg="#344e41",fg="white", text="Phone:",padx=1)
        lblphone.grid(row=6,column=0, sticky=W)
        entphone = Entry(labelframeleft,textvariable=self.var_phone, font=('arial',12,'bold'), width=18)
        entphone.grid(row=6,column=1,pady=3,padx=20)


        lblemail = Label(labelframeleft, font=('arial',12,'bold'),bg="#344e41",fg="white", text="Email:",padx=1)
        lblemail.grid(row=7,column=0, sticky=W)
        entemail = Entry(labelframeleft,textvariable=self.var_email, font=('arial',12,'bold'), width=18)
        entemail.grid(row=7,column=1,pady=3,padx=20)


        lbldep = Label(labelframeleft, font=('arial',12,'bold'),bg="#344e41",fg="white", text="Department:",padx=1)
        lbldep.grid(row=8,column=0, sticky=W)
        entdep = Entry(labelframeleft,textvariable=self.var_dept, font=('arial',12,'bold'), width=18)
        entdep.grid(row=8,column=1,pady=3,padx=20)

        lbldesig = Label(labelframeleft, font=('arial',12,'bold'),bg="#344e41",fg="white", text="Designation:",padx=1)
        lbldesig.grid(row=9,column=0, sticky=W)
        entdesig = Entry(labelframeleft,textvariable=self.var_desig, font=('arial',12,'bold'), width=18)
        entdesig.grid(row=9,column=1,pady=3,padx=20)

        lblGender = Label(labelframeleft, font=('arial',12,'bold'),bg="#344e41",fg="white", text="Gender:",padx=2,pady=2)
        lblGender.grid(row=10,column=0, sticky=W)
        CboGender = ttk.Combobox(labelframeleft,textvariable=self.var_gender,state='readonly',font=('arial',12,'bold'), width=16)
        CboGender ['value'] = ('Select Gender', 'Male', 'Female', 'Others','Prefer Not Say')
        CboGender.current(0)
        CboGender.grid(row=10, column=1, pady=3, padx=2)


        btnAdd=Button(labelframeleft,text="Payment",command=self.pay,width=10,font=("arial",11,"bold"),bg="orange",fg="black")
        btnAdd.place(x=275,y=350)
        


#==============================================================Buttons===========================================================================

        btnFrame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btnFrame.place(x=0,y=430,width=412,height=37)
        btnFrame.config(bg='black')     

        btnAdd=Button(btnFrame,text="Add",command=self.add_data,width=10,font=("arial",11,"bold"),bg="black",fg="white")
        btnAdd.grid(row=0,column=0,padx=1)

        btnUpdate=Button(btnFrame,text="Update",command=self.update,width=10,font=("arial",11,"bold"),bg="black",fg="white")
        btnUpdate.grid(row=0,column=1,padx=1)

        btnDelete=Button(btnFrame,text="Delete",command=self.delete,width=10,font=("arial",11,"bold"),bg="black",fg="white")
        btnDelete.grid(row=0,column=2,padx=1)

        btnReset=Button(btnFrame,text="Reset",command=self.reset,width=10,font=("arial",11,"bold"),bg="black",fg="white")
        btnReset.grid(row=0,column=3,padx=1)

#==============================================================TableFrame=========================================================================================

        TableFrame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details",font=("times new roman",14,"bold"),padx=2)
        TableFrame.place(x=443,y=60,width=865,height=500)
        TableFrame.config(bg='#84a98c')

        lblSearchby = Label(TableFrame, font=('arial',12,'bold'), text="Search By:",bg="red",fg="white")
        lblSearchby.grid(row=0,column=0, sticky=W,padx=2)

        self.search_var=StringVar()
        CboSearch = ttk.Combobox(TableFrame,textvariable=self.search_var,state='readonly',font=('arial',12,'bold'), width=13)
        CboSearch ['value'] = ('empid')
        CboSearch.current(0)
        CboSearch.grid(row=0, column=1,padx=2)

        self.var_search=StringVar()
        entSearch= Entry(TableFrame,textvariable=self.var_search, font=('arial',12,'bold'), width=24)
        entSearch.grid(row=0,column=2,padx=2)


        btnSearch=Button(TableFrame,text="Search",command=self.search,width=10,font=("arial",11,"bold"),bg="black",fg="white")
        btnSearch.grid(row=0,column=3,padx=2)

        btnShowAll=Button(TableFrame,text="Show All",command=self.fetch_data,width=10,font=("arial",11,"bold"),bg="black",fg="white")
        btnShowAll.grid(row=0,column=4,padx=2)


#===================================================================Show Data Table===================================================================================

        detailsTable=Frame(TableFrame,bd=2,relief=RIDGE)
        detailsTable.place(x=0,y=50,width=860,height=400)


        scroll_x=ttk.Scrollbar(detailsTable,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(detailsTable,orient=VERTICAL)

        self.Empdetails_table=ttk.Treeview(detailsTable,column=("empid","fName","lName",
        "dob","loc","doj","phone","email","dept","desig","gender"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.Empdetails_table.xview)
        scroll_y.config(command=self.Empdetails_table.yview)

        self.Empdetails_table.heading("empid",text="Emp ID")
        self.Empdetails_table.heading("fName",text="First Name")
        self.Empdetails_table.heading("lName",text="Last Name")
        self.Empdetails_table.heading("dob",text="DOB")
        self.Empdetails_table.heading("loc",text="Location")
        self.Empdetails_table.heading("doj",text="DOJ")
        self.Empdetails_table.heading("phone",text="Phone")
        self.Empdetails_table.heading("email",text="Email")
        self.Empdetails_table.heading("dept",text="Department")
        self.Empdetails_table.heading("desig",text="Desig")
        self.Empdetails_table.heading("gender",text="Gender")

        self.Empdetails_table["show"]="headings"


        self.Empdetails_table.column("empid",width=100)
        self.Empdetails_table.column("fName",width=100)
        self.Empdetails_table.column("lName",width=100)
        self.Empdetails_table.column("dob",width=100)
        self.Empdetails_table.column("loc",width=100)
        self.Empdetails_table.column("doj",width=100)
        self.Empdetails_table.column("phone",width=100)
        self.Empdetails_table.column("email",width=100)
        self.Empdetails_table.column("dept",width=100)
        self.Empdetails_table.column("desig",width=100)
        self.Empdetails_table.column("gender",width=100)

        self.Empdetails_table.pack(fill=BOTH,expand=1)
        self.Empdetails_table.bind("<ButtonRelease-1>",self.get_cursor)
 

#ADD FUNCTION  
    def add_data(self):
            try:
                conn=mysql.connector.connect (host="localhost", user="root", password="#Sooraj@1939", database="sys")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into employee values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                        self.var_empid.get(),
                                                                                        self.var_fName.get(),
                                                                                        self.var_lName.get(),
                                                                                        self.var_dob.get(),
                                                                                        self.var_loc.get(),
                                                                                        self.var_doj.get(),
                                                                                        self.var_phone.get(),
                                                                                        self.var_email.get(),                                                                                                                                                                                                                                         
                                                                                        self.var_dept.get(),
                                                                                        self.var_desig.get(),
                                                                                        self.var_gender.get()     
                                                                                    ))
                conn.commit()
                self.fetch_data()
                conn.close()                                            
                messagebox.showinfo("Success","Employee has been added",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning!",f"Something went wrong:{str(es)}",parent=self.root)

                    #FETCHING DATA

    def fetch_data(self):
                conn=mysql.connector.connect(host="localhost",user="root",password="#Sooraj@1939",database="sys")
                my_cursor=conn.cursor()
                my_cursor.execute("SELECT * from employee")
                rows=my_cursor.fetchall()
                if len(rows)!=0:
                    self.Empdetails_table.delete(*self.Empdetails_table.get_children())
                for i in rows:
                    self.Empdetails_table.insert("",END,values=i)
                conn.commit()
                conn.close()


    def get_cursor(self,event=""):
        cursor_row=self.Empdetails_table.focus()
        content=self.Empdetails_table.item(cursor_row)
        row=content["values"]

        self.var_empid.set(row[0]),
        self.var_fName.set(row[1]),
        self.var_lName.set(row[2]),
        self.var_dob.set(row[3]),
        self.var_loc.set(row[4]),
        self.var_doj.set(row[5]),
        self.var_phone.set(row[6])
        self.var_email.set(row[7]),
        self.var_dept.set(row[8]),
        self.var_desig.set(row[9]),
        self.var_gender.set(row[10]),
          

#UPDATE FUNCTION
    def update(self):
        if self.var_phone.get()=="":
            messagebox.showerror("Error!","Please Enter Phone No.",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="#Sooraj@1939",database="sys")
            my_cursor=conn.cursor()
            my_cursor.execute("UPDATE employee set FName=%s,LName=%s,DOB=%s,Location=%s,DOJ=%s,Phone=%s,Email=%s,Desig=%s,Dept=%s,Gender=%s where empid=%s",(
                                                                                                                                                                        
                                                                                                                                                                        self.var_fName.get(),
                                                                                                                                                                        self.var_lName.get(),
                                                                                                                                                                        self.var_dob.get(),
                                                                                                                                                                        self.var_loc.get(),
                                                                                                                                                                        self.var_doj.get(),
                                                                                                                                                                        self.var_phone.get(),
                                                                                                                                                                        self.var_email.get(),
                                                                                                                                                                        self.var_desig.get(),
                                                                                                                                                                        self.var_dept.get(),
                                                                                                                                                                        self.var_gender.get(),
                                                                                                                                                                        self.var_empid.get()


                                                                                                                                                                    ))

            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","Employee details has benn updated successfully.",parent=self.root)

#DELETE FUNCTION
    def delete(self):
        delete=messagebox.askyesno("Hotel Empire","Do you want to delete this Employee ?",parent=self.root)
        if delete>0:
            conn=mysql.connector.connect(host="localhost",user="root",password="#Sooraj@1939",database="sys")
            my_cursor=conn.cursor()
            query="delete from employee where empid=%s"
            value=(self.var_empid.get(),)
            my_cursor.execute(query,value)
        else:
            if not delete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

#RESET FUNCTION
    def reset(self):
        self.var_empid.set(""),
        self.var_fName.set(""),
        self.var_lName.set(""),
        self.var_dob.set(""),
        self.var_loc.set(""),
        self.var_doj.set(""),
        self.var_phone.set(""),
        self.var_email.set(""),
        self.var_gender.set(""),
        self.var_dept.set(""),
        self.var_desig.set("")

        x=random.randint(1000,9999)
        self.var_empid.set(str(x))

#SEARCH FUNCTION    ----- made changes
    def search(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="#Sooraj@1939",database="sys")
        my_cursor=conn.cursor()
        query="select * from employee where empid = %s"
        val=(self.var_search.get(),)
        my_cursor.execute(query,val)
        rows=my_cursor.fetchall()
        if len (rows)!=0:
            self.Empdetails_table.delete(*self.Empdetails_table.get_children())
            for i in rows:
                self.Empdetails_table.insert("",END,values=i)
        else:
            y = messagebox.showwarning("Warning","Employee Not Found !",parent=self.root)   
        conn.commit()
        conn.close()




    def pay(self):
        self.new_window=Toplevel(self.root)
        self.app=Payment(self.new_window)








if __name__ == "__main__":
    root=Tk()
    obj=Employee(root)
    root.mainloop()