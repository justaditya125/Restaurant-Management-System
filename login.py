from tkinter import *
import tkinter
import tkinter as tk
from PIL import ImageTk,Image
from tkinter import messagebox
import mysql.connector


def main():
    root=Tk()
    ob=login_system(root)
class login_system:
    def __init__(self,root):
        self.root=root
        self.root.title("Login page")
        self.root.geometry("1350x700+0+0")


       

#--------------------------------------------------------Variables-------------------------------------------------------------#
        self.username=StringVar()
        self.password=StringVar()
        
        
#--------------------------------------------------------Frame---------------------------------------------------------------------#
        canvas=Canvas(root, bg="black", height=250, width=300)
        filename = PhotoImage(file = "bg/login.png")
        background_label = Label(image=filename)
        background_label.place(relwidth=1, relheight=1)
        Label(self.root,text="Login",font=("algerian",40,'bold'),bg='green',fg='white',bd=10).place(x=0,y=0,relwidth=1)

     


        lbluser=Label(root,text="Username",font=("bookman old style",20,'bold'),bg="orange",fg='blue',width=10).place(x=500,y=200)
        txtuser=Entry(root,bd=5,textvariable=self.username,font=("comic sans ms",15)).place(x=700,y=200)

        lblpass=Label(root,text="Password",font=("bookman old style",20,'bold'),bg='yellow',fg='red',width=10).place(x=500,y=300)
        txtpass=Entry(root,bd=5,textvariable=self.password,font=("comic sans ms",15),show="*").place(x=700,y=300)

#----------------------------------------------------------Buttons-----------------------------------------------------------------------#

        btn_log=Button(root,text='Login',width=15,command=self.login,font=("comic sans ms",15),bg='white',fg='black').place(x=400,y=400)
        btn_exit=Button(root,text='Exit',width=15,command=self.exit3,font=("comic sans ms",15),bg='red',fg='white').place(x=600,y=400)
        btn_back=Button(root,text='Back',width=15,command=self.back2,font=("comic sans ms",15),bg='white',fg='black').place(x=800,y=400)
        root.mainloop()

 #------------------------------------------------------------Functions-----------------------------------------------------------------------#     

 
    def login(self):
        passwd=self.password.get()
        userid=self.username.get()
       
        
        if userid=="" or passwd=="":
            tkinter.messagebox.showerror("Error","All fields are required")
        

        else:
            passwd=self.password.get()
            userid=self.username.get()
            
   
            con=mysql.connector.connect(host="localhost",user="root",password="12345",database='Restaurant')
            cursor=con.cursor()
            cursor.execute("select Password, Account_Type from users where username='"+userid+"'")
            result=cursor.fetchall()
            loginSuccess = False
            accountType="user"
            for y in result:
                if y[0]==passwd:
                    loginSuccess= True
                    accountType=y[1]
                    

            if loginSuccess==True:
                self.root.destroy()
                if accountType=="Administrator":
                    import manage
                elif accountType=="User":
                    import order_page
                
            else:
                tkinter.messagebox.showerror("Error","User does not exist")

    def exit3(self):
        q=tkinter.messagebox.askquestion("Exit Application","Do you want to quit?")
        if q=="yes":
            self.root.destroy()
        else:
            return

    def back2(self):
        self.root.destroy()
        import login_register
        
       

            
            


main()
        
        



