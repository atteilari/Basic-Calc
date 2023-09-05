import tkinter as tk

class CalculatorView:

    def __init__(self, root):
        self.root = root
        self.root.resizable(False, False)
        self.root.title("Basic Calc 1.0") 
        self.controller = None  # Placeholder for the controller object

        # Create a string variable for storing the result of the calculator
        self.result = tk.StringVar()

        # Create an Entry widget for displaying the calculator's input and output.
        entry = tk.Entry(self.root, textvariable=self.result, justify="right", font=("Helvetica", 34), width=20)
        entry.grid(row=0, column=0, columnspan=4)  # Place the Entry widget in the GUI

        # Define labels for calculator buttons
        button_labels = [
            "C", "√", "x²", "/",
            "7", "8", "9", "*",
            "4", "5", "6", "-",
            "1", "2", "3", "+",
            "±", "0", ".", "="
        ]

        # Initialize row and column counters for button placement in the GUI
        row = 1
        col = 0

        # Create buttons
        for label in button_labels:
            # Create a Button widget with specified properties and associate a command (click handler) to it
            button = tk.Button(self.root, highlightthickness=0, text=label, height=5, width=7, command=lambda l=label: self.controller.button_click(l))

            # Configure button color (orange for operators and special buttons, black for numbers)
            if label in {"C", "√", "x²", "/", "*", "-", "+", ".", "=", "±"}:
                button.configure(fg="orange")
            else:
                button.configure(fg="black")

            # Place the button in the GUI
            button.grid(row=row, column=col)
            col += 1

            # Manage grid
            if col > 3:
                col = 0
                row += 1

    
    def set_controller(self, controller):
        self.controller = controller
