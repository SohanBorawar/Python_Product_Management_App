from tkinter import *
import tkinter as tk
import tkinter as ttk
from tkinter import messagebox as msg,ttk
import mysql.connector


def Database():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        database="product_managment_system",
        )






class Application(tk.Tk):

    def __init__(self) -> None:
        super().__init__()
        self.title("Product Managment Application")
        self.geometry("500x500")

        self.Database = Database()

        self.create_widgets()

    def create_widgets(self):

        self.header = tk.Label(self,text="Welcome To Universal Store",font="30")
        self.header.place(x=50,y=100)

        self.Regist = tk.Label(self,text="For Registration Click >",font="30")
        self.Regist.place(x=50,y=150)
        self.register_btn = tk.Button(self,text="Registration",font="30",command=self.Registration())
        self.register_btn.place(x=100,y=150)

        self.login = tk.Label(self,text="For Login Click >",font="30")
        self.login.place(x=50,y=200)
        self.login_btn = tk.Button(self,text="Login",font="30",command=self.Login)
        self.login_btn.place(x=100,y=200)

        self.exit = tk.Label(self,text="For Exit Click >",font="30")
        self.exit.place(x=50,y=250)
        self.exit_btn = tk.Button(self,text="Exit",font="30",command=self.exit)
        self.exit_btn.place(x=100,y=250)

    def Registration(self):
        self.clear_widgets()

        self.gender = tk.StringVar()

        self.frame1 = tk.Frame(master=self,height=30,bg="orange")
        self.frame1.pack(fill=X)
        self.regheader = tk.Label(master=self.frame1,text="Please Enter Below Details",bg="orange",fg="white")
        self.regheader.pack()


        self.l_name = tk.Label(self,text="Name *",font="10")
        self.l_name.place(x=50,y=50)

        self.l_contact = tk.Label(self,text="Contact *",font="10")
        self.l_contact.place(x=50,y=100)

        self.l_email = tk.Label(self,text="Email *",font="10")
        self.l_email.place(x=50,y=150)

        self.l_gender = tk.Label(self,text="Gender *",font="10")
        self.l_gender.place(x=50,y=200)

        self.l_city = tk.Label(self,text="City *",font="10")
        self.l_city.place(x=50,y=250)

        self.l_state = tk.Label(self,text="State *",font="10")
        self.l_state.place(x=50,y=300)

        self.l_role = tk.Label(self,text="Role",font="30")
        self.l_role.place(x=50,y=350)

        self.l_password = tk.Label(self,text="Password *",font="30")
        self.l_password.place(x=50,y=400)

#*******************************Entry Part*************************************

        self.e_name = tk.Entry(self,font="10")
        self.e_name.place(x=130,y=50)

        self.e_contact = tk.Entry(self,font="10")
        self.e_contact.place(x=130,y=100)

        self.e_email = tk.Entry(self,font="10")
        self.e_email.place(x=130,y=150)

        self.male_radio = tk.Radiobutton(self, text="Male", variable=self.gender, value="Male",font="1")
        self.male_radio.place(x=130,y=200)

        self.female_radio = tk.Radiobutton(self, text="Female", variable=self.gender, value="Female",font="1")
        self.female_radio.place(x=200,y=200)

        self.city_sel =  ttk.Combobox(self,value=["ahmedabad","vadodra","gandhinagar"],font="10")
        self.city_sel.place(x=130,y=250)

        self.state_sel = ttk.Combobox(self,value=["Gujarat","Delhi","Rajasthan","Banglore"],font="10")
        self.state_sel.place(x=130,y=300)

        self.e_role = ttk.Combobox(self,values=["Manager","Consumer"])
        self.e_role.place(x=130,y=350)

        self.e_password = tk.Entry(self,show="*",font="30")
        self.e_password.place(x=130,y=400)

#*********************************** Button Part ******************************************

        self.b_submit = tk.Button(self,text="Submit",width="10",height="2",bg="orange",fg="black")
        self.b_submit.place(x=130,y=450)

        self.b_back = tk.Button(self,text="Back",width="10",height="2",bg="orange",fg="black")
        self.b_back.place(x=130,y=500)


    def submit(self):

        if self.e_name.get()=="" or self.e_contact.get()=="" or self.e_email.get()=="" or self.city_sel.get()=="" or self.state_sel.get()=="" or self.e_password.get()=="" or self.e_role.get()=="":
            msg.showinfo("Registration Status","All Fields Are Mandatory")
        elif self.gender.get()=="":
            msg.showinfo("Registration Status","All Fields Are Mandatory")
        else :
            conn = Da()
            cursor = conn.cursor()
            query ="" 
            args = ()
            cursor.execute(query,args)
            conn.commit()
            conn.close()

            msg.showinfo("Registration Status","Registered Successfully")

            self.e_name.delete(0,"end")
            self.e_contact.delete(0,"end")
            self.e_email.delete(0,"end")
            self.e_password.delete(0,"end")

    def Login(self):
        self.clear_widgets()

        self.log_frame = Frame(self,bg="orange",height="100")
        self.log_frame.pack(fill=X)
        self.l_log_header = Label(self.log_frame,text="Hello, Login To Proced",font="30",bg="orange")
        self.l_log_header.pack()

        self.log_email = Label(self,text="Email",font="30")
        self.log_email.place(x=50,y=50)

        self.log_password = Label(self,text="password",font="30")
        self.log_password.place(x=50,y=100)

        self.e_log_email = Entry(self,font="30")
        self.e_log_email.place(x=140,y=50)

        self.e_log_password = Entry(self,font="30")
        self.e_log_password.place(x=140,y=100)

        self.b_login = Button(self,text="Login",width="10")
        self.b_login.place(x=120,y=170)

    def click_login(self):

        if self.e_log_email.get()=="" or self.e_log_password.get()=="" :
            msg.showinfo("Login Status","All Fields Are Mandatory")
        elif self.e_log_email == self.e_email and self.e_log_password == self.e_password :
            conn = Database()
            cursor = conn.cursor()
            query ="" 
            args = ()
            cursor.execute(query,args)
            conn.commit()
            conn.close()

            msg.showinfo("Registration Status","Registered Successfully")

            self.e_name.delete(0,"end")
            self.e_contact.delete(0,"end")
            self.e_email.delete(0,"end")
            self.e_password.delete(0,"end")

        else :
            msg.showinfo("Login Status","Entered Email And Password Are not Registered")



    def clear_widgets(self):
        for widget in self.winfo_children():
            widget.destroy()

    def exit(self):
        self.database.close()
        self.destroy()



if __name__ == "__main__":
    app = Application()
    app.mainloop()
