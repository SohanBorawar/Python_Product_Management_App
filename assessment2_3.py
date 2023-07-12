from tkinter import *
import tkinter as tk
import tkinter as ttk
from tkinter import messagebox as msg,ttk
import mysql.connector
import datetime as dt


font_style1 = ("Times New Roman",20)
font_style2 = ("Times New Roman",15)
font_stylebtn = ("Times New Roman",12)


def Database():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        database="product_managment_system",
        )


print(Database())



class Application(tk.Tk):

    def __init__(self) -> None:
        super().__init__()
        self.title("Product Managment Application")
        self.geometry("500x500")
        self.resizable(width=False,height=False)

        self.Database = Database()

        self.create_widgets()

    def create_widgets(self):
        self.clear_widgets()

        self.header = tk.Label(self,text="Welcome To Universal Store",font=font_style1)
        self.header.place(x=50,y=50)

        self.Regist = tk.Label(self,text="For Registration Click >",font=font_style2)
        self.Regist.place(x=50,y=150)
        self.register_btn = tk.Button(self,text="Registration",font=font_style2,command=self.Registration)
        self.register_btn.place(x=260,y=145)

        self.login = tk.Label(self,text="For Login Click >",font=font_style2)
        self.login.place(x=50,y=220)
        self.login_btn = tk.Button(self,text="Login",font=font_style2,command=self.Login)
        self.login_btn.place(x=260,y=215)

        self.exit = tk.Label(self,text="For Exit Click >",font=font_style2)
        self.exit.place(x=50,y=290)
        self.exit_btn = tk.Button(self,text="Exit",font=font_style2,command=self.exit)
        self.exit_btn.place(x=260,y=285)

    def Registration(self):
        self.clear_widgets()

        self.gender = tk.StringVar()

        self.frame1 = tk.Frame(master=self,height=30,bg="orange")
        self.frame1.pack(fill=X)
        self.regheader = tk.Label(master=self.frame1,text="Please Enter Below Details",bg="orange",fg="white")
        self.regheader.pack()


        self.l_name = tk.Label(self,text="Name *",font=font_style2)
        self.l_name.place(x=50,y=50)

        self.l_contact = tk.Label(self,text="Contact *",font=font_style2)
        self.l_contact.place(x=50,y=100)

        self.l_email = tk.Label(self,text="Email *",font=font_style2)
        self.l_email.place(x=50,y=150)

        self.l_gender = tk.Label(self,text="Gender *",font=font_style2)
        self.l_gender.place(x=50,y=200)

        self.l_city = tk.Label(self,text="City *",font=font_style2)
        self.l_city.place(x=50,y=250)

        self.l_state = tk.Label(self,text="State *",font=font_style2)
        self.l_state.place(x=50,y=300)

        self.l_role = tk.Label(self,text="Role",font = font_style2)
        self.l_role.place(x=50,y=350)

        self.l_password = tk.Label(self,text="Password *",font= font_style2)
        self.l_password.place(x=50,y=400)

#*******************************Entry Part*************************************

        self.e_name = tk.Entry(self,font= font_style2)
        self.e_name.place(x=160,y=50)

        self.e_contact = tk.Entry(self,font=font_style2)
        self.e_contact.place(x=160,y=100)

        self.e_email = tk.Entry(self,font=font_style2)
        self.e_email.place(x=160,y=150)

        self.male_radio = tk.Radiobutton(self, text="Male", variable=self.gender, value="Male",font=font_style2)
        self.male_radio.place(x=160,y=200)

        self.female_radio = tk.Radiobutton(self, text="Female", variable=self.gender, value="Female",font=font_style2)
        self.female_radio.place(x=250,y=200)

        self.city_sel =  ttk.Combobox(self,value=["ahmedabad","vadodra","gandhinagar"],font=font_style2)
        self.city_sel.place(x=160,y=250)

        self.state_sel = ttk.Combobox(self,value=["Gujarat","Delhi","Rajasthan","Banglore"],font=font_style2)
        self.state_sel.place(x=160,y=300)

        self.e_role = ttk.Combobox(self,values=["Manager","Consumer"],font=font_style2)
        self.e_role.place(x=160,y=350)

        self.e_password = tk.Entry(self,show="*",font=font_style2)
        self.e_password.place(x=160,y=400)

#*********************************** Button Part ******************************************

        self.b_submit = tk.Button(self,text="Submit",width="10",height="2",bg="orange",fg="black",command=self.submit)
        self.b_submit.place(x=130,y=450)

        self.b_back = tk.Button(self,text="Back",width="10",height="2",bg="orange",fg="black",command=self.create_widgets)
        self.b_back.place(x=250,y=450)

