import datetime as dt
import csv
print(dt.datetime.now())
print()
flag=1
print("WELCOME TO BELLE AME SALON")
print()

import mysql.connector
from tabulate import tabulate
mydb= mysql.connector.connect(host="localhost",user="root",passwd="password",database="Salon")
mc=mydb.cursor()


while(flag):
    print("1.Register","2.Display Services","3.Report","4.Modification of Service Menu","5.Exit",sep="\n")
    print()
    c=int(input("Enter your choice: "))
    print()

    
    if c==1:
        while(c==1):
            name=input("Enter Name of Client: ")
            phoneno=int(input("Enter client's phone number: "))
            s="Insert into Salon.USERS(Name,Phone_Number) VALUES(%s,%s)"
            b1=(name,phoneno)
            mc.execute(s,b1)
            print()
            t=input("Do you have another person to register Yes or NO: ")
            if t.upper()=="YES":
                print()
                c==1
            if t.upper()=="NO":
                c=99
                print()
                print("Thank You for for registering")
                print()
    mydb.commit()
    

    if c==2:
        mc.execute("Select * from SERVICES")
        serv=mc.fetchall()
        print(tabulate(serv,headers=["Service ID","Service Name","Price"], tablefmt="psql"))
        print()
        mob=int(input("What is the client's phone number: "))
        mc.execute("Select Name from USERS where Phone_Number={}".format(mob))
        nm=mc.fetchall()
        print()
        if nm==[]:
            print("This Number hasn't been registered. PLease Register first")
            print()
               
        else:
            for row in nm:
                print("This is the record of services for ",row[0])

            p=1
            totalprice=0
            while(p==1):
                print()
                choi=int(input("Enter the required Service ID: "))
                mc.execute("Select Price from SERVICES where Service_ID={}".format(choi))
                pil=mc.fetchall()
                for i in pil:
                    totalprice+=i[0]
            
                print()
                t=input("Does client have more service: YES or NO ")
                if t.upper()=="YES":
                    p==1
                if t.upper()=="NO":
                    print()
                    print("Total Price is",totalprice)
                    p=99

                d=dt.date.today()
                day=d.day
                month=d.month
                year=d.year
            s="Insert into PRICES(Phone_Number,Total_Price,Day,Month,Year) VALUES(%s,%s,%s,%s,%s)"
            b1=(mob,totalprice,day,month,year)
            mc.execute(s,b1)
            print()
        mydb.commit()
            
            
    
        
        

    if c==3:
        print("1.Monthly Report","2.Customer Report","3.Return To Main Menu",sep="\n")
        print()
        opt=int(input("Enter your choice: "))
        
        if opt==1:
            ye=int(input("Enter Year YYYY: "))
            mon=input("Enter the month: ")
            if mon.upper()=="JANUARY":
                ml=1
            if mon.upper()=="FEBRUARY":
                ml=2
            if mon.upper()=="MARCH":
                ml=3
            if mon.upper()=="APRIL":
                ml=4
            if mon.upper()=="MAY":
                ml=5
            if mon.upper()=="JUNE":
                ml=6
            if mon.upper()=="JULY":
                ml=7
            if mon.upper()=="AUGUST":
                ml=8
            if mon.upper()=="SEPTEMBER":
                ml=9
            if mon.upper()=="OCTOBER":
                ml=10
            if mon.upper()=="NOVEMBER":
                ml=11
            if mon.upper()=="DECEMBER":
                ml=12
            print()
            mc.execute("Select * from PRICES where Month={} and Year={}".format(ml,ye))
            monrep=mc.fetchall()
            mc.execute("select SUM(Total_Price) from PRICES where Month={} and Year={}".format(ml,ye))
            net_income=mc.fetchone()[0]
            print()
            if monrep==[]:
                print("NO RECORDS FOUND THIS MONTH OF GIVEN YEAR")
                print()
               
            else:
                print("TOTAL AMOUNT GAINED IN",mon.upper(),"IN",ye)
                print(net_income)
                column_names=["Phone_Number","Total_Price","Day","Month","Year"]
                fp=open("MONTHLY_REPORT.csv","w")
                myfile=csv.writer(fp)
                myfile.writerow(column_names)
                myfile.writerows(monrep)
                fp.close()
                print()
                print("TO TAKE A COPY OF THE RECORDS FOR THIS MONTH PLEASE PRINT THE FILE MONTHLY_REPORT.CSV")
                print()
            

        if opt==2:
            print()
            mob=int(input("Enter phone number for report: "))
            print()
            mc.execute("select Name from USERS where Phone_Number={}".format(mob))
            l=mc.fetchall()
            mc.execute("select * from PRICES where Phone_Number={}".format(mob))
            monrep=mc.fetchall()
            mc.execute("select SUM(Total_Price) from PRICES where Phone_Number={}".format(mob))
            net_income=mc.fetchone()[0]
            
            if monrep==[]:
                print("NO RECORDS FOUND FOR THIS PHONE NUMBER")
                print()
               
            else:
                print("TOTAL AMOUNT THAT",l[0][0],"HAS SPENT HERE")
                print(net_income)
                print()
                column_names=["Phone_Number","Total_Price","Day","Month","Year"]
                fp=open("CUSTOMER_REPORT.csv","w")
                myfile=csv.writer(fp)
                myfile.writerow(column_names)
                myfile.writerows(monrep)
                fp.close()
                print("TO TAKE A COPY OF THE RECORDS FOR THIS NUMBER PLEASE PRINT THE FILE CUSTOMER_REPORT.CSV")
                print()
                
        if opt==3:
            print()
            continue
    

    if c==4:
        print("1.Add Services","2.Modify Prices of Services","3.Remove Service","4.Return To Main Menu",sep="\n")
        print()
        opti=int(input("Enter Your choice: "))
        if opti==1:
            na=input("Enter name of Service: ")
            pr=int(input("Enter price of service: "))
            print()
            s="Insert into Salon.SERVICES(Service_Name,Price) VALUES(%s,%s)"
            b1=(na,pr)
            mc.execute(s,b1)
            print("Added Successfully")
            print()
        mydb.commit()

        if opti==2:
            nam=input("Enter the name of the Service whose price should be changed: ")
            pri=int(input("Enter new price of service: "))
            print()
            si="Update Salon.SERVICES SET Price = %s WHERE Service_Name = %s"
            b2=(pri,nam)
            mc.execute(si,b2)
            print("Modified Successfully")
            print()
        mydb.commit()

        if opti==3:
            se=input("Enter the name of the Service which should be deleted: ")
            print()
            sip="DELETE from Salon.SERVICES where Service_Name = %s"
            b3=(se,)
            mc.execute(sip,b3)
            print("Deleted Successfully")
            print()
        mydb.commit()

        if opti==4:
            print()
            continue
            
    

    if c==5:
        break


print("THANK YOU FOR USING OUR SERVICE. PLEASE VISIT AGAIN")
