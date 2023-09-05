# Import Tkinter for GUI
import tkinter as tk

# Import classes from different modules for the calculator application.
from view.calculator_view import CalculatorView
from model.calculator_model import CalculatorModel
from controller.calculator_controller import CalculatorController


def main():
    # Create the main application window using tkinter
    root = tk.Tk()

    # Create an instance of the CalculatorView class, which represents the GUI for the calculator
    view = CalculatorView(root)

    # Create an instance of the CalculatorModel class, which represents the underlying data and calculations
    model = CalculatorModel(view)

    # Create an instance of the CalculatorController class, which handles user interactions and updates the model and view
    controller = CalculatorController(model, view)

    # Associate the view with the controller
    view.set_controller(controller)

    # Start listening for user input and events
    controller.start_listening()
    root.mainloop()

# Check if this script is the main program being run, if so, execute the main() function to start the application
if __name__ == "__main__":
    main()
