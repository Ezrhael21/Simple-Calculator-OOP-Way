# Ezrhael R. Sicat
# BSCpE 1-5 
# 05/22/2023
# This program will create a simple calculator in an OOP way.

# Import Tkinter
from tkinter import *
# Import UserInterface
from New_User_Interface import NewUserInterface

# Create the window
window = Tk()
window.title("Simple Calculator")
window.geometry("400x200")

# Call the New User Interface
app = NewUserInterface(window)

window.mainloop()




