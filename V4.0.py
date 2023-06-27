"""
Project: MugBit
Programmer: Harsh Moreshwar Kale
Date: 27/06/2023
"""

# Import Statements
from tkinter import *
from tkinter import font
from docxtpl import *
from wikipedia import *
from docx import Document

# Create top level window
root = Tk()

# Set window title
root.title("MugBit")

# Set window size
root.geometry("1200x800")

# Set window icon
root.wm_iconbitmap("MugBit.ico")

# Designing the interface
nameLabel = Label(text="Enter Your Name", fg="orange")
nameLabel.pack()
rollNoLabel = Label(text="Enter Your Roll Number", fg="red")
rollNoLabel.pack()
ENRNoLabel = Label(text="Enter Your Enrollment Number", fg="blue")
ENRNoLabel.pack()
name = Entry(width=25, font=("Arial", 10))
name.pack()
rollNo = Entry(width=25, font=("Arial", 10))
rollNo.pack()
enrNo = Entry(width=25, font=("Arial", 10))
enrNo.pack()

# Looping the main window
root.mainloop()

