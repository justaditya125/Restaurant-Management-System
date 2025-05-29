from tkinter import *
import tkinter 
from tkinter import ttk
import mysql.connector
from tkinter import messagebox

def getConnection():
    con=mysql.connector.connect(host="localhost",user="root",password="12345",database='Restaurant')
    cursor=con.cursor()
    return cursor

def main():
    root=Tk()
    ob=regestration(root)
class regestration:
    def __init__(self,root):
        self.root=root
        self.root.title("Registration")

#----------------------------------------------------------------------------Variables----------------------------------------------------#
         
        self.Username=StringVar()
        self.Password=StringVar()
        self.Account_type=StringVar()
        self.confirm_User=StringVar()
        self.confirm_Pass=StringVar()


 #--------------------------------------------------------------BackGround-------------------------------------------------------------------------------------------#
        
        self.root.geometry("1350x700+0+0")
        Canvas(root, bg="black", height=250, width=300)
        filename = PhotoImage(file = "bg/register.png")
        background_label = Label(image=filename)
        background_label.place(relwidth=1, relheight=1)
        Label(self.root,text="Registration ", font=('comic sans MS',40,'italic'),bg='light green',fg='white',bd=10).place(x=0,y=0,relwidth=1)

        
#-----------------------------------------Username----------------------------------------------------------------------------------------------------------------#
        
        lbl_Username=Label(root,text="Username",bg='Black',fg='White',font=("comic sans ms",20,'italic'))
        lbl_Username.place(x=500,y=200)
        txt_Username=Entry(root,textvariable=self.Username,font=("comic sans ms",15,'italic'),bd=5,relief=GROOVE)
        txt_Username.place(x=750,y=200)

        
#--------------------------------------------Password--------------------------------------------------------------------------------------------#
        
        lbl_Password=Label(root,text="Password",bg='black',fg='white',font=("comic sans ms",20,'italic'))
        lbl_Password.place(x=500,y=300)
        txt_Password=Entry(root,textvariable=self.Password,font=("comic sans ms",15,'italic'),bd=5,relief=GROOVE,show="*")
        txt_Password.place(x=750,y=300)

        lbl_con_Password=Label(root,text="Confirm Password",bg='Black',fg='White',font=("comic sans ms",20,'italic'))
        lbl_con_Password.place(x=500,y=400)
        txt_con_Password=Entry(root,textvariable=self.confirm_Pass,font=("comic sans ms",15,'italic'),show="*",bd=5,relief=GROOVE)
        txt_con_Password.place(x=750,y=400)

        lbl_acc_type=Label(root,text="Account Type",bg='Black',fg='White',font=("comic sans ms",20,'italic'))
        lbl_acc_type.place(x=500,y=500)
        combo_acc_type=ttk.Combobox(root,textvariable=self.Account_type,font=("comic sans ms",15,'italic'),state='readonly')
        combo_acc_type['values']=("User","Administrator")
        combo_acc_type.place(x=750,y=500)


#-----------------buttons------------------------------------------------------------------------------------------------------------------------#
        
        
        Confirmbtn=Button(root,text="Confirm",width=10,command=self.confirm,bg='black',fg='white',font=("comic sans ms",12)).place(x=500,y=600)
        exitbtn=Button(root,text="Exit",width=10,command=self.exit2,bg='black',fg='white',font=("comic sans ms",12)).place(x=620,y=600)      
        Clearbtn=Button(root,text="Clear",width=10,command=self.clear,bg='black',fg='white',font=("comic sans ms",12)).place(x=740,y=600)
        Loginbtn=Button(root,text="Login",width=10,command=self.login,bg="black",fg="white",font=("comic sans ms",12)).place(x=860,y=600)
        root.mainloop()


#----------------functions----------------------------------------------------------------------------------------------------------------------------------------------------#

    def clear(self):
        self.Username.set("")
        self.Password.set("")
        self.confirm_User.set("")
        self.confirm_Pass.set("")
        self.Account_type.set("")
        

    def confirm(self):
        if self.Username.get()=="" or self.Password.get()=="" or self.confirm_User=="" or self.confirm_Pass.get()=="" or self.Account_type.get()=="":
           messagebox.showerror("Error","All Fields are required")

        elif self.Password.get()!=self.confirm_Pass.get():
            messagebox.showerror("Error","Password Mismatch")

        elif self.Username.get()==self.Password.get():
            messagebox.showerror("Error","Username & password cannot be same")

            
        else:
            con=mysql.connector.connect(host="localhost",user="root",password="12345",database='Restaurant')
            cursor=con.cursor()
            
            result=cursor.execute("insert into users values(%s,%s,%s)",(self.Username.get(),
                                                                                                        self.Password.get(),
                                                                                                        self.Account_type.get()))
            con.commit()
            self.clear()
            con.close()
            messagebox.showinfo("Succues","You are successfully registered")


    def exit2(self):
        q=tkinter.messagebox.askquestion("Exit Application","Do you want to quit?")
        if q=="yes":
            self.root.destroy()
        else:
            pass

    def login(self):
        self.root.destroy()
        import login #imports login page 
        
        
        
main()


        
