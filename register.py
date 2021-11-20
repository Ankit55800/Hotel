from tkinter import*
from tkinter import ttk
from tkinter import font
from PIL import Image,ImageTk
import mysql
import mysql.connector 
from tkinter import messagebox
from login import Login

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
        f_entry = Entry(frame_all,textvariable=var_fname, font=("Arial",12)).place(x=15 ,y=110)
        L_entry = Entry(frame_all, textvariable=var_lname, font=("Arial",12)).place(x=275 ,y=110)

        contact = Label(frame_all, text="Contact Number",  font=("Arial",12), bg="#457b9d", padx=10, pady=5).place(x=15 ,y=150)
        email = Label(frame_all, text="Email", font=("Arial",12), bg="#457b9d", padx=10, pady=5).place(x=275 ,y=150)
        contact_entry = Entry(frame_all,textvariable=var_phone, font=("Arial",12)).place(x=15 ,y=190)
        email_entry = Entry(frame_all,textvariable=var_email, font=("Arial",12)).place(x=275 ,y=190)




        security = Label(frame_all, text="Select Security Question", font=("Arial",12), bg="#457b9d", padx=10, pady=5).place(x=15 ,y=230)
        s_answer = Label(frame_all, text="Security Answer", font=("Arial",12), bg="#457b9d", padx=10, pady=5).place(x=275 ,y=230)
        select_question = ttk.Combobox(frame_all,textvariable=var_ques, state= 'readonly', font=("Arial",12))
        select_question['values']=("select", "Name of your First Pet", "Your native place", "Name of your first School")
        select_question.place(x=15 ,y=270)
        select_question.current(0)
        type_answer = Entry(frame_all,textvariable=var_ans, font=("Arial",12)).place(x=275 ,y=270)


        password = Label(frame_all, text="Type New Password", font=("Arial",12), bg="#457b9d", padx=10, pady=5).place(x=15 ,y=310)
        confirm_password = Label(frame_all, text="Confirm New Password", font=("Arial",12), bg="#457b9d", padx=10, pady=5).place(x=275 ,y=310)
        pword = Entry(frame_all, textvariable=var_pass,font=("Arial",12)).place(x=15 ,y=350)
        cpword = Entry(frame_all,textvariable=var_cpass, font=("Arial",12)).place(x=275 ,y=350)

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
    root=Tk()
    obj=Register(root)
    root.mainloop()    