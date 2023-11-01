#!/usr/bin/env python
# coding: utf-8

# In[1]:


#importing libraries

import tkinter
from tkinter import ttk
import string
import random

# Function to generate a password

def generate_password():
    password_length = int(length.get())
    complexity_value = complexity.get()
    
    
    #Setting the complexity
    
    if complexity_value == "Low":
        characters = string.ascii_lowercase
        
    elif complexity_value == "Moderate":
        characters = string.ascii_letters + string.digits
        
    elif complexity_value == "Hard":
        characters = string.ascii_letters + string.digits + string.punctuation
        
    else:
        print("Invalid Input Entered")
        

    password = ''.join(random.choice(characters) for _ in range(password_length))
    result_label.config(text="Your Password: " + password)
    
    

# Create the main window

root = tkinter.Tk()
root.title("PASSWORD GENERATOR")



# Setting the window size
window_width = 400  # Adjust this value as needed
window_height = 300  # Adjust this value as needed
root.geometry(f"{window_width}x{window_height}")


# Password Length Label and Entry Configuration

length_label = tkinter.Label(root, text="Choose Password Length:")
length_label.pack()
length = tkinter.StringVar()
length_entry = tkinter.Entry(root, textvariable=length)
length_entry.pack()
length.set("8")


# Complexity Label and Dropdown Configuration

complexity_label = tkinter.Label(root, text="Select Password Complexity:")
complexity_label.pack()
complexity = tkinter.StringVar()

complexity_combobox = ttk.Combobox(root, textvariable=complexity, values=["Low", "Moderate", "Hard"])
complexity_combobox.pack()
complexity.set("Moderate")


# Generate Button for Generating Password

generate_button = tkinter.Button(root, text="Generate Password", command=generate_password,bg="light blue", fg="black")

generate_button.pack()


# Result Label for Showing the Generated Password 

result_label = tkinter.Label(root, text="", wraplength=300)

result_label.pack()                 


root.mainloop()


# In[ ]:




