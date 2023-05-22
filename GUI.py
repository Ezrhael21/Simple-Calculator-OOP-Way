from tkinter import *

# Class for User Interface
class UserInterface(Frame):
    def __init__ (self, master):
        # Initialize the Frame
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()
        self.calculator()
    
    def create_widgets(self):
        self.input1_label = Label(self, text = "Input 1:", bg="blue")
        self.input1_label.grid(row=0, column=0)

    
    



