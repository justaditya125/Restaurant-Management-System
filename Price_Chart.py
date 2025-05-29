import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import mysql.connector

def chart1():
    con=mysql.connector.connect(host='localhost',user='root',password='12345',database='restaurant')
    cursor=con.cursor()
    sql1="select price,Item_Name from items"
    cursor.execute(sql1)
    result=cursor.fetchall()
    df=pd.DataFrame(list(result),columns=["price","Item_Name"])
    x=df.price
    y=df.Item_Name
    plt.xlabel("Price")
    plt.ylabel("Item Name")
    plt.title("Price Chart")
    plt.barh(y,x,color="green")
    plt.show()
    cursor.close()

chart1()
