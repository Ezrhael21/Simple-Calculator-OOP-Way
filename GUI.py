from tkinter import *
from New_Calculator import OtherOptions

# Class for User Interface
class UserInterface(Frame):
    def __init__ (self, master):
        # Initialize the Frame
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()
        self.new_calculator = OtherOptions()
    
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

        # Widget for Input2 Entry
        self.input2 = Entry(self)
        self.input2.grid (row=1, column=1)

        # Widget for operator label
        self.operator_label = Label(self, text = "Select Operator:")
        self.operator_label.grid (row=2, column=0)

        # Set the initial string value to "addition"
        self.operator_var = StringVar(self)
        self.operator_var.set("addition")

        # Create a drop down menu for selecting operator
        self.operator_options = OptionMenu(self, self.operator_var, "addition", "subtraction", "multiplication", "division", "squared", command=self.new_options)
        self.operator_options.grid(row=2, column=1)

        # Widget to trigger the calculation
        self.button = Button(self, text="Calculate", command=self.button_press, bg="green")
        self.button.grid(row=3, column=1)

        # Widget to display results
        self.result_label = Label(self, text="")
        self.result_label.grid(row=4, column=1)
        
    # Method to remove input 2 from the widget when squared is pressed
    def new_options(self, selected_operator):
        if selected_operator == "squared":
            self.input2_label.grid_remove()
            self.input2.grid_remove()
        else:
            self.input2_label.grid(row=1, column=0)
            self.input2.grid(row=1, column=1)

    # Method to define a function to be called when the button is pressed
    def button_press(self):
        try:
            # Retrieve the values from the input fields and operator selection
            number_one = self.input1.get()
            number_two = self.input2.get()
            operator = self.operator_var.get()

            # Perform the calculation based on the selected operator
            if operator == "addition":
                result = self.new_calculator.add(int(number_one), int(number_two))
            elif operator == "subtraction":
                result = self.new_calculator.subtract(int(number_one), int(number_two))
            elif operator == "multiplication":
                result = self.new_calculator.multiply(int(number_one), int(number_two))
            elif operator == "division":
                result = self.new_calculator.divide(int(number_one), int(number_two))
            elif operator == "squared":
                result = self.new_calculator.squared(int(number_one))
                
            # Update the result label with the calculated value
            self.result_label.config(text=result)

        # Handle the case of invalid inputs
        except ValueError:
            self.result_label.config(text="Invalid Input. Try again!")

        # Clear the input fields after each calculation
        self.input1.delete(0, END)
        self.input2.delete(0, END)





            
            
            

            

            


         












    
    



