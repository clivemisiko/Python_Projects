import tkinter as tk
from tkinter import ttk

# Conversion functions
def convert_length():
    try:
        value = float(input_entry.get())
        from_unit = from_combobox.get()
        to_unit = to_combobox.get()

        # Convert to base unit (meters)
        if from_unit == "Kilometers":
            value *= 1000
        elif from_unit == "Centimeters":
            value /= 100
        elif from_unit == "Millimeters":
            value /= 1000
        elif from_unit == "Miles":
            value *= 1609.34
        elif from_unit == "Yards":
            value *= 0.9144
        elif from_unit == "Feet":
            value *= 0.3048
        elif from_unit == "Inches":
            value *= 0.0254

        # Convert from base unit (meters) to target unit
        if to_unit == "Kilometers":
            value /= 1000
        elif to_unit == "Centimeters":
            value *= 100
        elif to_unit == "Millimeters":
            value *= 1000
        elif to_unit == "Miles":
            value /= 1609.34
        elif to_unit == "Yards":
            value /= 0.9144
        elif to_unit == "Feet":
            value /= 0.3048
        elif to_unit == "Inches":
            value /= 0.0254

        result_label.config(text=f"{value:.4f}")
    except ValueError:
        result_label.config(text="Invalid input")

def convert_weight():
    try:
        value = float(input_entry.get())
        from_unit = from_combobox.get()
        to_unit = to_combobox.get()

        # Convert to base unit (kilograms)
        if from_unit == "Grams":
            value /= 1000
        elif from_unit == "Milligrams":
            value /= 1_000_000
        elif from_unit == "Pounds":
            value *= 0.453592
        elif from_unit == "Ounces":
            value *= 0.0283495

        # Convert from base unit (kilograms) to target unit
        if to_unit == "Grams":
            value *= 1000
        elif to_unit == "Milligrams":
            value *= 1_000_000
        elif to_unit == "Pounds":
            value /= 0.453592
        elif to_unit == "Ounces":
            value /= 0.0283495

        result_label.config(text=f"{value:.4f}")
    except ValueError:
        result_label.config(text="Invalid input")

def convert_temperature():
    try:
        value = float(input_entry.get())
        from_unit = from_combobox.get()
        to_unit = to_combobox.get()

        # Convert to base unit (Celsius)
        if from_unit == "Fahrenheit":
            value = (value - 32) * 5 / 9
        elif from_unit == "Kelvin":
            value = value - 273.15

        # Convert from base unit (Celsius) to target unit
        if to_unit == "Fahrenheit":
            value = (value * 9 / 5) + 32
        elif to_unit == "Kelvin":
            value = value + 273.15

        result_label.config(text=f"{value:.4f}")
    except ValueError:
        result_label.config(text="Invalid input")

# Function to update units based on category
def update_units(*args):
    category = category_combobox.get()
    if category == "Length":
        units = ["Meters", "Kilometers", "Centimeters", "Millimeters", "Miles", "Yards", "Feet", "Inches"]
    elif category == "Weight":
        units = ["Kilograms", "Grams", "Milligrams", "Pounds", "Ounces"]
    elif category == "Temperature":
        units = ["Celsius", "Fahrenheit", "Kelvin"]

    from_combobox["values"] = units
    to_combobox["values"] = units
    from_combobox.current(0)
    to_combobox.current(1)

# Function to handle conversion
def perform_conversion():
    category = category_combobox.get()
    if category == "Length":
        convert_length()
    elif category == "Weight":
        convert_weight()
    elif category == "Temperature":
        convert_temperature()

# Create the main window
root = tk.Tk()
root.title("Unit Converter")
root.geometry("400x300")

# Category selection
category_label = tk.Label(root, text="Category:", font=("Arial", 12))
category_label.grid(row=0, column=0, padx=10, pady=10)

category_combobox = ttk.Combobox(root, values=["Length", "Weight", "Temperature"], font=("Arial", 12))
category_combobox.grid(row=0, column=1, padx=10, pady=10)
category_combobox.current(0)
category_combobox.bind("<<ComboboxSelected>>", update_units)

# Input field
input_label = tk.Label(root, text="Enter Value:", font=("Arial", 12))
input_label.grid(row=1, column=0, padx=10, pady=10)

input_entry = tk.Entry(root, font=("Arial", 12))
input_entry.grid(row=1, column=1, padx=10, pady=10)

# From unit
from_label = tk.Label(root, text="From:", font=("Arial", 12))
from_label.grid(row=2, column=0, padx=10, pady=10)

from_combobox = ttk.Combobox(root, font=("Arial", 12))
from_combobox.grid(row=2, column=1, padx=10, pady=10)

# To unit
to_label = tk.Label(root, text="To:", font=("Arial", 12))
to_label.grid(row=3, column=0, padx=10, pady=10)

to_combobox = ttk.Combobox(root, font=("Arial", 12))
to_combobox.grid(row=3, column=1, padx=10, pady=10)

# Update units initially
update_units()

# Convert button
convert_button = tk.Button(root, text="Convert", font=("Arial", 12), command=perform_conversion)
convert_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Result label
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

# Run the application
root.mainloop()