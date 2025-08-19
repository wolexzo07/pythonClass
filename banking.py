def accountName(username):

    fullname = ["Biobaku Oluwole","Ayodeji Peter","Wale Adeniji"]

    nameList = ["oluwole","ayo","wale"]

    if(username == nameList[0]):

        return "Account Name : " + fullname[0]
    
    elif(username == nameList[1]):

        return "Account Name : " + fullname[1]
    
    elif(username == nameList[2]):

        return "Account Name : " + fullname[2]
    
    else:

        return "No account name for " + username
    
    
def accountNameRF(username):

    fullname = ["Biobaku Oluwole","Ayodeji Peter","Wale Adeniji"]

    nameList = ["oluwole","ayo","wale"]

    if(username == nameList[0]):

        return fullname[0]
    
    elif(username == nameList[1]):

        return fullname[1]
    
    elif(username == nameList[2]):

        return fullname[2]
    
    else:

        return "nil"


def accountNumber(username):

    nameList = ["oluwole","ayo","wale"]

    accountList = ["1019011991","1100929221","1100929215"]

    if(username == nameList[0]):

        return "Account Number : " + accountList[0]
    
    elif(username == nameList[1]):

        return "Account Number : " + accountList[1]
    
    elif(username == nameList[2]):

        return "Account Number : " + accountList[2]
    
    else:
        return "No account number for " + username


def accountBalance(username):

         nameList = ["oluwole","ayo","wale"]

         balances = [100.89 , 200.76 , 400.98]

         if(username == nameList[0]):
             
             return "Account Balance : $" + str(balances[0])
             
         elif(username == nameList[1]):
             
             return "Account Balance : $" + str(balances[1])
         
         elif(username == nameList[2]):
             
             return "Account Balance : $" + str(balances[2])
         
         else:
             
             return "No account balance for " + username
         

def getBalance(username):

         nameList = ["oluwole","ayo","wale"]

         balances = [100.89 , 200.76 , 400.98]

         if(username == nameList[0]):
             
             return float(balances[0])
             
         elif(username == nameList[1]):
             
             return float(balances[1])
         
         elif(username == nameList[2]):
             
            return float(balances[2])
         
         else:
             
            return "No profile found"
             
    
def myAccount(username):

        nameList = ["oluwole","ayo","wale"]

        if(username == nameList[0]):
             
             print("========================")
             print(accountName(username))
             print(accountNumber(username))
             print(accountBalance(username))
             print("========================")
             
        elif(username == nameList[1]):
             
             print("========================")
             print(accountName(username))
             print(accountNumber(username))
             print(accountBalance(username))
             print("========================")
             
        elif(username == nameList[2]):
             
             print("========================")
             print(accountName(username))
             print(accountNumber(username))
             print(accountBalance(username))
             print("========================")
             
        else:
             
             print("No profile")


def removeMoney(username , amount):

    nameList = ["oluwole","ayo","wale"]

    balance = getBalance(username)

    # checking if user have sufficient balance

    if(balance < amount):

        print("Oops::You have insufficient balance")
    
    else:

        amountLeft = balance - float(amount)
        acctName = accountNameRF(username)

        print("========================")
        print("Account Name               : ",acctName)
        print("Withdrawal Amount          :  $" , float(amount))
        print("Balance Before withdrawal  :  $" , float(balance))
        print("Balance After withdrawal   :  $" , float(amountLeft))
        print("========================")


def addMoney(username , amount):
      
      nameList = ["oluwole","ayo","wale"]
    
      balance = getBalance(username)

      if(username == nameList[0]):
        
        return float(amount) + balance
      
      elif(username == nameList[1]):
        
        return float(amount) + balance
      
      elif(username == nameList[2]):
        
        return float(amount) + balance
      
      else:
          
          return "No account found"

           

addup = addMoney("ayo" , 100)  
#print(addup)

removeMoney("ayo" , 80.67)
removeMoney("wale" , 40.89)
removeMoney("oluwole" , 14.88)
           

          



"""
myAccount("oluwole")
myAccount("ayo")
myAccount("wale")
myAccount("ojo")

"""

#print(getBalance("oluwole"))
#print(getBalance("ayo"))
#print(getBalance("ayo"))