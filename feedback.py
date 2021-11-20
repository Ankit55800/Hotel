from tkinter import*
from PIL import Image,ImageTk 
from tkinter import ttk
import mysql.connector
from tkinter import messagebox



class Feedback:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Empire")
        self.root.geometry("1320x565+205+228")

   #===================================================Variables============================================

        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_phone=StringVar()
        self.var_email=StringVar()
        self.var_gender=StringVar()
        self.var_complain=StringVar()



#==============================================================TableFrame=========================================================================================

        TableFrame=LabelFrame(self.root,bd=2,relief=RIDGE,text="Feedback",font=("times new roman",14,"bold"),padx=2)
        TableFrame.place(x=0,y=0,width=1320,height=560)

        lblSearchby = Label(TableFrame, font=('arial',12,'bold'), text="Search By:",bg="red",fg="white")
        lblSearchby.grid(row=0,column=0, sticky=W,padx=2)

        self.search_var=StringVar()
        CboSearch = ttk.Combobox(TableFrame,textvariable=self.search_var,state='readonly',font=('arial',12,'bold'), width=13)
        CboSearch ['value'] = (' ','Ref','Empid','Phone','Email')
        CboSearch.current(0)
        CboSearch.grid(row=0, column=1,padx=2)

        self.txt_search=StringVar()
        entSearch= Entry(TableFrame,textvariable=self.txt_search, font=('arial',12,'bold'), width=24)
        entSearch.grid(row=0,column=2,padx=2)


        btnSearch=Button(TableFrame,text="Search",width=10,font=("arial",11,"bold"),bg="grey",fg="black")
        btnSearch.grid(row=0,column=3,padx=2)

        btnShowAll=Button(TableFrame,text="Show All",width=10,font=("arial",11,"bold"),bg="grey",fg="black")
        btnShowAll.grid(row=0,column=4,padx=2)


#===================================================================Show Data Table===================================================================================

        detailsTable=Frame(TableFrame,bd=2,relief=RIDGE)
        detailsTable.place(x=0,y=50,width=1300,height=530)


        scroll_x=ttk.Scrollbar(detailsTable,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(detailsTable,orient=VERTICAL)

        self.Empdetails_table=ttk.Treeview(detailsTable,column=("fName","lName","gender","phone","email","feedback"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.Empdetails_table.xview)
        scroll_y.config(command=self.Empdetails_table.yview)

        self.Empdetails_table.heading("fName",text="First Name")
        self.Empdetails_table.heading("lName",text="Last Name")
        self.Empdetails_table.heading("gender",text="Gender")
        self.Empdetails_table.heading("phone",text="Phone")
        self.Empdetails_table.heading("email",text="Email")
        self.Empdetails_table.heading("feedback",text="Feedback")


        self.Empdetails_table["show"]="headings"


        self.Empdetails_table.column("fName",width=100)
        self.Empdetails_table.column("lName",width=100)
        self.Empdetails_table.column("gender",width=100)
        self.Empdetails_table.column("phone",width=100)
        self.Empdetails_table.column("email",width=100)
        self.Empdetails_table.column("feedback",width=100)


        self.Empdetails_table.pack(fill=BOTH,expand=1)
        self.Empdetails_table.bind("<ButtonRelease-1>")





















if __name__ == "__main__":
    root=Tk()
    obj=Feedback(root)
    root.mainloop()