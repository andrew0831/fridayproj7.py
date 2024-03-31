import re
import sqlite3
import tkinter as tk
from tkinter import messagebox

def validate_email(email):
    
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_pattern, email)

def sign_up():
    email = email_var.get()
    password = password_var.get()
    confirm_password = confirm_password_var.get()
    
    if password != confirm_password:
        messagebox.showerror("Error", "Passwords do not match. Please try again.")
        return
    
    if not validate_email(email):
        messagebox.showerror("Error", "Invalid email format. Please enter a valid email address.")
        return
    
    c.execute("SELECT * FROM users WHERE email=?", (email,))
    if c.fetchone():
        messagebox.showerror("Error", "Email already exists. Please use a different email.")
        return
    
    c.execute("INSERT INTO users (email, password) VALUES (?, ?)", (email, password))
    conn.commit()
    
    messagebox.showinfo("Success", "Sign up successful. You will now be redirected to the sign-in page.")
    
    root.withdraw()
    
    sign_in_window.deiconify()

conn = sqlite3.connect('usersinfo.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS users
             (email TEXT PRIMARY KEY, password TEXT)''')
conn.commit()

root = tk.Tk()
root.title("Sign Up")

tk.Label(root, text="Email:").grid(row=0, column=0, sticky="e")
tk.Label(root, text="Password:").grid(row=1, column=0, sticky="e")
tk.Label(root, text="Confirm Password:").grid(row=2, column=0, sticky="e")

email_entry = tk.Entry(root, textvariable=tk.StringVar())
password_entry = tk.Entry(root, show="*", textvariable=tk.StringVar())
confirm_password_entry = tk.Entry(root, show="*", textvariable=tk.StringVar())

email_entry.grid(row=0, column=1)
password_entry.grid(row=1, column=1)
confirm_password_entry.grid(row=2, column=1)

email_var = tk.StringVar()
password_var = tk.StringVar()
confirm_password_var = tk.StringVar()

email_entry["textvariable"] = email_var
password_entry["textvariable"] = password_var
confirm_password_entry["textvariable"] = confirm_password_var

signup_button = tk.Button(root, text="Sign Up", command=sign_up)
signup_button.grid(row=3, columnspan=2)

sign_in_window = tk.Toplevel()
sign_in_window.title("Sign In")
sign_in_window.geometry("300x100")

tk.Label(sign_in_window, text="Email:").grid(row=0, column=0, sticky="e")
tk.Label(sign_in_window, text="Password:").grid(row=1, column=0, sticky="e")

email_entry = tk.Entry(sign_in_window)
password_entry = tk.Entry(sign_in_window, show="*")

email_entry.grid(row=0, column=1)
password_entry.grid(row=1, column=1)

login_button = tk.Button(sign_in_window, text="Sign In")
login_button.grid(row=2, columnspan=2)

sign_in_window.withdraw()

root.mainloop()
