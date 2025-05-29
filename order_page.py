from tkinter import *
from tkinter import ttk
import tkinter
import random
import mysql.connector
from tkinter import messagebox
from datetime import datetime
from datetime import date
from datetime import *



def main():
    root=Tk()
    ob=restaurant(root)
class restaurant:
    def __init__(self,root):
        self.root=root
        self.root.title("order")
        self.root.geometry("1350x700+0+0")


 #------------------------------------------------------BackGround-------------------------------------------------------------------------------------------#
        canvas=Canvas(root, height=250, width=300)
        filename = PhotoImage(file = "bg/order.png")
        background_label = Label(image=filename)
        background_label.place(relwidth=1, relheight=1)
        Label(self.root,text="Order Page", font=('comic sans MS',40,'bold'),bg='black',fg='Cyan',bd=10).place(x=0,y=0,relwidth=1)

        #------------------------------------------------------------Variables-------------------------------------------------------------#
        today=date.today()
        td=today.strftime("%B %d,%Y")
        self.date=td
        t=datetime.now()
        self.ct=t.strftime("%H:%M:%S")
        self.cname=StringVar()
        self.Item_Name=StringVar()
        self.Price=StringVar()
        self.Total_Price=StringVar()
        self.No_of_piece=StringVar()
        self.No_of_plate=[]
        self.table=StringVar()
        self.c1=StringVar()
        self.c2=StringVar()
        self.c3=StringVar()
        self.c4=StringVar()
        self.c5=StringVar()
        self.c6=StringVar()
        self.q1=IntVar()
        self.q2=IntVar()
        self.q3=IntVar()
        self.q4=IntVar()
        self.q5=IntVar()
        self.q6=IntVar()
        
        x=random.randint(1000,9999)
        self.billno=StringVar()
        self.billno.set(x)





#--------------------------------------------------------------Left Frame----------------------------------------------------------#

        con=mysql.connector.connect(host="localhost",user="root",password="12345",database='Restaurant')
        cursor=con.cursor()
        sql="select item_name from items"
        cursor.execute(sql)
        name=cursor.fetchall()

        
        billnumber=Label(root,text="Bill No:",bg='Black',fg='White',font=("comic sans MS",20,'italic')).place(x=1000,y=100)
        billnumber=Label(root,bg='black',fg='white',font=("comic sans MS",20,'italic'),textvariable=self.billno).place(x=1095,y=100)
        
        lbl_Chair1=Label(root,text="Chair 1",bg='Black',fg='White',font=("comic sans MS",20,'italic')).place(x=50,y=200)
        combo_Chair1=ttk.Combobox(root,textvariable=self.c1,font=("comic sans MS",13,'italic'),state='readonly',values=name).place(x=200,y=200)



        lbl_Chair2=Label(root,text="Chair 2",bg='Black',fg='White',font=("comic sans MS",20,'italic')).place(x=50,y=270)
        combo_Chair2=ttk.Combobox(root,textvariable=self.c2,font=("comic sans MS",13,'italic'),state='readonly',values=name).place(x=200,y=270)
     
        

        lbl_Chair3=Label(root,text="Chair 3",bg='Black',fg='White',font=("comic sans MS",20,'italic')).place(x=50,y=340)
        combo_Chair3=ttk.Combobox(root,textvariable=self.c3,font=("comic sans MS",13,'italic'),state='readonly',values=name).place(x=200,y=340)



        lbl_Chair4=Label(root,text="Chair 4",bg='Black',fg='White',font=("comic sans MS",20,'italic')).place(x=50,y=410)
        combo_Chair4=ttk.Combobox(root,textvariable=self.c4,font=("comic sans MS",13,'italic'),state='readonly',values=name).place(x=200,y=410)
     


        lbl_Chair5=Label(root,text="Chair 5",bg='Black',fg='White',font=("comic sans MS",20,'italic')).place(x=50,y=480)
        combo_Chair5=ttk.Combobox(root,textvariable=self.c5,font=("comic sans MS",13,'italic'),state='readonly',values=name).place(x=200,y=480)
       

        lbl_Chair6=Label(root,text="Chair 6",bg='Black',fg='White',font=("comic sans MS",20,'italic')).place(x=50,y=550)
        combo_Chair6=ttk.Combobox(root,textvariable=self.c6,font=("comic sans MS",13,'italic'),state='readonly',values=name).place(x=200,y=550)
  
 
        lbl_Table=Label(root,text="Table",bg='Black',fg='White',font=("comic sans MS",20,'italic')).place(x=30,y=100)
        values=('Table 1','Table 2','Table 3','Table 4','Table 5','Table 6','Table 7','Table 8','Table 9','Table 10',)
        combo_table=ttk.Combobox(root,textvariable=self.table,font=("comic sans MS",15,'italic'),state='readonly',values=values).place(x=150,y=100)


        lbl_Cname=Label(root,text="Customer Name",bg='black',fg='white',font=("comic sans MS",17,'italic')).place(x=450,y=100)
        entry_Cname=Entry(root,textvariable=self.cname,font=("comic sans MS",16,'italic'),bd=5,relief=GROOVE).place(x=650,y=100)
   

