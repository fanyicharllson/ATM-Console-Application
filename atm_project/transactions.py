from datetime import datetime

class Transaction:
    now = datetime.now()
    def __init__(self, username, ammount, withdrawAmount):
        self.__username = username 
        self.__ammount = ammount
        self.__withdrawAmount = withdrawAmount
    
    def get_name(self):
        return self.__username
    
    def get_amount(self):
        return self.__ammount 
    
    def information(self):
        print("\n")
        print(f"{self.__username}, below are your transaction history..\n")
        print(f"Name: {self.__username}")
        print(f"Amount in Total: ${self.__ammount}")
        if (self.__withdrawAmount == None): 
            print(f"Withdrawed Amount: $0, nothing withdrawed!")
        else:
            print(f"Withdrawed Amount: ${self.__withdrawAmount}")
            
        print(f"Transaction date: {Transaction.now.strftime('%Y-%m-%d')}")  
        print(f"Transaction time: {Transaction.now.strftime("%H:%M:%S")}") 
        