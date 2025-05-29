from tkinter import *
from tkinter import ttk
import tkinter
import mysql.connector
from tkinter import messagebox


def main():
    root=Tk()
    ob=users(root)

class users:
    def __init__(self,root):
        self.root=root
        self.root.title("User Management")
        self.root.geometry("1350x700+0+0")


 #------------------------------------------------------BackGround-------------------------------------------------------------------------------------------#
        canvas=Canvas(root, bg="black", height=250, width=300)
        filename = PhotoImage(file = "bg/users.png")
        background_label = Label(image=filename)
        background_label.place(relwidth=1, relheight=1)
        Label(self.root,text="Users", font=('comic sans MS',40,'italic'),bg='black',fg='white',bd=10).place(x=0,y=0,relwidth=1)

        #---------------------------------------------------------------------variables----------------------------------#
        self.Username=StringVar()
        self.Account_type=StringVar()
        self.Search_by=StringVar()
        self.Search_txt=StringVar()




        #----------------------------------------------Left-------------------------------------------------------------------------------------------#



        lbl_Username=Label(root,text="Username",bg='Black',fg='White',font=("comic sans MS",20,'italic')).place(x=10,y=120)
        txt_Username=Entry(root,textvariable=self.Username,font=("comic sans MS",15,'italic'),bd=5,relief=GROOVE).place(x=190,y=120)
   

        lbl_Accounttype=Label(root,text="Account Type",bg='Black',fg='White',font=("comic sans MS",18,'italic')).place(x=10,y=190)
        values=('User','Administration')
        combo_Accounttype=ttk.Combobox(root,textvariable=self.Account_type,font=("comic sans MS",15,'italic'),state='readonly',values=values).place(x=190,y=190)

        #-------------------------------------------------------------buttons-------------------------------------------------------------#

        
        Updatebtn=Button(root,text="Update",width=10,command=self.update,font=("comic sans MS",10,'italic'),bg="black",fg="white").place(x=30,y=400)
        Deletebtn=Button(root,text="Delete",width=10,command=self.delete,font=("comic sans MS",10,'italic'),bg="black",fg="white").place(x=140,y=400)
        Itemsbtn=Button(root,text="Manage Items",width=11,command=self.manage_items,font=("comic sans MS",10,'italic'),bg="black",fg="white").place(x=240,y=400)   
        Exitbtn=Button(root,text="Exit",width=10,command=self.exit,font=("comic sans MS",10,'italic'),bg="black",fg="white").place(x=345,y=400)
     #-----------------------------------------------Right-------------------------------------------------#
      

        lbl_Search=Label(root,text="Search By",bg='Black',fg='White',font=("comic sans MS",18,'italic')).place(x=500,y=120)
        values1=('Username','Account Type')
        combo_Search=ttk.Combobox(root,textvariable=self.Search_by,width=15,font=("comic sans MS",13,'italic'),state='readonly',values=values1).place(x=650,y=120)
        txt_Search=Entry(root,textvariable=self.Search_txt,width=20,font=("comic sans MS",13,'italic'),bd=5,relief=GROOVE).place(x=850,y=120)
        Searchbtn=Button(root,command=self.Search_users,text="Search",width=10,pady=5,font=("comic sans MS",10,'italic')).place(x=1080,y=120)
        Shwoallbtn=Button(root,text="Show All",command=self.fetch_data,width=10,pady=5,font=("comic sans MS",10,'italic')).place(x=1180,y=120)




        #--------------------------------------------------------------Frame------------------------------------------------------------------------#

        Table_Frame=Frame(root,bd=4,relief=RIDGE)
        Table_Frame.place(x=500,y=180,width=760,height=500)

        style=ttk.Style()
        style.configure("Treeview",
                        background="white",
                        foreground="black",
                        rowheight=25,
                        fieldbackground="white")
        style.map("Treeview",
                  background=[('selected','blue')])
        self.Restaurant_table=ttk.Treeview(Table_Frame,columns=('Username','Account Type'))
        self.Restaurant_table.heading('Username',text='Username')
        self.Restaurant_table.heading('Account Type',text='Account Type')
        self.Restaurant_table['show']='headings'
        self.Restaurant_table.column('Username', width=100, anchor='center')
        self.Restaurant_table.column('Account Type', width=100, anchor='center')
        self.Restaurant_table.pack(fill=BOTH,expand=1)
        self.Restaurant_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
        root.mainloop()