#--------------------------------------------Quantity----------------------------------------#

        Quantity=[1,2,3,4,5,6,7,8,9,10]

        combo_Q1=ttk.Combobox(root,textvariable=self.q1,font=("comic sans MS",14,'italic'),state='readonly',values=Quantity).place(x=450,y=200)

        combo_Q2=ttk.Combobox(root,textvariable=self.q2,font=("comic sans MS",14,'italic'),state='readonly',values=Quantity).place(x=450,y=270)

        combo_Q3=ttk.Combobox(root,textvariable=self.q3,font=("comic sans MS",14,'italic'),state='readonly',values=Quantity).place(x=450,y=340)
        
        combo_Q4=ttk.Combobox(root,textvariable=self.q4,font=("comic sans MS",14,'italic'),state='readonly',values=Quantity).place(x=450,y=410)
       
        combo_Q5=ttk.Combobox(root,textvariable=self.q5,font=("comic sans MS",14,'italic'),state='readonly',values=Quantity).place(x=450,y=480)
        
        combo_Q6=ttk.Combobox(root,textvariable=self.q6,font=("comic sans MS",14,'italic'),state='readonly',values=Quantity).place(x=450,y=550)
    

#----------------------------------------------------------Buttons---------------------------------------------#

        Clearbtn=Button(root,text="Clear",command=self.clear,width=10,font=("comic sans MS",13,'italic')).place(x=1120,y=650)
        Billbtn=Button(root,text="Generate Bill",command=self.bill,width=10,font=("comic sans MS",13,'italic')).place(x=1000,y=650)

#------------------------------------------------------BILL------------------------------------------------#
        Rec=Label(root,bg='white',bd=4,font=("comic sans MS",12,'italic'),relief=GROOVE)
        Rec.place(x=900,y=150,height=250,width=350)
        Rec_title=Label(Rec,text="Bill",font=("comic sans MS",12,'italic'),bd=0,relief=GROOVE).pack(fill=X)
        scroll_y=Scrollbar(Rec,orient=VERTICAL)
        self.rec=Text(Rec,yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.rec.yview)
        self.rec.pack(fill=BOTH,expand=1)
        
        root.mainloop()
        

