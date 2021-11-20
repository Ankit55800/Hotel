from tkinter import*
from tkinter import ttk
import mysql
import mysql.connector
from tkinter import messagebox
import random
#import tempfile







class Payment:
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

     
        entAmt = Entry(labelframeleft,textvariable=self.amt, font=('arial',12,'bold') , width=18)
        entAmt.place(x=156,y=184)


        lblPay = Label(labelframeleft, font=('arial',12,'bold'), text="Payment Mode:",padx=2,pady=2)
        lblPay.place(x=0, y=220)
        CboPay = ttk.Combobox(labelframeleft,textvariable=self.payment,state='readonly',font=('arial',12,'bold'), width=16, height=15)
        CboPay ['value'] = ('Mode of payment', 'Online', 'Cheque', 'Cash')
        CboPay.current(0)
        CboPay.place(x=156, y=220)


        lblcheque = Label(labelframeleft, font=('arial',12,'bold'), text="Cheque No.:",padx=1)
        lblcheque.place(x=0,y=250)
        entcheque = Entry(labelframeleft,textvariable=self.chequeno,font=('arial',12,'bold'), width=18)
        entcheque.place(x=156,y=250)
        #entcheque.config(state="normal")

    
        







#==============================================================Buttons===========================================================================

        
        btn2=Button(labelframeleft,text="Print",command=self.print,width=10,font=("arial",11,"bold"),bg="orange",fg="black")
        btn2.place(x=0,y=290)
        btn3=Button(labelframeleft,text="Exit",command=self.cancel,width=10,font=("arial",11,"bold"),bg="red",fg="black")
        btn3.place(x=390,y=290)
        btn4=Button(labelframeleft,text="Pay",command=self.pay,width=10,font=("arial",11,"bold"),bg="red",fg="black")
        btn4.place(x=390,y=100)
        btn5=Button(labelframeleft,text="Total",command=self.total,width=15,font=("arial",11,"bold"),bg="red",fg="black")
        btn5.place(x=0,y=180)


        self.textarea=Text(labelframeleft)


#PRINT        
    def print(self):
        return

#CANCEL
    def cancel(self):
        self.root.destroy()

#total   
    def total(self):  
        amount=self.amount.get()
        bonus=self.bonus.get()  
        tot=amount+bonus
        self.amt.set(tot)
        #input_text.set(tot)

#PAY
    def pay(self):
        
        if self.payment.get()=='Mode of payment':
            messagebox.showerror("Error!","Please select a mode of payment.",parent=self.root)
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


            

 

if __name__ == "__main__":
    root=Tk()
    obj=Payment(root)
    root.mainloop()