#********************************** Submit Part *****************************************************

    def submit(self):
        conn = Database()
        cursor = conn.cursor()
        query = "select * from stock where Product"

        if self.e_name.get()=="" or self.e_contact.get()=="" or self.e_email.get()=="" or self.city_sel.get()=="" or self.state_sel.get()=="" or self.e_password.get()=="" or self.e_role.get()=="":
            msg.showinfo("Registration Status","All Fields Are Mandatory")
        elif self.gender.get()=="":
            msg.showinfo("Registration Status","All Fields Are Mandatory")
        else :
            conn = Database()
            cursor = conn.cursor()
            query ="insert into user(Name,Contact,Email,Gender,City,State,Role,Password) values(%s,%s,%s,%s,%s,%s,%s,%s)" 
            args = (self.e_name.get(),self.e_contact.get(),self.e_email.get(),self.gender.get(),self.city_sel.get(),self.state_sel.get(),self.e_role.get(),self.e_password.get() )
            cursor.execute(query,args)
            conn.commit()
            conn.close()

            msg.showinfo("Registration Status","Registered Successfully")

            self.e_name.delete(0,"end")
            self.e_contact.delete(0,"end")
            self.e_email.delete(0,"end")
            self.e_password.delete(0,"end")
            self.clear_widgets()
            self.create_widgets()

#************************************* Login Part ************************************************

    def Login(self):
        self.clear_widgets()

        self.log_frame = Frame(self,bg="orange",height=150)
        self.log_frame.pack(fill=X)
        self.l_log_header = Label(self.log_frame,text="Hello, Login To Proced",font=font_style2,bg="orange")
        self.l_log_header.pack()

        self.log_email = Label(self,text="Email",font=font_style2)
        self.log_email.place(x= 100,y=100)

        self.log_password = Label(self,text="password",font=font_style2)
        self.log_password.place(x=100,y=200)

        self.e_log_email = Entry(self,font=font_style2)
        self.e_log_email.place(x=200,y=100)

        self.e_log_password = Entry(self,font=font_style2)
        self.e_log_password.place(x=200,y=200)

        self.b_login = Button(self,text="Login",width="10",command=self.click_login,font=font_stylebtn)
        self.b_login.place(x=150,y=270)

    def click_login(self):

        if self.e_log_email.get()=="" or self.e_log_password.get()=="" :
            msg.showinfo("Login Status","All Fields Are Mandatory")

        else:
            conn = Database()
            cursor = conn.cursor()
            query ="select * from user where Email=%s and Password=%s" 
            args = (self.e_log_email.get(),self.e_log_password.get())
            cursor.execute(query,args)
            self.result = cursor.fetchall()
            print(self.result)
            if self.result:
                for i in self.result :
                    self.loged_data = i
                    role = i[6]
                    print(role)
                if role == "Manager":
                    msg.showinfo("Login Status","Login Successfully")
                    self.product_manager_page()
                    
                elif role == "Consumer":
                    msg.showinfo("Login Status","Login Successfully")
                    self.customer_page()
                    
                else:
                    msg.showinfo("Login Status","Entered Email & Password Not Found")
            else:
                msg.showinfo("Login Status","Entered Email & Password Not Found")

            conn.close()


