import string
import random
import pyperclip
from tkinter import *
from tkinter.ttk import *
import tkinter as tk
from PIL import Image, ImageTk
from ttkthemes import ThemedTk

# root = tk.Tk()  
root = ThemedTk(theme="arc") 
var = IntVar()
var1 = IntVar()
root.configure(bg="lightblue")
root.title("Random Password Generator")
root.geometry("400x400+400+180")


output_pass = StringVar()
 
all_combi = [string.punctuation, string.ascii_uppercase, string.digits, string.ascii_lowercase] 

def randPassGen():
    length = int(pass_len.get())

    characterList = ""
    if digit_var.get() == 1:
        characterList += string.digits
    if letter_var.get() == 1:
        characterList += string.ascii_letters
    if special_var.get() == 1:
        characterList += string.punctuation

    password = []

    for i in range(length):
        randomchar = random.choice(characterList)
        password.append(randomchar)
        output_pass.set(password)

def copyPass():
    
    pyperclip.copy(output_pass.get())





pass_head = tk.Label(root, text = 'Password Length', font = 'arial 12 bold',bg="lightblue").pack(pady=10) 
 
pass_len = IntVar() 
length = Spinbox(root, from_ = 4, to_ = 32 , textvariable = pass_len , width = 24, font='arial 16').pack()



digit_var = tk.IntVar()
digit_check = tk.Checkbutton(root, text="Digits", variable=digit_var,bg="lightblue", ).pack(pady=5)


letter_var = tk.IntVar()
letter_check = tk.Checkbutton(root, text="Letters", variable=letter_var,bg="lightblue").pack()


special_var = tk.IntVar()
special_check = tk.Checkbutton(root, text="Special characters", variable=special_var,bg="lightblue").pack()



radio_low = tk.Radiobutton(root, text="Low", variable=var, value=1,bg="lightblue").pack(pady=5)

radio_middle = tk.Radiobutton(root, text="Medium", variable=var, value=0,bg="lightblue").pack()

radio_strong = tk.Radiobutton(root, text="Strong", variable=var, value=3,bg="lightblue").pack()


pass_label = tk.Label(root, text = 'Random Generated Password', font = 'arial 12 bold', bg="lightblue").pack(pady=5)
Entry(root , textvariable = output_pass, width = 24, font='arial 16').pack()
Button(root, text = "Generate Password" , command = randPassGen).pack(pady= 5),Button(root, text = 'Copy to Clipboard', command = copyPass).pack(pady= 5)

root.mainloop()