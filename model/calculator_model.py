import math

class CalculatorModel:

    def __init__(self, view):
        self.view = view
        self.chars = set('+-/*.')

    # Evaluate the expression and button click
    def evaluate(self, current_input, button_label):
        
        # Handle clear operation
        if button_label == "C":
            self.view.result.set("")

        # Handle calculating the expression using eval
        elif button_label == "=" or button_label == "\r":
            self.view.result.set(eval(current_input))
        
        # Handle square root operation
        elif button_label == "√":
            self.view.result.set(math.sqrt(float(current_input)))
        
        # Handle squared operation
        elif button_label == "x²":
            self.view.result.set(float(current_input) ** 2)
        
        # Handle sign change operation
        elif button_label == "±":
            self.view.result.set(float(current_input) * -1)
        
        # Handle backspace operation
        elif button_label == "<-":
            if current_input:
                current_input = current_input[:-1]
                self.view.result.set(current_input)

        # Handle digits
        else:
            self.view.result.set(current_input + button_label)
