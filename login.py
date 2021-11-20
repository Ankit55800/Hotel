from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk 
from tkinter import messagebox
from Hotel import HotelEmpire
from Main import Mainpage
import mysql
import mysql.connector
from tkcalendar import *




def main():
    win=Tk()
    app=Login(win)
    win.mainloop()


class Login:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Empire")
        self.root.geometry("1550x800+0+0")
      
#============================================================Image=====================================================================
        self.img1=ImageTk.PhotoImage(file=r"C:\Users\hp\Desktop\Hotel\images\bg12.jpg")
        lblimg1=Label(self.root,image=self.img1)
        lblimg1.place(x=0,y=0,width=1550,height=1100)


        frame=Frame(self.root,bg='black')
        frame.place(x=610,y=170,width=340,height=450)

        img2=Image.open(r"C:\Users\hp\Desktop\Hotel\images\person1.jpg")
        img2=img2.resize((100,100),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        lblimg2=Label(self.root,image=self.photoimg2,bg='black',bd=0)
        lblimg2.place(x=730,y=170,width=100,height=120)


        get_str=Label(frame,text="Get Started", font=("times new roman",20,"bold"),bg="black",fg="white")
        get_str.place(x=95,y=120)


#label
        lblUser=Label(frame,text="Username", font=("times new roman",15,"bold"),bg="black",fg="white")
        lblUser.place(x=70,y=165)
        self.txtUser=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtUser.place(x=40,y=200,width=270)

        lblPass=Label(frame,text="Password", font=("times new roman",15,"bold"),bg="black",fg="white")
        lblPass.place(x=70,y=235)
        self.txtpass=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtpass.place(x=40,y=270,width=270)

#Icon

        img3=Image.open(r"C:\Users\hp\Desktop\Hotel\images\person2.png")
        img3=img3.resize((25,25),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        lblimg3=Label(self.root,image=self.photoimg3,bg='black',bd=0)
        lblimg3.place(x=650,y=335,width=25,height=25)


        img4=Image.open(r"C:\Users\hp\Desktop\Hotel\images\lock.jpg")
        img4=img4.resize((25,25),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        lblimg4=Label(self.root,image=self.photoimg4,bg='black',bd=0)
        lblimg4.place(x=650,y=410,width=25,height=25)

#Login button
        btnlogin=Button(frame,command=self.loginadmin,text='Login as Admin',font=("times new roman",13,"bold"),bd=3, relief=RIDGE,fg='white',bg='red',activeforeground='white',activebackground='red')
        btnlogin.place(x=47,y=310,width=125,height=35)
        btnlogin=Button(frame,command=self.loginuser,text='Login as User',font=("times new roman",13,"bold"),bd=3, relief=RIDGE,fg='white',bg='red',activeforeground='white',activebackground='red')
        btnlogin.place(x=180,y=310,width=120,height=35)

#reg button
        btnreg=Button(frame,text='Registration',command=self.reg_win,font=("times new roman",12,"bold"),borderwidth=0,fg='white',bg='black',activeforeground='white',activebackground='black')
        btnreg.place(x=10,y=360,width=120,height=35)




    def reg_win(self):
        self.newwin=Toplevel(self.root)
        self.app=Register(self.newwin)



    def loginadmin(self):
        if self.txtUser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error", "All fields required.")
        elif self.txtUser.get()=="Admin@123" and self.txtpass.get()=="1939":
            messagebox.showinfo("Successful","Welcome to Hotel Empire.")
            self.new_window=Toplevel(self.root)
            self.app=HotelEmpire(self.new_window)
        else:
            messagebox.showerror("Invalid","Invalid Username & Password")


    def loginuser(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="#Sooraj@1939",database="sys")
        my_cursor=conn.cursor()
        uname=self.txtUser.get()
        passw=self.txtpass.get()
        
        my_cursor.execute("Select * from registration where Email = %s and New_Password= %s",(uname,passw))
        
        results = my_cursor.fetchall()
        if results:
            for i in results:
                messagebox.showinfo("Successful","Welcome to Hotel Empire.")
                self.new_window=Toplevel(self.root)
                self.app=Mainpage(self.new_window)
        else:
            messagebox.showerror("Invalid","Invalid Username or Password")
        if self.txtUser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error", "All fields required.")
        conn.close()


#SAI Reg.

class Register:
    def __init__(self,root):
        root.title("Hotel Empire")
        root.geometry("600x600+450+130")


        
        var_fname=StringVar()
        var_lname=StringVar()
        var_phone=IntVar()
        var_email=StringVar()
        var_ques=StringVar()
        var_ans=StringVar()
        var_pass=StringVar()
        var_cpass=StringVar()

        frame_all=LabelFrame(root,bd=2,relief=RIDGE,text="Registration",font=("times new roman",14,"bold"),padx=2)
        frame_all.place(x=0,y=0,width=600,height=600)
        frame_all.config(bg='#84a98c')


        fname = Label(frame_all, text="First Name",  font=("Arial",12), bg="#457b9d", padx=10, pady=5).place(x=15 ,y=70)
        Lname = Label(frame_all, text="Last Name",  font=("Arial",12), bg="#457b9d", padx=10, pady=5).place(x=275 ,y=70)
        f_entry = Entry(frame_all, font=("Arial",12)).place(x=15 ,y=110)
        L_entry = Entry(frame_all,  font=("Arial",12)).place(x=275 ,y=110)

        contact = Label(frame_all, text="Contact Number",  font=("Arial",12), bg="#457b9d", padx=10, pady=5).place(x=15 ,y=150)
        email = Label(frame_all, text="Email", font=("Arial",12), bg="#457b9d", padx=10, pady=5).place(x=275 ,y=150)
        contact_entry = Entry(frame_all, font=("Arial",12)).place(x=15 ,y=190)
        email_entry = Entry(frame_all, font=("Arial",12)).place(x=275 ,y=190)




        security = Label(frame_all, text="Select Security Question", font=("Arial",12), bg="#457b9d", padx=10, pady=5).place(x=15 ,y=230)
        s_answer = Label(frame_all, text="Security Answer", font=("Arial",12), bg="#457b9d", padx=10, pady=5).place(x=275 ,y=230)
        select_question = ttk.Combobox(frame_all, state= 'readonly', font=("Arial",12))
        select_question['values']=("select", "Name of your First Pet", "Your native place", "Name of your first School")
        select_question.place(x=15 ,y=270)
        select_question.current(0)
        type_answer = Entry(frame_all, font=("Arial",12)).place(x=275 ,y=270)


        password = Label(frame_all, text="Type New Password", font=("Arial",12), bg="#457b9d", padx=10, pady=5).place(x=15 ,y=310)
        confirm_password = Label(frame_all, text="Confirm New Password", font=("Arial",12), bg="#457b9d", padx=10, pady=5).place(x=275 ,y=310)
        pword = Entry(frame_all, font=("Arial",12)).place(x=15 ,y=350)
        cpword = Entry(frame_all, font=("Arial",12)).place(x=275 ,y=350)

        TandC = Checkbutton(frame_all, text="I agree to Terms and Conditions", onvalue=1, offvalue=0, bg="#457b9d").place(x=15 ,y=390)

        def register():
            conn=mysql.connector.connect (host="localhost", user="root", password="#Sooraj@1939", database="sys")
            my_cursor=conn.cursor()
            my_cursor.execute("insert into registration values(%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                            var_fname.get(),
                                                            var_lname.get(),
                                                            var_phone.get(),
                                                            var_email.get(),
                                                            var_ques.get(),
                                                            var_ans.get(),
                                                            var_pass.get(),
                                                            var_cpass.get()



            ))
            conn.commit()
            messagebox.showinfo("Success","Registration Successfull!",parent=root)
            conn.close()
    



        Register= Button(frame_all, text="REGISTER",  font=("Arial",15), bg="#457b9d",padx=70, command = register).place(x=25 ,y=450)

        def login():
            new_window=Toplevel(root)
            app=Login(new_window)

        Loginbtn= Button(frame_all, text="LOGIN",  font=("Arial",15), bg="#457b9d",padx=70, command = login).place(x=25 ,y=500)








if __name__ == "__main__":
    main()