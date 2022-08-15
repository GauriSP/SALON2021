import mysql.connector
mydb= mysql.connector.connect(host="localhost",user="root",passwd="password",database="Salon")
mc=mydb.cursor()
mc.execute("Create table USERS(User_ID bigint PRIMARY KEY NOT NULL AUTO_INCREMENT, Name varchar(255), Phone_Number bigint)")
mc.execute("Alter table USERS AUTO_INCREMENT=1000")

