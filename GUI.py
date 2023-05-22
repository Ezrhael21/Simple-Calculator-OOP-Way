from tkinter import *

# Class for User Interface
class UserInterface(Frame):
    def __init__ (self, master):
        # Initialize the Frame
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()
        self.calculator()
    
    # Method to create widgets
    def create_widgets(self):

        # Widget for Input1 Label
        self.input1_label = Label(self, text = "Input 1:", bg="blue")
        self.input1_label.grid(row=0, column=0)
        
        # Widget for Input1 Entry
        self.input1 = Entry(self)
        self.input1.grid (row=0, column=1)

        # Widget for Input2 Label
        self.input2_label = Label(self, text = "Input 2:", bg="blue")
        self.input2_label.grid (row=1, column=0)

        # Widget for Input2 Label
        self.input2 = Entry(self)
        self.input2.grid (row=1, column=1)

        # Widget for operator label
        self.operator_label = Label(self, text = "Select Oprator:")
        self.operator_label.grid (row=2, column=0)

        # Set the initial string value to "addition"
        self.operator_var = StringVar(self)
        self.operator_var.set("addition")

        # Create a drop down menu for selecting operator
        self.operator_options = OptionMenu(self, self.operator_var, "addition", "subtraction", "multiplication", "division")
        self.operator_options.grid(row=2, column=1)

        # Method to define a function to be called when the button is pressed
        def button_press(self):
            try:
                # Retrieve the values from the input fields and operator selection
                number_one = self.input1.get()
                number_two = self.input2.get()
                operator = self.operator_var.get()

                # Perform the calculation based on the selected operator
                if operator == "addition":
                    result = self.calculator.add(number_one, number_two)
                elif operator == "subtraction":
                    result = self.calculator.subtract(number_one, number_two)
                elif operator == "multiplication":
                    result = self.calculator.multiply(number_one, number_two)
                  

            

            


         












    
    



