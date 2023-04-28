from tkinter import *
from tkinter import messagebox
from password_strength import PasswordStats

def check_strength():
 if entry.get() == "":
    messagebox.showinfo("Error","Password cant be empty")    
 else:
    result = PasswordStats(entry.get())
    strength = result.strength()
    if strength >= 0.66:
        new = "Passowrd is strong"
        result_label.config(text=new)
    elif strength < 0.66 and strength > 0.5:
        new = "Password is good"
        result_label.config(text=new)
    else:
        new = "Password is poor" 
        result_label.config(text=new)
   

root = Tk()

root.title("Password-strength")
root.geometry("300x500")
root.resizable(0,0)
root.configure(background="black")


title = Label(root, text = "Password-Strength-Calculator", bg="black", fg="white")
title.pack(ipady=15)
title.config(font=("verdana",12,"bold"))

value = Label(root, text= "Enter your password", bg = "black", fg="white")
value.pack(ipady = 5)
value.config(font = ("verdana",10))

entry = Entry(root)
entry.pack(ipady = 4)

btn = Button(root, text = "Check", command = check_strength)
btn.pack(pady = 10)


result_label = Label(root, text = "Password - Strength ", bg = "black", fg = "white")
result_label.pack()
result_label.config(font = ("verdana",10))

root.mainloop()