from tkinter import *
from tkinter import ttk
import tkinter
import mysql.connector
from tkinter import messagebox
def main():
    root=Tk()
    ob=restaurant(root)
class restaurant:
    def __init__(self,root):
        self.root=root
        self.root.title("Manage Items")
        self.root.geometry("1350x700+0+0")

        
 #------------------------------------------------------BackGround-------------------------------------------------------------------------------------------#
        canvas=Canvas(root, bg="black", height=250, width=300)
        filename = PhotoImage(file = "bg/items.png")
        background_label = Label(image=filename)
        background_label.place(relwidth=1, relheight=1)
        Label(self.root,text="ITEMS", font=('comic sans MS',40,"bold"),bg="light green",fg='white',bd=10).place(x=0,y=0,relwidth=1)
        
        #----------Variables----------#
         
        self.Item_Code_var=StringVar()
        self.Item_Name_var=StringVar()
        self.Price_var=StringVar()
        self.No_of_piece_var=StringVar()
        self.Meal_type_var=StringVar()

       

        self.Search_by=StringVar()
        self.Search_txt=StringVar()
        
         #------------Left Fields------------------------------------------------------------------#

        lbl_ItemCode=Label(root,text="Item Code",bg='light green',fg='White',font=("comic sans MS",20,'italic')).place(x=30,y=190)
        txt_ItemCode=Entry(root,textvariable=self.Item_Code_var,font=("comic sans MS",15,'italic'),bd=5,relief=GROOVE).place(x=200,y=190)
 

        lbl_ItemName=Label(root,text="Item Name",bg='light green',fg='White',font=("comic sans MS",20,'italic')).place(x=30,y=250)
        txt_ItemName=Entry(root,textvariable=self.Item_Name_var,font=("comic sans MS",15,'italic'),bd=5,relief=GROOVE).place(x=200,y=250)


        lbl_Price=Label(root,text="Price",bg='light green',fg='White',font=("comic sans MS",20,'italic')).place(x=30,y=310)
        txt_Price=Entry(root,textvariable=self.Price_var,font=("comic sans MS",15,'italic'),bd=5,relief=GROOVE).place(x=200,y=310)


        lbl_Noofpiece=Label(root,text="No of piece",bg='light green',fg='white',font=("comic sans MS",20,'italic')).place(x=30,y=370)
        txt_Nofpiece=Entry(root,textvariable=self.No_of_piece_var,font=("comic sans MS",15,'italic'),bd=5,relief=GROOVE).place(x=200,y=370)
    

        lbl_Mealtype=Label(root,text="Meal type",bg='light green',fg='White',font=("comic sans MS",20,'italic')).place(x=30,y=430)
        values3=('Breakfast','Lunch','Snack','Dinner','Beverages','Breakfast/Lunch','Breakfast/Lunch/Snack/Dinner','Breakfast/Dinner','Snack/Dinner')
        combo_Mealtype=ttk.Combobox(root,textvariable=self.Meal_type_var,width=26,font=("comic sans MS",13,'italic'),state='readonly',values=values3).place(x=200,y=430)


        #--------------Left Buttons----------------------------------------------------------------------#

        Addbtn=Button(root,text="Add",width=10,command=self.add_items,font=("comic sans MS",10,'italic')).place(x=80,y=550)
        Updatebtn=Button(root,text="Update",width=10,command=self.update,font=("comic sans MS",10,'italic')).place(x=180,y=550)
        Deletebtn=Button(root,text="Delete",width=10,command=self.delete,font=("comic sans MS",10,'italic')).place(x=280,y=550)
        Clearbtn=Button(root,text="Clear",width=10,command=self.clear,font=("comic sans MS",10,'italic')).place(x=380,y=550)
        Usersbtn=Button(root,text="Manage Users",width=10,command=self.manage_users,font=("comic sans MS",10,'italic')).place(x=80,y=600)

    
    #--------------Right Buttons-----------------------------------------------------#
        lbl_Search=Label(root,text="Search By",bg='light green',fg='White',font=("comic sans MS",18,'italic')).place(x=550,y=120)
        values5=('Item Code','Item Name','No of Piece','Meal Type')
        combo_Search=ttk.Combobox(root,textvariable=self.Search_by,width=10,font=("comic sans MS",13,'italic'),state='readonly',values=values5).place(x=690,y=120)
        txt_Search=Entry(root,textvariable=self.Search_txt,width=18,font=("comic sans MS",13,'italic'),bd=5,relief=GROOVE).place(x=820,y=120)
        Searchbtn=Button(root,text="Search",width=10,pady=5,command=self.Search_data,font=("comic sans MS",10,'italic')).place(x=1020,y=120)
        Shwoallbtn=Button(root,text="Show All",width=10,pady=5,command=self.fetch_data,font=("comic sans MS",10,'italic')).place(x=1120,y=120)
        


         #------------------Table Frame---------------------------#
        Table_Frame=Frame(self.root,bd=4,relief=RIDGE)
        Table_Frame.place(x=550,y=180,width=650,height=500)

        style=ttk.Style()
        style.configure("Treeview",
                        background="white",
                        foreground="black",
                        rowheight=25,
                        fieldbackground="white")
        style.map("Treeview",
                  background=[('selected','orange')])
        scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)
        self.Restaurant_table=ttk.Treeview(Table_Frame,columns=('Item Code','Item Name','Price','No of piece','Meal Type','Category','Price Date'),yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.Restaurant_table.yview)
        self.Restaurant_table.heading('Item Code',text='Item Code')
        self.Restaurant_table.heading('Item Name',text='Item Name')
        self.Restaurant_table.heading('Price',text='Price')
        self.Restaurant_table.heading('No of piece',text='No of piece')
        self.Restaurant_table.heading('Meal Type',text='Meal Type')

       
        self.Restaurant_table['show']='headings'
        self.Restaurant_table.column('Item Code', width=115,anchor=CENTER)
        self.Restaurant_table.column('Item Name', width=115,anchor=CENTER)
        self.Restaurant_table.column('Price', width=115,anchor=CENTER)
        self.Restaurant_table.column('No of piece', width=115,anchor=CENTER)
        self.Restaurant_table.column('Meal Type', width=180,anchor=CENTER)

      
        self.Restaurant_table.pack(fill=BOTH,expand=1)
        self.Restaurant_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
        root.mainloop()  
        

    #---------------------------------------------functions-----------------------------#

    def add_items(self):
        
        if self.Item_Code_var.get()=="" or self.Item_Name_var.get()=="" or self.Price_var.get()=="" or self.No_of_piece_var.get()=="" or self.Meal_type_var.get()=="":
            messagebox.showerror("Error","All fields are required ")

            
        else:
            con=mysql.connector.connect(host="localhost",user="root",password="12345",database='Restaurant')
            cursor=con.cursor()
            cursor.execute("insert into Items values(%s,%s,%s,%s,%s)",(self.Item_Code_var.get(),
                                                                                                         self.Item_Name_var.get(),
                                                                                                        self.Price_var.get(),
                                                                                                        self.No_of_piece_var.get(),
                                                                                                        self.Meal_type_var.get()
                                                                                                        
                                                                                                     
                                                                                                          ))
            con.commit()
            self.fetch_data()
            self.clear()
            con.close()
            messagebox.showinfo("Succues","Item has been added")
            

    def fetch_data(self):
        self.Search_txt.set("")
        self.Search_by.set("")
        self.Restaurant_table.tag_configure('odd',background='thistle')
        self.Restaurant_table.tag_configure('even',background='cyan')
        
        con=mysql.connector.connect(host="localhost",user="root",password="12345",database='Restaurant')
        cursor=con.cursor()
        cursor.execute("select * from items")
        rows=cursor.fetchall()
        if len(rows)!=0:
            self.Restaurant_table.delete(*self.Restaurant_table.get_children())
            count=0
            for rows in rows:
                if count %2 ==0:
                    self.Restaurant_table.insert('',END,values=rows,tags=('even'))
                    count+=1
                else:
                    self.Restaurant_table.insert('',END,values=rows,tags=('odd'))
                    count+=1
            con.commit()
        con.close()

    def clear(self):
        self.Item_Code_var.set("")
        self.Item_Name_var.set("")
        self.Price_var.set("")
        self.No_of_piece_var.set("")
        self.Meal_type_var.set("")

       

    def get_cursor(self,ev):
        cursor_row=self.Restaurant_table.focus()
        contents=self.Restaurant_table.item(cursor_row)
        row=contents['values']
        self.Item_Code_var.set(row[0])
        self.Item_Name_var.set(row[1])
        self.Price_var.set(row[2])
        self.No_of_piece_var.set(row[3])
        self.Meal_type_var.set(row[4])

       

    def update(self):
        con=mysql.connector.connect(host="localhost",user="root",password="12345",database='Restaurant')
        cursor=con.cursor()
        cursor.execute("update Items set Item_Name=%s, Price=%s, No_of_Piece=%s, Meal_Type=%s where Item_Code=%s",(
                                                                                                    self.Item_Name_var.get(),
                                                                                                    self.Price_var.get(),
                                                                                                    self.No_of_piece_var.get(),
                                                                                                    self.Meal_type_var.get(),
                                                                                                    self.Item_Code_var.get()))
  
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()
        tkinter.messagebox.showinfo("Restaurant Management","Item has been updated")
        con=mysql.connector.connect(host="localhost",user="root",password="12345",database='Restaurant')
        cursor=con.cursor()     

    def delete(self):
        con=mysql.connector.connect(host="localhost",user="root",password="12345",database='Restaurant')
        cursor=con.cursor()
        cursor.execute("delete from items where Item_Code='"+self.Item_Code_var.get()+"'")
        con.commit()
        con.close()
        self.fetch_data()
        self.clear()
        tkinter.messagebox.showinfo("Restaurant Management","Item has been deleted")


    def Search_data(self):
        self.Restaurant_table.tag_configure('odd',background='pale green')
        self.Restaurant_table.tag_configure('even',background='steel blue')
        
        con=mysql.connector.connect(host="localhost",user="root",password="12345",database='Restaurant')
        cursor=con.cursor()
        cursor.execute("select * from items where "+str(self.Search_by.get()).replace(" ","_")+" like '%"+str(self.Search_txt.get()) +"%'")
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


    def manage_users(self):
        self.root.destroy()
        import manage_users #imports user management page 
    
        self.root.mainloop()        
main()
