**Author:** Atte Ilari Tarkiainen
**Date:** 05.09.2023
**Platform:** MacOS Ventura 13.5.1
**Application Version:** 1.0
**Python Version:** Python 3.11.5

# Basic Calc.
### Summary

This calculator is a Python project that serves to demonstrate the basics of object oriented programming (OOP) & the Model View Controller (MVC) -architecture / design pattern.

As such, the file & folder structure in this project is split according to the MVC-architecture where -/main.py acts as a the main entry point for the program, view/calculator_view.py acts as the GUI, controller/calculator_controller.py handles the user's input events & model/calculator_model.py handles the logic functions necessary for the calculator to evaluate the expressions given to it.

The script has not been packaged into a .exe for the purposes of this demonstration. All source code is executable as long as Python3 is installed on the computer. To run the calculator, download the entire repository & run the -/main.py file via texteditor, IDE or terminal of your choosing.

### Functionality

Basic Calc. gathers user input either via pressing the virtual buttons on the GUI or via keystrokes.

Recognized keystrokes include:

- 0-9 (Digits)
- Enter (Equals)
- Backspace (Remove Last Added Character)
- Plus (Addition)
- Minus (Subtraction)
- Asterisk (Multiplication)
- Slash (Division)
- c or C (Clear)

Basic Calc. can handle the following operations:

- Addition
- Subtraction
- Multipliciation
- Division
- Clear
- Squared
- Square Root
- Equals

### To-Do

- Invalid input catching (such as multiple decimal points in a single number)
- Syntax Error, divide by 0 Error and other Error catching and display

### Screenshots

![Basic Calc. on startup](<Screenshot 2023-09-05 at 16.44.56.png>)
![Basic Calc. with an expression](<Screenshot 2023-09-05 at 16.46.29.png>)
