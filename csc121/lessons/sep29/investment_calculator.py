"""
investment_calculator.py: create a GUI investment calculator with tkinter
By: Dillon S.
9/29/26
"""

import tkinter as tk

# # Create a frame (or window)
# root = tk.Tk()
#
# # Set title for frame (or window)
# root.title("Investment Calculator")
#
# # Set size for frame
# root.geometry("400x400")
#
# # Determine if frame should be resizeable
# root.resizable(width=False, height=False)
#
# # Create a label for the frame
# label = tk.Label(root, text="Invested Amount")
#
# # pack() method makes label visible
# label.pack()
#
# # Create an entry (textbox) for the frame
# entry = tk.Entry(root, width=20)
#
# # pack() method makes entry (textbox) visible
# entry.pack()
#
# # Gets the value from current entry box (default = string)
# amount = entry.get()
#
# # Create a button to show amount, with a lambda
# button = tk.Button(root, text="Show Amount", command=lambda:show_user_input)
#
# # Pack the button
# button.pack()
#
# # Create a label for the amount
# label_amount = tk.Label(root, text="The amount user entered is $")
# label_amount.pack()
#
# def show_user_input():
#     amount = entry.get()
#     label_amount.config(text=amount)
#
# # Display the frame
# root.mainloop()

class InvestmentCalculator:

    def __init__(self, root):
        """
        layout the GUI
        :param root: Tk()
        """
        self.root = root
        self.root.title("Investment Calculator")
        self.root.geomtry("400x400")
        self.create_widgets()

    def create_widgets(self):
        title_label = tk.Label(self.root, text="Monthly-Compounded Investment Calculator")
        title_label.grid(row=0, column=0, columnspan=2, pady=10)

        tk.Label(self.root, text="Investment Amount").grid(row=1, column=0, padx=10, pady=10)
        self.investment_entry = tk.Entry(self.root, width=20)
        self.investment_entry.grid(row=1, column=1, oadx=10, padx=10, pady=10)

        tk.Label(self.root, text="Annual Interest Rate (%)").grid(row=2, column=0, padx=10, pady=10)
        self.apr_entry = tk.Entry(self.root, width=20)
        self.apr_entry.grid(row=2, column=1, oadx=10, padx=10, pady=10)

        tk.Label(self.root, text="Investment Term (years)").grid(row=3, column=0, padx=10, pady=10)
        self.years_entry = tk.Entry(self.root, width=20)
        self.years_entry.grid(row=3, column=1, oadx=10, padx=10, pady=10)

        calc_button = tk.Button(self.root, text="Calculate", command=self.calculate)
        calc_button.grid(row=4, column=0, padx=10, pady=10)

        # Result
        self.result_label = tk.Label(self.root, text="Future Value: $0.00")
        self.result_label.grid(row=5, column=0, columnspan=2, pady=10, sticky=tk.E)

    # Calculate the amount
    def calculate(self):
        try:
            invested_amount = float(self.investment_entry.get())
            apr = float(self.apr_entry.get())
            years = int(self.years_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Please enter a numeric value")
        else:
            future_value = invested_amount * (1 + apr / 100 / 12) ** (years * 12)
            interest_gained = future_value - invested_amount

            result = f"Future Value: ${future_value:,.2f}"
            result += f"\nInterest Gained: ${interest_gained:,.2f}"

            self.result_label.config(text=result)

    # Clear the result
    def clear(self):
        pass

# Create main method
def main():
    root = tk.Tk()
    app = InvestmentCalculator(root)
    root.mainloop()

# Run main method
if __name__ == "__main__":
    main()