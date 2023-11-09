import tkinter as tk
from tkinter import messagebox


#For Admin Login
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "admin123" 

# Function to handle login button click
def on_login_click():
    entered_username = username_entry.get()
    entered_password = password_entry.get()

    # Check if Admin is logging in
    if entered_username == ADMIN_USERNAME and entered_password == ADMIN_PASSWORD:
        messagebox.showinfo("Login Success", "Welcome Admin!")
        return
    elif entered_username == ADMIN_USERNAME and entered_password != ADMIN_PASSWORD:
        messagebox.showerror("Login Failed", "Invalid username or password. Please try again.")
        return

    with open("user_accounts.txt", "r") as file:
        while True:
            line = file.readline()
            if not line:
                break
            
            if "Username" in line:
                stored_username = line.split(":")[1].strip()
                stored_password = file.readline().split(":")[1].strip()
                
                if entered_username == stored_username and entered_password == stored_password:
                    messagebox.showinfo("Login Successful", "Login successful!")
                    return
    
    messagebox.showerror("Login Failed", "Invalid username or password. Please try again.")

def delete_all_accounts_click():
    admin_username = input("Enter admin username: ")
    admin_password = input("Enter admin password: ")

    if admin_username == ADMIN_USERNAME and admin_password == ADMIN_PASSWORD:
        with open("user_accounts.txt", "w") as file:
            file.write("")
        print("All user accounts deleted successfully!")
    else:
        print("Admin authorization failed. Please try again.")

# Function to handle exit button click
def on_exit_click():
    root.destroy()

# Tkinter GUI setup
root = tk.Tk()
root.title("Login Form")
root.geometry("340x440")
root.configure(background="#e1d8b9")

# Username Label and Entry
username_label = tk.Label(root, text="Username:")
username_label.pack()
username_entry = tk.Entry(root)
username_entry.pack()

# Password Label and Entry
password_label = tk.Label(root, text="Password:")
password_label.pack()
password_entry = tk.Entry(root, show="*")  # Show asterisks for password
password_entry.pack()

# Delete all accounts button
delete_all_accounts_button = tk.Button(root, text="Delete All Accounts", command=delete_all_accounts_click)
delete_all_accounts_button.pack()


# Login Button
login_button = tk.Button(root, text="Login", command=on_login_click)
login_button.pack()

# Exit Button
exit_button = tk.Button(root, text="Exit", command=on_exit_click)
exit_button.pack()

# Run the Tkinter event loop
root.mainloop()
