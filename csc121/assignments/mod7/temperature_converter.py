"""
temperature_converter.py: Converts Fahrenheit to Celsius, and vise versa.
By: Dillon. S
10/1/26
"""

import tkinter
import tkinter as gui


# Create TemperatureConverter class object
class TemperatureConverter:

    """
    Initializes the temperature converter class
    """
    def __init__(self, root: tkinter.Tk):
        self.root = root
        self.root.title("Temperature Calculator")
        self.root.geometry("400x400")
        self.root.resizable(width=False, height=False)
        self.create_widgets()

# Creates all widgets to use
    def create_widgets(self):
        # Allow column 0 and column 1 to expand evenly, keeping content centered
        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=1)

        # Header across both columns
        header = gui.Label(self.root, text="Convert Temperature", font=("Arial", 12, "bold"))
        header.grid(row=0, column=0, columnspan=2, pady=(15, 10))

        # Fahrenheit Row
        self.fahrenheit_label = gui.Label(self.root, text="Fahrenheit")
        self.fahrenheit_label.grid(row=1, column=0, sticky="e", padx=5, pady=5)

        self.fahrenheit = gui.Entry(self.root, width=20)
        self.fahrenheit.grid(row=1, column=1, sticky="w", padx=5, pady=5)
        self.fahrenheit.insert(0, "32.0")
        self.fahrenheit.bind("<Return>", lambda event: self.convert(False))

        # Celsius Row
        self.celsius_label = gui.Label(self.root, text="Celsius")
        self.celsius_label.grid(row=2, column=0, sticky="e", padx=5, pady=5)

        self.celcius = gui.Entry(self.root, width=20)
        self.celcius.grid(row=2, column=1, sticky="w", padx=5, pady=5)
        self.celcius.insert(0, "0.0")
        self.celcius.bind("<Return>", lambda event: self.convert(True))

        # Create a frame for buttons
        self.button_frame = gui.Frame(self.root)
        self.button_frame.grid(row=3, columnspan=2)

        # Buttons Row
        self.convert_to_celcius = gui.Button(self.button_frame, text=">>>>", command=lambda: self.convert(False))
        self.convert_to_celcius.grid(row=3, column=0, sticky="e", padx=5, pady=10)

        self.convert_to_fahrenheit = gui.Button(self.button_frame, text="<<<<", command=lambda: self.convert(True))
        self.convert_to_fahrenheit.grid(row=3, column=1, sticky="w", padx=5, pady=10)

        self.result = gui.Message(self.button_frame, text="---")
        self.result.grid(row=4, column=0, columnspan=2, sticky="nsew")

    # Convert between temperatures
    def convert(self, reverse:bool):
        try:
            fahrenheit = float(self.fahrenheit.get())
            celcius = float(self.celcius.get())
        except ValueError:
            raise ValueError("Error computing temperature value(s)")
        else:
            computed:float = 0
            if reverse:
                computed = (celcius * 9 / 5) + 32
                self.result.config(text=f"F -> C: {computed}")
            else:
                computed = (fahrenheit - 32) * 5 / 9
                self.result.config(text=f"C -> F: {computed}")
            print(computed)

    # Create key press event
    def key_press(self, reverse:bool):
        try:
            self.convert(reverse)
        except AttributeError:
            raise AttributeError("Invalid key press")

# Create the GUI interface
def main():
    root = gui.Tk()
    app = TemperatureConverter(root)
    root.mainloop()

# Run main method
if __name__ == "__main__":
    main()