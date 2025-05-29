import mysql.connector 
con=mysql.connector.connect(host="localhost",user="root",password="12345")
cursor=con.cursor()
cursor.execute("create database restaurant")
con2=mysql.connector.connect(host="localhost",user="root",password="12345",database="restaurant")
cursor=con2.cursor()
cursor.execute("create table users(Username varchar(100) primary key, Password varchar(100), Account_Type varchar(100))")
cursor.execute("create table  items(Item_Code integer primary key, Item_Name varchar(100), Price integer, No_of_Piece integer, Meal_Type varchar(100))")
cursor.execute('''create table orders(Bill_No integer primary key, Customer_Name varchar(100), Table_No varchar(100), Date DATE,Chair_1 varchar(100), Quantity_1 integer,
                        Chair_2 varchar(100), Quantity_2 integer,
                        Chair_3 varchar(100), Quantity_3 integer,
                        Chair_4 varchar(100), Quantity_4 integer,
                        Chair_5 varchar(100), Quantity_5 integer,
                        Chair_6 varchar(100), Quantity_6 integer,
                        Total integer, Grand_Total float)''')