#-------------------------------------------------------functions-----------------------------------------------#


    def fetchall(self):
        con=mysql.connector.connect(host="localhost",user="root",password="12345",database='Restaurant')
        cursor=con.cursor()
        cursor.execute("select * from items")
        rows=cursor.fetchall()
        if len(rows)!=0:
            self.Restaurant_table.delete(*self.Restaurant_table.get_children())
            for rows in rows:
                self.Restaurant_table.insert('',END,values=rows)
            con.commit()
        con.close()

    def get_cursor(self,ev):
        cursor_row=self.Restaurant_table.focus()
        contents=self.Restaurant_table.item(cursor_row)
        row=contents['values']
        self.Item_Name.set(row[0])
        self.Price.set(row[1])

    def clear(self):
          self.table.set("")
          self.c1.set("")
          self.c2.set("")
          self.c3.set("")
          self.c4.set("")
          self.c5.set("")
          self.c6.set("")
          self.q1.set("0")
          self.q2.set("0")
          self.q3.set("0")
          self.q4.set("0")
          self.q5.set("0")
          self.q6.set("0")
          self.rec.delete('1.0',END)
          self.cname.set("")
          x=random.randint(1000,9999)
          self.billno.set(x)


    def bill(self):
        name1=self.c1.get()
        name2=self.c2.get()
        name3=self.c3.get()
        name4=self.c4.get()
        name5=self.c5.get()
        name6=self.c6.get()
        if self.table.get()=="":
            messagebox.showerror("Error","Please select table")
            return
        if self.cname.get()=="":
            messagebox.showerror("Error","Please enter customer name")
            return
        else:
            con=mysql.connector.connect(host="localhost",user="root",password="12345",database='Restaurant')
            cursor=con.cursor()
            self.rec.delete('1.0',END)
            self.rec.insert(END,f"\nCustomer Name: {str(self.cname.get())}")
            self.rec.insert(END,f"\nDate: {str(self.date)}")
            self.rec.insert(END,f"\nTime: {str(self.ct)}")
            self.rec.insert(END,f"\nBill No: {str(self.billno.get())}")
            self.rec.insert(END,f"\n{str(self.table.get())}")
            self.rec.insert(END,"\n================================")
            self.rec.insert(END,f"\nItem        Qty         Price")
            self.rec.insert(END,"\n================================")
            if self.c1.get()!=0 and self.q1.get()!=0:
                cursor.execute("select price from items where item_name='"+name1+"'")
                result=cursor.fetchone()
                for a in result:
                    a
                    t1=a*self.q1.get()
                self.rec.insert(END,f"\n{self.c1.get()}         {self.q1.get()}             {t1}")
            if self.q1.get()==0:
                t1=0

            if self.c2.get()!=0 and self.q2.get()!=0:
                cursor.execute("select price from items where item_name='"+name2+"'")
                result2=cursor.fetchone()
                for b in result:
                    b
                    t2=b*self.q2.get()
                self.rec.insert(END,f"\n{self.c2.get()}         {self.q2.get()}             {t2}")
            if self.q2.get()==0:
                t2=0

            if self.c3.get()!=0 and self.q3.get()!=0:
                cursor.execute("select price from items where item_name='"+name3+"'")
                result3=cursor.fetchone()
                for c in result:
                    c
                    t3=c*self.q3.get()
                self.rec.insert(END,f"\n{self.c3.get()}         {self.q3.get()}             {t3}")
            if self.q3.get()==0:
                t3=0

            if self.c4.get()!=0 and self.q4.get()!=0:
                cursor.execute("select price from items where item_name='"+name4+"'")
                result4=cursor.fetchone()
                for d in result4:
                    d
                    t4=d*self.q4.get()
                self.rec.insert(END,f"\n{self.c4.get()}         {self.q4.get()}             {t4}")
            if self.q4.get()==0:
                t4=0

            if self.c5.get()!=0 and self.q5.get()!=0:
                cursor.execute("select price from items where item_name='"+name5+"'")
                result5=cursor.fetchone()
                for e in result5:
                    e
                    t5=e*self.q5.get()
                self.rec.insert(END,f"\n{self.c5.get()}         {self.q5.get()}             {t5}")
            if self.q5.get()==0:
                t5=0

            if self.c6.get()!=0 and self.q6.get()!=0:
                cursor.execute("select price from items where item_name='"+name6+"'")
                result6=cursor.fetchone()
                for f in result6:
                    f
                    t6=f*self.q6.get()
                self.rec.insert(END,f"\n{self.c6.get()}         {self.q6.get()}             {t6}")
            if self.q6.get()==0:
                t6=0
            total=t1+t2+t3+t4+t5+t6
            GST=total*0.18
            Grandtotal=total+GST
            self.rec.insert(END,"\n================================")
            self.rec.insert(END,f"\n        Total:           {total}")
            self.rec.insert(END,f"\n        GST:             18%")
            self.rec.insert(END,f"\n        Grand Total:    {Grandtotal}")
            a=tkinter.messagebox.askquestion("Confirm","Would you like to confirm your order?")
            if a=="yes":
                con=mysql.connector.connect(host="localhost",user="root",password="12345",database='Restaurant')
                cursor=con.cursor()
                cursor.execute("insert into orders values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.billno.get(),
                                                                                                                                             self.cname.get(),
                                                                                                                                             self.table.get(),
                                                                                                                                             date.today(),
                                                                                                                                             self.c1.get(),
                                                                                                                                             self.q1.get(),
                                                                                                                                             self.c2.get(),
                                                                                                                                             self.q2.get(), 
                                                                                                                                             self.c3.get(),
                                                                                                                                             self.q3.get(),
                                                                                                                                             self.c4.get(),
                                                                                                                                             self.q4.get(),
                                                                                                                                             self.c5.get(),
                                                                                                                                             self.q5.get(),
                                                                                                                                             self.c6.get(),
                                                                                                                                             self.q6.get(),
                                                                                                                                             total,
                                                                                                                                             Grandtotal))
                con.commit()
                self.clear()
                con.close()
                messagebox.showinfo("Succues","Thank you for placing your order")
            if a=="no":
                return

       
main() 