#*****************************************Manager's Pages**************************************************************

    def product_manager_page(self):
        self.clear_widgets()

        self.l_manager = tk.Label(self,text="Product Manager Page \n\nHello Manager \nHere's What You Can Do",font=font_style1)
        self.l_manager.place(x=100,y=50) 

        self.manager_mstock_btn = tk.Button(self,text="Manage Stocks",font=font_stylebtn,command=self.manage_stock)
        self.manager_mstock_btn.place(x=100,y=200)

        self.manager_vstock_btn = tk.Button(self,text="View Stock",font=font_stylebtn,command=self.view_stock)
        self.manager_vstock_btn.place(x=250,y=200)

        self.b_back = tk.Button(self,text="Back",width="10",height="2",bg="orange",fg="black",command=self.create_widgets)
        self.b_back.place(x=180,y=300)

    def manage_stock(self):
        self.clear_widgets()

        self.l_manage_stock = tk.Label(self,text="Manage Stocks",font=font_style1)
        self.l_manage_stock.place(x=50,y=50) 

        self.l_product_name = tk.Label(self,text="Product Name",font=(30))
        self.l_product_name.place(x=100,y=100)

        self.l_product_qty = tk.Label(self,text="Quantity",font=(30))
        self.l_product_qty.place(x=100,y=150)

        self.l_product_price = tk.Label(self,text="Price",font=(30))
        self.l_product_price.place(x=100,y=200)

        self.e_product_name = tk.Entry(self,font=font_style2)
        self.e_product_name.place(x=220,y=100)

        self.e_product_qty = tk.Entry(self,font=font_style2)
        self.e_product_qty.place(x=220,y=150)
        
        self.e_product_price = tk.Entry(self,font=font_style2)
        self.e_product_price.place(x=220,y=200)

        self.insert_product_btn = tk.Button(self,text="Insert",font=font_stylebtn,command=self.insert_data)
        self.insert_product_btn.place(x=100,y=250)

        self.search_product_btn = tk.Button(self,text="Search",font=font_stylebtn,command=self.search_data)
        self.search_product_btn.place(x=250,y=250)

        self.update_product_btn = tk.Button(self,text="Update",font=font_stylebtn,command=self.update_data)
        self.update_product_btn.place(x=100,y=300)

        self.delete_product_btn = tk.Button(self,text="Delete",font=font_stylebtn,command=self.delete_data)
        self.delete_product_btn.place(x=250,y=300)

        self.b_back = tk.Button(self,text="Back",width="10",height="2",bg="orange",fg="black",command=self.product_manager_page)
        self.b_back.place(x=200,y=400)

    def insert_data(self):

            if self.e_product_name.get()=="" or self.e_product_qty.get=="" or self.e_product_price.get()=="" :
                 msg.showinfo("Insert Status","All Fields Are Mandatory")

            else :
                conn = Database()
                cursor = conn.cursor()
                query = "insert into product(Product_name,Qty,Price) value(%s,%s,%s)"
                args = (self.e_product_name.get(),self.e_product_qty.get(),self.e_product_price.get())
                cursor.execute(query,args)
                conn.commit()
                conn.close()

                msg.showinfo("Insert Status","Data Inserted Successfully")

                self.e_product_name.delete(0,"end")
                self.e_product_qty.delete(0,"end")
                self.e_product_price.delete(0,"end")

    def search_data(self):
         
         if self.e_product_name.get()=="":
              msg.showinfo("Search Status","Product Name Is Mandatory")
         else :
              conn = Database()
              cursor = conn.cursor()
              query = "select * from product where Product_name = %s"
              args = (self.e_product_name.get(),)
              cursor.execute(query,args)
              self.row = cursor.fetchall()

              for i in self.row:
                   self.e_product_qty.insert(0,i[1])
                   self.e_product_price.insert(0,i[2])
              else:
                   msg.showinfo("Search Status","Id Not Found") 

    def update_data(self):
         
         if self.e_product_name.get()=="" or self.e_product_qty.get()=="" or self.e_product_price.get()=="" :
              msg.showinfo("Update Status","ALl Fields Are Mandatory")
         else:
              conn = Database()
              cursor = conn.cursor()
              query = "update product set Qty=%s Price=%s where Product_name=%s"
              args = (self.e_product_qty.get(),self.e_product_price.get(),self.e_product_name.get())
              cursor.execute(query,args)  
              conn.commit()
              conn.close()

              msg.showinfo("Update Status","Stock Updated Successfully")

              self.e_product_name.delete(0,"end")
              self.e_product_qty.delete(0,"end")
              self.e_product_price.delete(0,"end")

    def delete_data(self):

         if self.e_product_name.get()=="":
              msg.showinfo("Delete Status","Product Name Is Compulsory")
         else:
              conn = Database()
              cursor = conn.cursor()
              query = "delete from stocks where Product_name=%s"
              args = (self.e_product_name.get(),)
              cursor.execute(query,args)  
              conn.commit()
              conn.close()

              msg.showinfo("Delete Status","Product Deleted Successfully")

              self.e_product_name.delete(0,"end")

     
    def view_stock(self):
        self.clear_widgets()

        self.l_view_stock = tk.Label(self,text="Here You Can View Stocks",font=font_style1)
        self.l_view_stock.place(x=50,y=50)

        conn = Database()
        cursor = conn.cursor()
        query = "select * from stocks"
        args = None
        cursor.execute(query,args)
        self.row = cursor.fetchall()
        print(self.row)

        for i in self.row:
             self.view_product_name = tk.Label(self,text=f"Product : {i[0]}",font=font_style2)
             self.view_product_name.place(x=50,y=100)

             self.view_product_qty = tk.Label(self,text=f"Qty : {i[1]}",font=font_style2)
             self.view_product_qty.place(x=50,y=150)

             self.view_product_price = tk.Label(self,text=f"Price : {i[2]}",font=font_style2)
             self.view_product_price.place(x=50,y=200)


