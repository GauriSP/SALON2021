import mysql.connector
mydb= mysql.connector.connect(host="localhost",user="root",passwd="password",database="Salon")
mc=mydb.cursor()
mc.execute("Alter table SERVICES AUTO_INCREMENT=1")
mc.execute("ALTER TABLE SERVICES MODIFY Service_Name char(25)")
