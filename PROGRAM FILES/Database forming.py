import mysql.connector
mydb= mysql.connector.connect(host="localhost",user="root",passwd='password')
mc=mydb.cursor()
mc.execute("Create Database Salon")

#Optional part just for my understanding
#mc.execute("Show Databases")
#for a in mc:
    #print(a)
