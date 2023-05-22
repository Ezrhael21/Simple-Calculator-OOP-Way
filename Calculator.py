# Class for Calculator
class Calculate:
    # Method to add two numbers
    def add(self, number_one, number_two):
        return number_one + number_two
    # Method to subtract two numbers
    def subtract(self, number_one, number_two):
        return number_one - number_two
    # Method to multiply two numbers
    def multiply(self, number_one, number_two):
        return number_one * number_two
    # Method to divide two numbers
    def divide(self, number_one, number_two):
        # Display error when the case is dividing by zero
        if number_two == 0:
            return "Error: Division by Zero"
        else:
            return number_one / number_two
