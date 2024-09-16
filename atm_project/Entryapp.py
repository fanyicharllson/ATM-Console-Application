import hashlib
from database import Database
from atm import ATM


# Method to hash password
def hashed_password(password: str) -> str:
    sha256 = hashlib.sha256()
    sha256.update(password.encode('utf-8'))
    return sha256.hexdigest()

# Global input for collecting username and password
def userEntryInfo():
    while True:
        try:
            name = input("Enter your name: ")
            user_password = input("Enter your password: ")
            return name, user_password
        except Exception as e:
            print("Invalid username or password")
            print("Please try again!")

# Login method
def login():
    print("Signing in...")
    conn = Database("C:/Users/NTECH/OneDrive/Desktop/CREATED DATABASES/atm.db")
    if conn:
        name, userpassword = userEntryInfo()
        c = conn.cursor()
        # Hash the entered password before comparing
        hashed_pass = hashed_password(userpassword)
        c.execute("SELECT COUNT(*) FROM users WHERE username=? AND password=?", (name, hashed_pass))
        data = c.fetchone()
        if data and data[0] > 0:
            print()
            print("Login successful! Welcome", name)
            ATM(name)  #  ATM functionality is available
        else:
            print("Invalid username or password!")
            print("\n")
            
    else:
        print("Connection Error")
        return False

# Signup method
def signup():
    print("Signing up...")
    try:
        connection = Database("C:/Users/NTECH/OneDrive/Desktop/CREATED DATABASES/atm.db")
        if connection:
            name, userpassword = userEntryInfo()
            c = connection.cursor()
            c.execute("SELECT COUNT(*) FROM users WHERE username=?", (name,))
            if c.fetchone()[0] > 0:
                print('Error: Username already exists. Please try again.')
                return
            
            new_hash_password = hashed_password(userpassword)
            c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (name, new_hash_password))
            print("Sign Up was successful!")
            connection.commit()
            ATM(name)  #  ATM functionality is available
        else:
            print("Error connecting to the database")
    except Exception as e:
        print("Sign Up Failed! Please try again.", e)
    finally:
        connection.close()

# Sign out method
def signout():
    print("Signed out!")
    quit()

# Invalid choice method
def Invalid_choice():
    print("Invalid choice! Please try again.")

# Starting of the ATM project
def EntryInfo():
     print()
     print("Please login or sign up to start using ATM.")
    
     while True:
        print("1) Sign Up")
        print("2) Sign In")
        print("3) Sign Out")
        
        info = {
            1: signup,  # Fixed mapping for sign-up and login
            2: login,
            3: signout  
        }
        try:
            user_choice = int(input("Option(1-3): "))
            info.get(user_choice, Invalid_choice)()
            
        except Exception as e:
            print(f"Error: {e}")
            print('Please try again!')
            
   