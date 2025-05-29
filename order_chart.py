import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import mysql.connector

def chart2():
    con=mysql.connector.connect(host='localhost',user='root',password='12345',database='restaurant')
    cursor=con.cursor()
    sql1="select Total,Customer_Name from orders"
    cursor.execute(sql1)
    result=cursor.fetchall()
    df=pd.DataFrame(list(result),columns=["Customer_Name","Total"])
    x=df.Customer_Name
    y=df.Total
    plt.ylabel("Customer_Name")
    plt.xlabel("Total")
    plt.title("Order Chart")
    plt.barh(y,x,color="blue",height=0.5)
    plt.show()
    cursor.close()

chart2()
