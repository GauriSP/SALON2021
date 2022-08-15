import mysql.connector
mydb= mysql.connector.connect(host="localhost",user="root",passwd="password",database="Salon")
mc=mydb.cursor()
mc.execute("Create table SERVICES(Service_ID integer PRIMARY KEY NOT NULL AUTO_INCREMENT, Service_Name char(25), Price integer)")


