# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 21:44:42 2024

@author: Eshaan Gurjar
"""

from tkinter import *
from tkinter import messagebox

username_value = "Kalpana"
password_value = "Sattu"

root = Tk()
root.geometry("600x400")

login = Label(root, text = "Login", font = ("Helvetica Bold", 20))
login.place(relx = 0.5, rely = 0.1, anchor = CENTER)

username = Label(root, text = "Username", font = ("Helvetica Bold", 11))
username.place(relx = 0.1, rely = 0.2, anchor = CENTER)

username_take = Entry(root, width = 90)
username_take.place(relx = 0.5, rely = 0.3, anchor = CENTER)

password = Label(root, text = "Password", font = ("Helvetica Bold", 11))
password.place(relx = 0.1, rely = 0.4, anchor = CENTER)

password_take = Entry(root, width = 90)
password_take.place(relx = 0.5, rely = 0.5, anchor = CENTER)

def check():
    print("hello")
    if username_take.get() == username_value and password_take.get() == password_value:
        messagebox.showinfo("Logged in", "Username and Password is correct")
    else:
        messagebox.showinfo("Error", "Username or Password is incorrect")

check = Button(root, text = "Login", command = check)
check.place(relx = 0.5, rely = 0.6, anchor = CENTER)

root.mainloop()

