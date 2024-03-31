import sqlite3
import tkinter as tk
from tkinter import messagebox


def sign_in(event=None):  
    print("Sign in button clicked")  
    email = email_entry.get()
    password = password_entry.get()
     
    c.execute("SELECT * FROM users WHERE email=? AND password=?", (email, password))
    user = c.fetchone()
    
    if user:
        login_message.config(text="Log in successful.", fg="green")
    else:
        login_message.config(text="Email or password incorrect.", fg="red")

conn = sqlite3.connect('usersinfo.db')
c = conn.cursor()

root = tk.Tk()
root.title("Sign In")


tk.Label(root, text="Email:").grid(row=0, column=0, sticky="e")
tk.Label(root, text="Password:").grid(row=1, column=0, sticky="e")

email_entry = tk.Entry(root)
password_entry = tk.Entry(root, show="*")

email_entry.grid(row=0, column=1)
password_entry.grid(row=1, column=1)

login_button = tk.Button(root, text="Sign In")
login_button.grid(row=2, columnspan=2)

login_button.bind("<Button-1>", sign_in)

login_message = tk.Label(root, text="", fg="black")
login_message.grid(row=3, columnspan=2)

root.mainloop()
