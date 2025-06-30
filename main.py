
import json
import random
import string
from pathlib import Path



class Bank:
    database='data.json'
    data= []
    try:
        if Path(database).exists():
           with open(database) as fs:
             data= json.loads(fs.read())
        else :
            print("no such file exist")     
    except Exception as err:
        print(f"an error occurs as {err}")
    @classmethod  
    def __update(cls):
        with open(cls.database,'w') as fs:
            fs.write(json.dumps(Bank.data)) 
    @classmethod
    def __accountNumber(cls):
        return str(random.randint(10**9, 10**10 - 1))           
    def createAccount(self):
        info={
            "name": input("Tell your name :-"),
            "age": int(input("enter your age :-")),
            "email": input("enter your email"),
            "pin": int(input("enter your pin")),
            "accountNo": Bank.__accountNumber(),
            "balance": 0
            
        }
        if info['age']<18 or len(str(info["pin"]))!=4:
            print("sorry you cannot create an account")
        else:
            print("account created successfully!!!")
            for i in info:
                print(f"{i} : {info[i]}")
            print("note your account number")    
            Bank.data.append(info)     
            Bank.__update()
    def depositMoney(self):
        accNumber=input("tell your account number:-")
        pin=int(input("enter your pin:-"))
        userData= [i for i in Bank.data if i['accountNo']==accNumber and i['pin']==pin]
        if userData==False:
            print("sorry no data found!!")
        else:
            amount=int(input("how much money you want to deposit "))
            if amount>10000 or amount<=0:
                print("sorry the amount is too much or too low so that you cannot deposit")
            else:
                userData[0]['balance']+=amount
                Bank.__update()
                print("Amount deposit successfully!!!")        
    
    def withdrawMoney(self):
        accNumber=input("tell your account number:-")
        pin=int(input("enter your pin:-"))
        userData= [i for i in Bank.data if i['accountNo']==accNumber and i['pin']==pin]
        if userData==False:
            print("sorry no data found!!")
        else:
            amount=int(input("how much money you want to deposit "))
            if userData[0]['balance']<amount:
                print("sorry you dont have that much money ")
            else:
                userData[0]['balance']-=amount
                Bank.__update()
                print("Amount withdrew successfully!!!") 
                    
     
    def showDetails(self):
        accNumber=input("tell your account number:-")
        pin=int(input("enter your pin:-"))
        userData= [i for i in Bank.data if i['accountNo']==accNumber and i['pin']==pin]
        print("Your information are \n\n")
        for i in userData[0]:
            print(f"{i} : {userData[0][i]}")
            
     
    def updateDetails(self):
        accNumber=input("tell your account number:-")
        pin=int(input("enter your pin:-"))
        userData= [i for i in Bank.data if i['accountNo']==accNumber and i['pin']==pin]
        if userData==False:
            print("sorry no data found!!")
        else:
            print("You cannot change your age, account number, balance")
            print("Fill the details for change or leave it empty if no change")
            newData={
                "name": input("please tell new name or press enter: "),
                "email":input("please enter new email or press enter: "),
                "pin":input("enter new pin or press enter: ")
            }    
            if newData["name"]=="":
                newData["name"]=userData[0]["name"]
            if newData["email"]=="":
                newData["name"]=userData[0]["name"]    
            if newData["pin"]=="":
                newData["name"]=userData[0]["name"]
            newData['age']=userData[0]['age']
            newData['accountNo']=userData[0]['accountNo']
            newData['balance']=userData[0]['balance']
            if type(newData['pin'])==str:
                newData['pin']=int(newData['pin']) 
            for i in newData:
                if newData[i]==userData[0][i]:
                    continue
                else:
                    userData[0][i]=newData[i]    
            Bank.__update()
            print("details updated successfully!!!")  
    
    
    def deleteAcc(self):
        accNumber=input("tell your account number:-")
        pin=int(input("enter your pin:-"))
        userData= [i for i in Bank.data if i['accountNo']==accNumber and i['pin']==pin]
        if userData==False:
            print("sorry no data found!!")
        else:
            check=input("press y if you actually delete the account or press n: ")
            if check=='n' or check=='N':
                print("bypassed")
            else :
                index=Bank.data.index(userData[0])
                Bank.data.pop(index)
                print("account deleted successfully!!!")
                Bank.__update()        
                  
                
        
                

user=Bank()
print("press 1 for creating an account ")
print("press 2 for deposit money in the bank ")
print("press 3 for withdraw money from bank account ")
print("press 4 for details")
print("press 5 for updating the details your account")
print("press 6 for delete  your account")
check =int(input("enter your response:-"))
if check==1:
    user.createAccount()
if check==2:
    user.depositMoney()
if check==3:
    user.withdrawMoney() 
if check==4:
    user.showDetails()     
if check==5:
    user.updateDetails()
if check==6:
    user.deleteAcc()              
    