from tkinter import *
import tkinter
import tkinter as tk
from PIL import ImageTk
from tkinter import messagebox
import mysql.connector
from PIL import ImageTk,Image


def main():
    root=Tk()
    ob=manage1(root)
    
class manage1:
    
    def __init__(self,root):
        self.root=root
        self.root.title("Admin page")
        self.root.geometry("1350x700+0+0")
    

        #------------------------------------------------------BackGround-------------------------------------------------------------------------------------------#
        Canvas(root, bg="black", height=250, width=300)
        filename = PhotoImage(file = "bg/admin.png")
        background_label = Label(image=filename)
        background_label.place(relwidth=1, relheight=1)
      
        #--------------------------------------------------------------buttons----------------------------------------------------------------------------#
      
        items_manage=Button(root,text='Manage Items',width=15,command=self.managei,font=('comic sans MS',15,"italic"),bg='white',fg='red').place(x=640,y=100)
        users_manage=Button(root,text='Manage users',width=15,command=self.manageu,font=('comic sans MS',15,"italic"),bg='white',fg='red').place(x=640,y=200)
        chart1_btn=Button(root,text='Price Chart',width=15,command=self.chart1,font=('comic sans MS',15,"italic"),bg='white',fg='red').place(x=640,y=300)
        chart2t_btn=Button(root,text='Order Chart',width=15,command=self.chart2,font=('comic sans MS',15,"italic"),bg='white',fg='red').place(x=640,y=400)
        exit_btn=Button(root,text='Exit',width=15,command=self.exit,font=('comic sans MS',15,"italic"),bg='white',fg='red').place(x=640,y=500)
        root.mainloop()


    #-------------------------------------------------functions-------------------------------------------------------#

    def exit(self):
        q=tkinter.messagebox.askquestion("Exit Application","Do you want to quit?")
        if q=="yes":
            self.root.destroy()
        else:
            return

    def manageu(self):
        self.root.destroy()
        import manage_users
        

    def managei(self):
        self.root.destroy()
        import manage_items

    def chart1(self):
        import Price_Chart

    def chart2(self):
        import order_chart
        


        



main()
