# PyLoginManager: Building a User Authentication System in Python
# import json module

import json
import os

ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "admin123"

def print_logo():
 print("""
   ____        _   _   _           _     _             
  |  _ \      | | | | | |         | |   (_)            
  | |_) | __ _| |_| |_| | ___  ___| |__  _ _ __   
  |  _ < / _` | __| __| |/ _ \/ __| '_ \| | '_ \ 
  | |_) | (_| | |_| |_| |  __/\__ \ | | | | |_) |
  |____/ \__,_|\__|\__|_|\___||___/_| |_|_| .__/ 
                                          | |        
                                          |_|        
  """)

print("Welcome, Admin!\n")




def create_account():
    username = input("Enter a username: ")
    password = input("Enter a password: ")

    if not os.path.exists("user_accounts.json"):
        with open("user_accounts.json", "w") as file:
            file.write("[]")

    with open("user_accounts.json", "r+") as file:
        try:
            user_accounts = json.load(file)
        except json.JSONDecodeError:
            user_accounts = []

        # Check if the username already exists
        for user in user_accounts:
            if user["Username"] == username:
                print("Username already exists. Please choose a different username.")
                return

        # Append new user entry
        user_accounts.append({"Username": username, "password": password})

        # Move the cursor to the beginning of the file
        file.seek(0)
        # Truncate the file
        file.truncate()
        # Write the updated user accounts
        json.dump(user_accounts, file, indent=4)

    print("====================\nAccount created successfully!\nWelcome, {0}!\n====================".format(username))



def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    with open("user_accounts.json", "r") as file:
        user_accounts = json.load(file)

    if any(user["Username"] == username and user["password"] == password for user in user_accounts):
        print("Login successful!")
    else:
        print("Invalid username or password. Please try again.")


def delete_account():
    username_to_delete = input("Enter the username to delete: ")

    with open("user_accounts.json", "r+") as file:
        try:
            user_accounts = json.load(file)
        except json.JSONDecodeError:
            user_accounts = []

        # Find and remove the user account
        updated_accounts = [user for user in user_accounts if user.get("Username") != username_to_delete]

        # Move the cursor to the beginning of the file
        file.seek(0)
        # Truncate the file
        file.truncate()
        # Write the updated user accounts
        json.dump(updated_accounts, file, indent=4)

    print(f"User account '{username_to_delete}' deleted successfully!")


def delete_all_accounts():
    # Second Version of the delete all accounts function
    print("\n⚠️  WARNING: This action will delete all user accounts.\n\nThis action cannot be undone.\n")
    
    print("Please enter the admin username and password to continue.")

    admin_username = input("Enter admin username: ")
    admin_password = input("Enter admin password: ")

    if admin_username == ADMIN_USERNAME and admin_password == ADMIN_PASSWORD:
        with open("user_accounts.json", "w") as file:
            json.dump({}, file)
        print("All user accounts deleted successfully!")
    else:
        print("Admin authorization failed. Please try again.")

# Main program
print_logo()

while True:
    print("1. Create Account")
    print("2. Login")
    print("3. Delete Account")
    print("4. Delete All Accounts (Admin Only)")
    print("5. Exit")
    print("6. Forgot Password")

    choice = input("Enter your choice (1/2/3/4/5): ")

    if choice == "1":
        create_account()
    elif choice == "2":
        login()
    elif choice == "3":
        delete_account()
    elif choice == "4":
        delete_all_accounts()
    elif choice == "5":
        print("Exiting program. Goodbye!")
        break
    elif choice == "6":
        print("Please contact the admin to reset your password.")
    else:
        print("Invalid choice. Please enter 1, 2, 3, 4, 5, or 6.")
