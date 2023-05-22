from tkinter import *

# Class for User Interface
class UserInterface(Frame):
    def __init__ (self, master):
        # Initialize the Frame
        Frame.__init__(self, master)
        self.create_widgets()
        self.calculator()
    



