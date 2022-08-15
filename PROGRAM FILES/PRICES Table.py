import mysql.connector
mydb= mysql.connector.connect(host="localhost",user="root",passwd="password",database="Salon")
mc=mydb.cursor()
mc.execute("CREATE TABLE PRICES(Phone_Number bigint,Total_Price bigint, Day integer, Month integer,Year integer)")


