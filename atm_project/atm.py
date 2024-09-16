from database import Database
from transactions  import Transaction


def depositAmmount(name):
    print("Depositing...")
    connection = Database("C:/Users/NTECH/OneDrive/Desktop/CREATED DATABASES/atm.db")
    if connection:
        while True:
            try:
                amount = float(input("Enter amount you want to deposit:  "))
                if amount <= 0:
                    print("\n You cannot deposit any amount less than 0.")
                    print("Please try again!")
                    continue
                else:
                    c = connection.cursor()
                    c.execute("SELECT IFNULL(amount, 0) FROM users WHERE username=?", (name,))
                    current_balance = c.fetchone()[0]
                    
                    new_balance = current_balance + amount
                    
                    c.execute("UPDATE users SET amount=? WHERE username=? ", (new_balance, name))
                    connection.commit()
                    
                    print("\n")
                    print(f"Dear {name}, you successfully deposited ${amount}.")
                    
                    transact = Transaction(name, new_balance, None)
                    transact.information()  #Transaction details
                    print("\n")
                    return
            
            except Exception as e:
                print("Invalid amount: ", e) 
                print("Please try again.")
            
           
    connection.close()            
                   
        
    

def withdrawAmmount(name):
    print("Withdrawing...")
    try:
        connection = Database("C:/Users/NTECH/OneDrive/Desktop/CREATED DATABASES/atm.db")
        if connection:
            c = connection.cursor()
            c.execute("SELECT IFNULL(amount, 0) FROM users WHERE username=?", (name,))
            useramount = c.fetchone()[0]
            
            while True:  
                withdrawer_amount = float(input("Enter the ammount you want to withdraw:  "))
                if (withdrawer_amount > useramount):
                    print(f"Insufficient funds to withdraw! Current amount is {useramount}")
                    print("Please try again")
                    continue
                
                elif withdrawer_amount <= 0:
                    print(f"You can only withdraw amount greater than 0, {name}, you entered {withdrawer_amount}")
                    continue
                
                else:
                    new_user_ammount  = useramount - withdrawer_amount
                    c.execute("UPDATE users SET amount=? WHERE username=? ", (new_user_ammount, name))
                    connection.commit()
                    
                    print("\n")
                    print(f"Dear {name}, you successfully withdrawed ${withdrawer_amount}.")
                    
                    transact = Transaction(name, new_user_ammount, withdrawer_amount)
                    transact.information()  #Transaction details
                    print("\n")
                    return
                    
    
    except Exception as e:
        print("Error: ", e)
    
    finally:
        connection.close()            
    
    
    

def Balance(name):
    print()
    print("Balance...")
    try:
        connection = Database("C:/Users/NTECH/OneDrive/Desktop/CREATED DATABASES/atm.db")
        if connection:
            c = connection.cursor()
            c.execute("SELECT IFNULL(amount, 0) FROM users WHERE username=?", (name,))
            useramount = c.fetchone()[0]
            
            print(f"Dr {name}, your remaining balance is: ${useramount}")
            print("\n")
            
            return
   
    except Exception as e:
        print("Error: ", e)  
        print("Please try again later!")
        return 
    
    finally:
        connection.close()      
    
    

def exit(name):
    print(f"Thankyou {name}, for using this ATM!")
    quit()
    
def invalid_operation():
    print("Invalid operation. Please try again!")   



def ATM(username):
    print("\n")
    print("Welcome to ATM")
    while True:
        print("1) Deposit")
        print("2) Withdraw")
        print("3) View Balance")
        print("4) Exit")
        try:
            options = {
                1: depositAmmount,
                2: withdrawAmmount,
                3: Balance,
                4: exit
            }
            user_input = int(input("Please enter your choice(1-4): "))
            
            options.get(user_input, invalid_operation)(username)
      
        except Exception as e:
            print("Error: " + str(e) + " Please try again!")
      
           
                      
    