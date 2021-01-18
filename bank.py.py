import csv
import sys
def heading():
    m=open("bank.csv","a",newline='')
    w=csv.writer(m)
    l={n:["ACCOUNT NO","NAME","BALANCE","AGE"]}
    w.writerow(l)
    m.close()
def data():
    m=open("bank.csv","a",newline='')
    w=csv.writer(m)
    n=int(input("Enter the SR no. Account holder"))
    
    for x in range(n):
       
        a=int(input("enter the account number"))
        n=input("Enter the name")
        b=int(input("enter balance"))
        c=int(input("age"))
        l={n:[a,n,b,c]}
        w.writerow(l)
    m.close()
def display():
    m=open("bank.csv","r",newline='')
    

    acct=csv.reader(m)
    for i in acct:
        print(i)
        

while True:
    print("bank managemet system")
    print("1 -MAIN MENU \n 2-INPUT & ADD DATA \n 3-DISPLAY \n 4-Exit")
    gh=int(input("Enter your choice"))
    if gh==1:
        heading()
    if gh==2:
        ch=int(input("Password"))
        if ch==123:
            data()
    if gh==3:
        display()
    if gh==4:
        print("Thank for using our bank managment system")
        sys.exit()