import mysql.connector
mydb= mysql.connector.connect(host="localhost",user="root",passwd="password",database="Salon")
mc=mydb.cursor()
mc.execute("Alter table USERS Modify User_ID NOT NULL AUTO_INCREMENT=1000")
