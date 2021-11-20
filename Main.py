from tkinter import*
from tkcalendar import *
from PIL import Image,ImageTk
from tkinter import ttk
import random
from tkinter import messagebox
import mysql
import mysql.connector



class Mainpage:
    def __init__(self,root):
        root=root
        root.title("Hotel Empire")
        root.geometry("1920x1080")
        root.config(bg='#FDFCDC')


        var_name=StringVar()
        var_checkin_date = StringVar()
        var_stay_duration = StringVar()
        var_room_type = StringVar()
        var_Identity_Proof=StringVar()
        var_address=StringVar()
        var_idNo=StringVar()
        var_mobile=StringVar()
        var_email=StringVar()
        var_gender=StringVar()
        var_mealtype=StringVar()
        var_price=StringVar()



        var_ref=StringVar()
        x=random.randint(100000,999999)
        var_ref.set(int(x))




        # Define image
        self.img1=ImageTk.PhotoImage(file=r"C:\Users\hp\Desktop\Hotel\images\bgimg.png")
        lblimg1=Label(root,image=self.img1)
        lblimg1.place(x=0,y=0,relwidth=1,relheight=1)
        #newimage


        # Create a canvas
        my_canvas = Canvas(root, width=1920, height=1808)
        my_canvas.pack(fill="both", expand=True)

        # Set image in canvas
        my_canvas.create_image(0,0, image=self.img1, anchor="nw")





        #outline
        Label1 = Label(root, bg="#ebf8ff", padx=200  , pady=290  ).place(x=70 ,y=130)
        Label2 = Label(root, bg="#ebf8ff", padx=355  , pady=25 ).place(x=645 ,y=45)
        Label3 = Label(root, bg="#ebf8ff", padx=350  , pady=290  ).place(x=650 ,y=130)

        #frames
        Frame1 = Frame(root, bg="#ebf8ff", padx=200  , pady=340  ).place(x=70 ,y=50)
        Frame2 = Frame(root, bg="#ebf8ff", padx=350  , pady=20 ).place(x=650 ,y=50)
        Frame3 = Frame(root, bg="#ebf8ff", padx=350  , pady=300  ).place(x=650 ,y=125)

        combostyle = ttk.Style()

        combostyle.theme_create('combostyle', parent='alt',
                                settings = {'TCombobox':
                                            {'configure':
                                            {'fieldbackground': '#0096c7',
                                            'background': '#0077b6'
                                            }}}
                                )
        # ATTENTION: this applies the new style 'combostyle' to all ttk.Combobox
        combostyle.theme_use('combostyle') 





        #function for room booking
        def roomBooking():


            def Roomtype():
                if var_room_type.get()=="Standard":
                    var_price="2000"
                elif var_room_type.get()=="Deluxe":
                    var_price="3500"
                else :
                    var_price="5000"

            def Payment():
                global payment
                payment=Tk()
                payment.title('Registration Form')
                payment.geometry("600x300")
                Frame3 = Frame(payment, bg="#ebf8ff", padx=350  , pady=300  ).place(x=650 ,y=125)
                Roompayment = Button(payment, text="Pay Now",bg="#00043a", fg="#e3f2fd", padx=121 ,  font=('Eina01',24), borderwidth=0, command=add_data).place(x=100 ,y=130)
            def confirmbooking():
                if var_Identity_Proof.get() =="select id type":
                    messagebox.showwarning("Warning","Please select Id type",parent=root)
                elif var_idNo.get() == "":
                    messagebox.showwarning("Warning","Enter Valid ID",parent=root)
                elif var_room_type.get() == "select room type":
                    messagebox.showwarning("Warning","Please select room type",parent=root)
                else:
                    Payment()




            #ADD FUNCTION
            def add_data():
                
                if var_mobile.get()=="" or var_ref.get()=="" or var_name.get()=="" or var_room_type.get()=="select room type":
                    messagebox.showerror("Error!","All fields are mandatory",parent=root)
                else:
                    try:
                        conn=mysql.connector.connect (host="localhost", user ="root", password="#Sooraj@1939", database="sys")
                        my_cursor=conn.cursor()
                        my_cursor.execute("insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                var_ref.get(),
                                                                                                var_gender.get(),
                                                                                                var_mobile.get(),
                                                                                                var_email.get(),                                                                                        
                                                                                                var_idNo.get(),
                                                                                                var_address.get(),  
                                                                                                var_name.get(),
                                                                                                my_label.cget("text"),
                                                                                                var_stay_duration.get(),
                                                                                                var_Identity_Proof.get(),
                                                                                                var_room_type.get()
                                                                                            ))
                        conn.commit()
                        conn.close()                                            
                        messagebox.showinfo("Success","Booking Confirmed",parent=root)
                        payment.destroy()
                    except Exception as es:
                        messagebox.showwarning("Warning!",f"Something went wrong:{str(es)}",parent=root)

                            #FETCHING DATA

            
            
            Label3 = Label(root, bg="#ebf8ff", padx=350  , pady=290  ).place(x=650 ,y=130)
            Frame3 = Frame(root, bg="#ebf8ff", padx=350  , pady=300  ).place(x=650 ,y=125)

        
                


            def calendar():
                datewindow = Tk()
                datewindow.title('Pick a date')
                datewindow.geometry("300x250")

                cal = Calendar(datewindow, selectmode="day", date_pattern= 'dd/mm/yy', year=2021, month=11, day=13)
                cal.pack()

                def grab_date():
                    my_label.config(text=cal.get_date())
                    datewindow.destroy()

                my_button = Button(datewindow, text="Get date", command=grab_date,)  
                my_button.pack(pady=20)
            

            #labels Booking ID, Name, Identity proof, Address, Contact,Checkin Date, Stay Duration, Room Type, Avalible Rooms
            global my_label
            my_label = Label(root, width=19 ,padx=3, pady=5, bg="#0096c7" ,text="", anchor='w', font=('Eina01',24))  
            my_label.place(x=930,y=422)


            L_BookingID = Label(root, text="Booking ID", bg="#0077b6", fg="#e3f2fd", font=('Eina01',24),padx=60).place(x=670,y=170)
            L_Name = Label(root, text="Name", bg="#0096c7", fg="#e3f2fd", font=('Eina01',24),padx=90).place(x=670,y=212)
            L_IdentityProof = Label(root, text="Identity Proof", bg="#0077b6", fg="#e3f2fd", font=('Eina01',24),padx=55).place(x=670,y=254)
            L_IdentityNumber = Label(root, text="Identity Number", bg="#0096c7", fg="#e3f2fd", font=('Eina01',24),padx=30).place(x=670,y=296)
            L_Address = Label(root, text="Address", bg="#0077b6", fg="#e3f2fd", font=('Eina01',24),padx=80).place(x=670,y=338)
            L_Contact = Label(root, text="Contact", bg="#0096c7", fg="#e3f2fd", font=('Eina01',24),padx=75).place(x=670,y=380)
            L_Checkin_Date = Label(root, text="Checkin Date", bg="#0077b6", fg="#e3f2fd", font=('Eina01',24),padx=35).place(x=670,y=422)
            L_StayDuration = Label(root, text="Stay Duration", bg="#0096c7", fg="#e3f2fd", font=('Eina01',24),padx=40).place(x=670,y=464)
            L_Room_type = Label(root, text="Room Type", bg="#0077b6", fg="#e3f2fd", font=('Eina01',24),padx=60).place(x=670,y=506)
            L_Gender = Label(root, text="Gender", bg="#0096c7", fg="#e3f2fd", font=('Eina01',24),padx=80).place(x=670,y=548)
            L_Email = Label(root, text="Mail ID", bg="#0077b6", fg="#e3f2fd", font=('Eina01',24),padx=80).place(x=670,y=590)



            #Label widget for displaying date
            
            
            B_Get_Date = Button(root, text="Pick Date ▼",font=('Helvatica',18),bg="#0096c7", command=calendar).place(x=1162,y=422)


            #Entry widgets
            E_BookingID = Entry(root, textvariable=var_ref, width=20, font=('Eina01',26), bg="#0077b6").place(x=932,y=170)
            E_Name = Entry(root,textvariable=var_name ,width=20, font=('Eina01',26), bg="#0096c7").place(x=932,y=212)
            E_IdentityProof = ttk.Combobox(root,textvariable=var_Identity_Proof , width=19, font=('Eina01',26), state= 'readonly')
            E_IdentityProof['values']=("select id type", "Aadhar Card", "Pan Card", "Passport")
            E_IdentityProof.place(x=932,y=254)
            E_IdentityProof.current(0)
            E_IdentityNumber = Entry(root,textvariable=var_idNo , width=20, font=('Eina01',26),bg="#0077b6").place(x=932,y=296)
            E_Address = Entry(root, textvariable=var_address ,width=20, font=('Eina01',26),bg="#0096c7").place(x=932,y=338)
            E_Contact = Entry(root, textvariable=var_mobile , width=20, font=('Eina01',26),bg="#0077b6").place(x=932,y=380)
            
            E_StayDuration = Entry(root, textvariable=var_stay_duration , width=20, font=('Eina01',26),bg="#0077b6").place(x=932,y=464)
            C_Room_type = ttk.Combobox(root, textvariable=var_room_type, width=20 , state= 'readonly', font=('Eina01',25))

            C_Room_type['values']=("select room type", "Standard | RS.2500/-", "Deluxe | RS.4500/-", "Suite | RS.6500/-")
            C_Room_type.place(x=932,y=506)
            C_Room_type.current(0)

            C_Gender = ttk.Combobox(root, textvariable=var_gender, width=20 , state= 'readonly', font=('Eina01',24))

            C_Gender['values']=("select your Gender", "Male", "Female", "Other")
            C_Gender.place(x=932,y=548)
            C_Gender.current(0)
            E_Mail = Entry(root, textvariable=var_email , width=20, font=('Eina01',26),bg="#0077b6").place(x=932,y=588)





            confirm_Booking = Button(root, text="Confirm Booking", bg="#00043a", fg="#e3f2fd", padx=35 ,  font=('Eina01',24), borderwidth=0, command=confirmbooking ).place(x=670,y=650)



        #function for meals

        def meals():

            Label3 = Label(root, bg="#ebf8ff", padx=350  , pady=290  ).place(x=650 ,y=130)
            Frame3 = Frame(root, bg="#ebf8ff", padx=350  , pady=300  ).place(x=650 ,y=125)
            #labels Booking ID, Name, Identity proof, Address, Contact,Checkin Date, Stay Duration, Room Type, Avalible Rooms

            L_BookingID = Label(root, text="Booking ID", bg="#0077b6", fg="#e3f2fd", font=('Eina01',24),padx=60).place(x=670,y=170)
            L_Name = Label(root, text="Name", bg="#0096c7", fg="#e3f2fd", font=('Eina01',24),padx=90).place(x=670,y=212)
            L_Food = Label(root, text="Items Avalible", bg="#0077b6", fg="#e3f2fd", font=('Eina01',24),padx=40).place(x=670,y=254)
            
            #Meals confirmation
            def mealconfirmation():
                if var_mealtype.get() =="Choose your Meal":
                    messagebox.showwarning("Warning","Please select your meal Type",parent=root)

                else:
                    messagebox.showinfo("Success","Your Order is on the way, Payment will be collected infort of the door",parent=root)




            #Entry widgets
            
            E_BookingID = Entry(root, textvariable=var_ref, width=20, font=('Eina01',26), bg="#0077b6").place(x=932,y=170)
            E_Name = Entry(root,textvariable=var_name ,width=20, font=('Eina01',26), bg="#0096c7").place(x=932,y=212)
            C_Meal_type = ttk.Combobox(root, textvariable=var_mealtype , width=19 , state= 'readonly', font=('Eina01',26))

            C_Meal_type['values']=("Choose your Meal", "Breakfast", "Lunch", "Dinner")
            C_Meal_type.place(x=932,y=252)
            C_Meal_type.current(0)
            #Check Avalible rooms

            confirm_order = Button(root, text="Confirm Order", bg="#00043a", fg="#e3f2fd", padx=35 ,  font=('Eina01',24), borderwidth=0, command=mealconfirmation ).place(x=670,y=650)


            #placefiller
            L_Filler = Label(root, bg="#0096c7", padx=311, pady=30).place(x=670,y=545)


        #function for receipt

        def receipt():
            
            #outline
            Label3 = Label(root, bg="#ebf8ff", padx=350  , pady=290  ).place(x=650 ,y=130)
            Frame3 = Frame(root, bg="#ebf8ff", padx=350  , pady=300  ).place(x=650 ,y=125)
        #fetch data
            conn=mysql.connector.connect(host="localhost",user ="root",password="#Sooraj@1939",database="sys")
            my_cursor=conn.cursor()
            my_cursor.execute("SELECT checkin_date FROM sys.customer WHERE Ref = "+ str(var_ref.get()))
            date=my_cursor.fetchall()
            E_Checkin_Date = Label(root, text=date, width=19 ,padx=14, anchor='w',font=('Eina01',25),bg="#0096c7").place(x=922,y=379)
            

            #labels Booking ID, Name, Identity proof, Address, Contact,Checkin Date, Stay Duration, Room Type, Avalible Rooms

            L_BookingID = Label(root, text="Booking ID", bg="#0077b6", fg="#e3f2fd", font=('Eina01',24),padx=60).place(x=670,y=170)
            L_Name = Label(root, text="Name", bg="#0096c7", fg="#e3f2fd", font=('Eina01',24),padx=90).place(x=670,y=212)
            L_IdentityProof = Label(root, text="Identity Proof", bg="#0077b6", fg="#e3f2fd", font=('Eina01',24),padx=60).place(x=670,y=254)
            L_Address = Label(root, text="Address", bg="#0096c7", fg="#e3f2fd", font=('Eina01',24),padx=80).place(x=670,y=296)
            L_Contact = Label(root, text="Contact", bg="#0077b6", fg="#e3f2fd", font=('Eina01',24),padx=75).place(x=670,y=338)
            L_Checkin_Date = Label(root, text="Checkin Date", bg="#0096c7", fg="#e3f2fd", font=('Eina01',24),padx=32).place(x=670,y=380)
            L_StayDuration = Label(root, text="Stay Duration", bg="#0077b6", fg="#e3f2fd", font=('Eina01',24),padx=40).place(x=670,y=422)
            L_Room_type = Label(root, text="Room Type", bg="#0096c7", fg="#e3f2fd", font=('Eina01',24),padx=60).place(x=670,y=464)

            #Entry widgets

            E_BookingID = Entry(root, textvariable=var_ref, width=20, font=('Eina01',26), bg="#0077b6").place(x=932,y=170)
            E_Name = Entry(root,textvariable=var_name ,width=20, font=('Eina01',26), bg="#0096c7").place(x=932,y=212)
            E_IdentityProof = Entry(root,textvariable=var_Identity_Proof , width=20, font=('Eina01',26),bg="#0077b6").place(x=932,y=254)
            E_Address = Entry(root, textvariable=var_address ,width=20, font=('Eina01',26),bg="#0096c7").place(x=932,y=295)
            E_Contact = Entry(root, textvariable=var_mobile , width=20, font=('Eina01',26),bg="#0077b6").place(x=932,y=338)
            E_StayDuration = Entry(root, textvariable=var_stay_duration , width=20, font=('Eina01',26),bg="#0077b6").place(x=932,y=423)
            E_Room_type = Entry(root,textvariable=var_room_type, width=21 ,font=('Eina01',24),bg="#0096c7").place(x=932,y=467)


            #Buttons for receipt
            def getreceipt():
                messagebox.showinfo("Success","Receipt has been sent to your mail ID",parent=root)
            def printreceipt():
                messagebox.showerror("Error","Connect your Printer",parent=root)

            makeReceipt = Button(root, text="Get Receipt", bg="#00043a", fg="#e3f2fd", padx=35 ,  font=('Eina01',24), borderwidth=0, command=getreceipt).place(x=670,y=650)

            printReceipt = Button(root, text="Print Receipt", bg="#00043a", fg="#e3f2fd", padx=35 ,  font=('Eina01',24), borderwidth=0, command=printreceipt).place(x=1040,y=650)

            conn.commit()
            conn.close() 


        #function for Services

        def services():
            
            Label3 = Label(root, bg="#ebf8ff", padx=350  , pady=290  ).place(x=650 ,y=130)
            Frame3 = Frame(root, bg="#ebf8ff", padx=350  , pady=300  ).place(x=650 ,y=125)

            #Services confirmation
            def serviceconfirmation():
                messagebox.showinfo("Request Success","Marked services are on the way.",parent=root)


            #Checkboxes for services
            C_RoomService = Checkbutton(root, text="Request Room Service", font=('Helvatica',20), onvalue=1, offvalue=0, bg="#0077b6").place(x=670,y=170)
            C_WifiServicee = Checkbutton(root, text="Request Wifi Service",  font=('Helvatica',20),onvalue=1, offvalue=0, bg="#0096c7").place(x=670,y=215)
            C_ElectricityIssue = Checkbutton(root, text="Request Electricity Issue Service", font=('Helvatica',20), onvalue=1, offvalue=0,bg="#0077b6").place(x=670,y=260)
            C_HouseKeeping = Checkbutton(root, text="Request House Keeping",  font=('Helvatica',20), onvalue=1, offvalue=0, bg="#0096c7").place(x=670,y=305)
            C_Misc = Checkbutton(root, text="Request Miscellaneous Service", font=('Helvatica',20), onvalue=1, offvalue=0, bg="#0077b6").place(x=670,y=350)


            




            

            Request_service = Button(root, text="Request Service", bg="#00043a", fg="#e3f2fd", padx=35 ,  font=('Eina01',24), borderwidth=0, command=serviceconfirmation ).place(x=670,y=650)
          
        #function for complaints

        def complaints():
            
            Label3 = Label(root, bg="#ebf8ff", padx=350  , pady=290  ).place(x=650 ,y=130)
            Frame3 = LabelFrame(root, bg="#ebf8ff", padx=350  , pady=300  ).place(x=650 ,y=125)

            L_complaint = Label(root, text="Write your complaint below",  font=('Eina01',26), bg="#0077b6", fg="#e3f2fd").place(x=670,y=170)

            textbox = Text(root, width=50, height=15,bg='#0096c7', font=('Helvatica',16)).place(x=670 ,y=225)

            def submitComplaint():
                
                messagebox.showinfo("Done","Your complaind is submitted",parent=root)



            Submit = Button(root, text="Submit", bg="#00043a", fg="#e3f2fd", padx=35 ,  font=('Eina01',24), borderwidth=0, command=submitComplaint ).place(x=670,y=650)

            

        #feedback page

        def feedback():
            
            Label3 = Label(root, bg="#ebf8ff", padx=350  , pady=290  ).place(x=650 ,y=130)
            Frame3 = LabelFrame(root, bg="#ebf8ff", padx=350  , pady=300  ).place(x=650 ,y=125)

            L_feedback = Label(root, text="Please give your valuble Feedback", font=('Eina01',26), bg="#0077b6", fg="#e3f2fd").place(x=670,y=170)

            textboxf = Text(root, width=50, height=15,bg='#0096c7', font=('Helvatica',16)).place(x=670 ,y=225)
            def submitFeedback():
                
                messagebox.showinfo("Done","Thank you for submitting your Feedback",parent=root)


            Submitf = Button(root, text="Submit", bg="#00043a", fg="#e3f2fd", padx=35 ,  font=('Eina01',24), borderwidth=0, command=submitFeedback ).place(x=670,y=650)







        

        def reset():
            my_label.config(text="")
            var_name.set(""),
            var_checkin_date.set(""),
            var_stay_duration.set(""),
            var_room_type.set(""),
            var_Identity_Proof.set(""),
            var_address.set(""),
            var_idNo.set("")
            var_mobile.set(""),
            var_email.set(""),
            var_gender.set(""),
            

            x=random.randint(100000,999999)
            var_ref.set(str(x))

        #buttons

        RoomBooking = Button(root, text="Booking",bg="#00043a", fg="#e3f2fd", padx=121 ,  font=('Eina01',24), borderwidth=0, command=roomBooking).place(x=83 ,y=150)
        Receipt = Button(root, text="Receipt",bg="#00043a", fg="#e3f2fd",padx=124, font=('Eina01',24), borderwidth=0,command=receipt).place(x=83 ,y=250)
        meals_Refreshments = Button(root, text="Meals and Refreshments",bg="#00043a", fg="#e3f2fd", font=('Eina01',24), borderwidth=0, command=meals).place(x=83 ,y=350)
        Services = Button(root, text="Services",bg="#00043a", fg="#e3f2fd",padx=118, font=('Eina01',24), borderwidth=0, command=services).place(x=83 ,y=450)
        Complaints = Button(root, text="Complaints",bg="#00043a", fg="#e3f2fd",padx=99, font=('Eina01',24), borderwidth=0, command=complaints).place(x=83 ,y=550)
        Feedback = Button(root, text="Feedback",bg="#00043a", fg="#e3f2fd",padx=109, font=('Eina01',24), borderwidth=0, command=feedback).place(x=83 ,y=650)

        mainmenu = Button(root, text="Main Menu",bg="#00043a", fg="#e3f2fd", font=('Eina01',24), borderwidth=0,command=roomBooking).place(x=650 ,y=51)

        newsession = Button(root, text="New Session",bg="#00043a", fg="#e3f2fd",command=reset,  font=('Eina01',24), borderwidth=0).place(x=925 ,y=51)

        
        def logOut():
            root.destroy()
        logout = Button(root, text="Logout",bg="#00043a", fg="#e3f2fd",command=logOut,  font=('Eina01',24), borderwidth=0).place(x=1233 ,y=51)


        



if __name__ == "__main__":
    root=Tk()
    obj=Mainpage(root)
    root.mainloop()