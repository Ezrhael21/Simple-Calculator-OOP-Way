from tkinter import *
from GUI import UserInterface

# Class for adding new method in the user interface
class NewUserInterface(UserInterface):
    # Method to remove input 2 label and entry from the widget when squared is pressed
    def new_options(self, selected_operator):
        if selected_operator == "squared":
            self.input2_label.grid_remove()
            self.input2.grid_remove()
        else:
            self.input2_label.grid(row=1, column=0)
            self.input2.grid(row=1, column=1)
