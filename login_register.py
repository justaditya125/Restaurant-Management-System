from tkinter import *
import tkinter
from tkinter import messagebox


def main():
    root=Tk()
    ob=window1(root)


class window1:
    def __init__(self,root):
        Canvas(root)
        filename = PhotoImage(file = "bg/loginregister.png")
        background_label = Label(image=filename)
        background_label.place(relwidth=1, relheight=1)
        self.root=root
        self.root.title("Login/Register ")
        self.root.geometry("1350x700+0+0")
        Label(root,text="Login/Register",bd=10,relief=GROOVE,font=("comic sans MS",40,'italic'),bg='blue',fg='white').pack(side=TOP,fill=X)
     
        
    
        
   

    #------------------------------------------------------------------buttons--------------------------------------------------------------------------------#
        

        Registerbtn=Button(root,text="Register",width=10,command=self.register,bg="yellow",fg="black",font=("comic sans ms",12)).place(x=400,y=300)
        Loginbtn=Button(root,text="Login",width=10,command=self.Login,bg="yellow",fg="black",font=("comic sans ms",12)).place(x=600,y=300)
        Exitbtn=Button(root,text="Exit",width=10,command=self.Exit1,bg="yellow",fg="black",font=("comic sans ms",12)).place(x=800,y=300)
        root.mainloop()
        

    #--------------------------------------functions----------------------------------#        
    def Exit1(self):
        e=tkinter.messagebox.askyesno("Login Page","Do you want to exit?")
        if e=='yes':
            self.root.destroy()
        else:
            return

    def Login(self):
        self.root.destroy()
        import login #opens login page
        

    def register(self):
        self.root.destroy()
        import register #opens register page

main()