#*****************************************Customer's Page*************************************************


    def customer_page(self):

        self.clear_widgets()

        self.l_customer = tk.Label(self,text=f"Customer Page \n\nHello {self.loged_data[0]} \nHere's What You Can Do",font=font_style1)
        self.l_customer.place(x=100,y=50)

        self.customer_pstock_btn = tk.Button(self,text="Purchase Stocks",font=font_stylebtn,command=self.purchase_stock)
        self.customer_pstock_btn.place(x=100,y=200)

        self.customer_vorder_btn = tk.Button(self,text="View Order",font=font_stylebtn,command=self.view_order)
        self.customer_vorder_btn.place(x=250,y=200)

        self.b_back = tk.Button(self,text="Back",width="10",height="2",bg="orange",fg="black",command=self.create_widgets)
        self.b_back.place(x=180,y=300)

    def purchase_stock(self):
        self.clear_widgets()

        self.l_purchase_stock = tk.Label(self,text=f"{self.loged_data[0]} purchase Stocks",font=font_style1)
        self.l_purchase_stock.place(x=50,y=50) 

        self.l_purchase_product_name = tk.Label(self,text="Product Name",font=font_style2)
        self.l_purchase_product_name.place(x=100,y=100)

        self.l_purchase_product_qty = tk.Label(self,text="Quantity",font=font_style2)
        self.l_purchase_product_qty.place(x=100,y=150)

        self.e_purchase_product_name = tk.Entry(self,font=font_style2)
        self.e_purchase_product_name.place(x=220,y=100)

        self.e_purchase_product_qty = tk.Entry(self,font=font_style2)
        self.e_purchase_product_qty.place(x=220,y=150)
    
        self.insert_purchase_product_btn = tk.Button(self,text="Purchase Item",font=font_stylebtn,command=self.onclick_purchase)
        self.insert_purchase_product_btn.place(x=170,y=200)
   
        self.b_back = tk.Button(self,text="Back",width="10",height="2",bg="orange",fg="black",command=self.customer_page)
        self.b_back.place(x=180,y=300)


    def onclick_purchase(self):
        if self.e_purchase_product_name.get()=="" or self.e_purchase_product_qty.get()=="" :
            msg.showinfo("Purchase Status","All Fields Are Mandatory To Purchase")
        else :
            conn = Database()
            cursor = conn.cursor()
            query ="select * from stocks where Product_name=%s" 
            args = (self.e_purchase_product_name.get(),)
            cursor.execute(query,args)
            self.product_list = cursor.fetchall()

            for i in self.product_list:
                self.stock_price = i[2]
                self.stock_qty = i[1]

            self.total_price = self.stock_price * int(self.e_purchase_product_qty.get())

            self.new_stock = self.stock_qty - int(self.e_purchase_product_qty.get())

            conn = Database()
            cursor = conn.cursor()
            query = "insert into orders(Product_name,Purchased_qty,Total_price,Order_date,consumer_email) value(%s,%s,%s,%s,%s)"
            args = (self.e_purchase_product_name.get(),self.e_purchase_product_qty.get(),self.total_price,dt.datetime.now(),self.loged_data[2])
            cursor.execute(query,args)
            conn.commit()
            conn.close()

            msg.showinfo("Purchase Status","Order Purchased Successfully")


            conn = Database()
            cursor = conn.cursor()
            query = "update stocks set Qty = %s where Product_name = %s "
            args = (self.new_stock,self.e_purchase_product_name.get())
            cursor.execute(query,args)
            conn.commit()
            conn.close()

    def view_order(self):
        self.clear_widgets()
        
        conn = Database()
        cursor = conn.cursor()
        query ="select * from orders where Consumer_email = %s" 
        args = (self.loged_data[2],)
        cursor.execute(query,args)
        self.order_list = cursor.fetchall(
        )
      #  self.orders_listbox = tk.Listbox(self)
      #  self.orders_listbox.place(x=50,y=100)

        
        for i in self.order_list:
            self.cus_ordered_Product_id = tk.Label(self,text=f"Order Id : {i[0]}")
            self.cus_ordered_Product_id.place(x=50,y=100)

            self.cus_ordered_Product_name = tk.Label(self,text=f"Product Name : {i[1]}")
            self.cus_ordered_Product_name.place(x=50,y=150)

            

    def clear_widgets(self):
        for widget in self.winfo_children():
            widget.destroy()

    def exit(self):
        self.database.close()
        self.destroy()





if __name__ == "__main__":
    app = Application()
    app.mainloop()
