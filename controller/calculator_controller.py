class CalculatorController:

    def __init__(self, model, view):
        self.model = model
        self.view = view

    # Handle user input via clicking GUI buttons
    def button_click(self, button_label):
        current_input = self.view.result.get()
        self.model.evaluate(current_input, button_label)

    # Bind keyboard events to the main window
    def bind_keyboard_events(self):
        self.view.root.bind("<KeyPress>", self.key_press)

    # Handle key press events
    def key_press(self, event):
        current_input = self.view.result.get()
        # Get the key that was pressed.
        key = event.keysym

        # Check if the pressed key is a digit, operator, Enter, or Backspace, if so handle accordingly
        if key.isdigit() or key in ("\r", "\x7f", "Return", "BackSpace", "plus", "minus", "asterisk", "slash", "c", "C"):
            if key in ("Return", "KP_Enter"):
                self.model.evaluate(current_input, "=")
            elif key == "BackSpace":
                self.model.evaluate(current_input, "<-")
            elif key == "plus":
                self.model.evaluate(current_input, "+")
            elif key == "minus":
                self.model.evaluate(current_input, "-")
            elif key == "asterisk":
                self.model.evaluate(current_input, "*")
            elif key == "slash":
                self.model.evaluate(current_input, "/")
            elif key in ("c", "C"):
                self.model.evaluate(current_input, "C")
            else:
                self.model.evaluate(current_input, key)

    # Start listening for keyboard events
    def start_listening(self):
        self.bind_keyboard_events()

