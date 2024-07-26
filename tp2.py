# Electricity bill generator program

import tkinter as tk

# Function to calculate electricity bill amount
def calculate_bill():
    # Get the number of units consumed and rate per unit from the input fields
    units_consumed = float(units_entry.get())
    rate_per_unit = float(rate_entry.get())

    # Calculate the bill amount
    bill_amount = units_consumed * rate_per_unit

    # Display the bill amount in the label
    bill_label.config(text=f"Bill amount: {bill_amount:.2f}")

# Create the main window
root = tk.Tk()

# Create the input fields and labels
units_label = tk.Label(root, text="Number of units consumed:")
units_entry = tk.Entry(root)

rate_label = tk.Label(root, text="Rate per unit:")
rate_entry = tk.Entry(root)

# Create the calculate button
calculate_button = tk.Button(root, text="Calculate Bill", command=calculate_bill)

# Create the bill label
bill_label = tk.Label(root, text="")

# Pack the widgets
units_label.pack()
units_entry.pack()

rate_label.pack()
rate_entry.pack()

calculate_button.pack()

bill_label.pack()

# Run the main loop
root.mainloop()
