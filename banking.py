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

    


myAccount("oluwole")
myAccount("ayo")
myAccount("wale")
myAccount("ojo")