#---------------------------------------------------------Functions-------------------------------------------------------------------------------------#

    def get_cursor(self,ev):
        cursor_row=self.Restaurant_table.focus()
        contents=self.Restaurant_table.item(cursor_row)
        row=contents['values']
        self.Username.set(row[0])
        self.Account_type.set(row[1])

    
    def fetch_data(self):
        self.Search_by.set("")
        self.Search_txt.set("")
        self.Restaurant_table.tag_configure('odd',background='yellow')
        self.Restaurant_table.tag_configure('even',background='red')
        
        con=mysql.connector.connect(host="localhost",user="root",password="12345",database='Restaurant')
        cursor=con.cursor()
        cursor.execute("select  Username,Account_type from users")
        rows=cursor.fetchall()
        if len(rows)!=0:
            self.Restaurant_table.delete(*self.Restaurant_table.get_children())
            count=0
            for rows in rows:
                if count % 2==0:
                    self.Restaurant_table.insert('',END,values=rows,tags=('even',))
                else:
                    self.Restaurant_table.insert('',END,values=rows,tags=('odd',))
                count+=1
            con.commit()
        con.close()
    


    def clear(self):
        self.Username.set("")
        self.Account_type.set("")


    def update(self):
        if self.Username.get()=="" or self.Account_type.get()=="":
            messagebox.showerror("Error","Please select account")
        else:
            con=mysql.connector.connect(host="localhost",user="root",password="12345",database='Restaurant')
            cursor=con.cursor()
            cursor.execute("update Users set  Account_Type=%s where password=%s ",(self.Account_type.get(),
                                                                                                    self.Username.get()))
            con.commit()
            self.fetch_data()
            self.clear()
            con.close()
            messagebox.showinfo("Success","Record has been updated")
            

    def Search_users(self):
        self.Restaurant_table.tag_configure('odd',background='pale green')
        self.Restaurant_table.tag_configure('even',background='steel blue')
        
        con=mysql.connector.connect(host="localhost",user="root",password="12345",database='Restaurant')
        cursor=con.cursor()
        cursor.execute("select Username, Account_Type from users where "+str(self.Search_by.get()).replace(" ","_")+" like '%"+str(self.Search_txt.get()) +"%'")
        rows=cursor.fetchall()
        if len(rows)!=0:
            self.Restaurant_table.delete(*self.Restaurant_table.get_children())
            count=0
            for rows in rows:
                if count%2==0:
                    self.Restaurant_table.insert('',END,values=rows,tags=('even'))
                    count+=1
                else:
                    self.Restaurant_table.insert('',END,values=rows,tags=('odd'))
                    count+=1      
            con.commit()
        con.close()

    def delete(self):
        if self.Username.get()=="" or self.Account_type.get()=="":
            messagebox.showerror("Error","Please select account")
        else:
            con=mysql.connector.connect(host="localhost",user="root",password="12345",database='Restaurant')
            cursor=con.cursor()
            cursor.execute("delete from users where Username='"+self.Username.get()+"'")
            con.commit()
            con.close()
            self.fetch_data()
            self.clear()
            messagebox.showinfo("Success","Record has been deleted")

        
    def exit(self):
        q=tkinter.messagebox.askquestion("Exit Application","Do you want to exit?")
        if q=="yes":
            self.root.destroy()
        else:
            return

    def manage_items(self):
        self.root.destroy()
        import manage_items
        


    


    



main()
