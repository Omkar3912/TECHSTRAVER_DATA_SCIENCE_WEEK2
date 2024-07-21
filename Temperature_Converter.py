import tkinter as tk
from tkinter import ttk

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def convert_to_fahrenheit():
    try:
        celsius = float(celsius_entry.get())
        fahrenheit = celsius_to_fahrenheit(celsius)
        result_label.config(text=f"Result: {fahrenheit:.2f} °F")
    except ValueError:
        result_label.config(text="Invalid input. Please enter a number.")

def convert_to_celsius():
    try:
        fahrenheit = float(fahrenheit_entry.get())
        celsius = fahrenheit_to_celsius(fahrenheit)
        result_label.config(text=f"Result: {celsius:.2f} °C")
    except ValueError:
        result_label.config(text="Invalid input. Please enter a number.")

# Create the main window
root = tk.Tk()
root.title("Temperature Converter")
root.geometry("300x150")

# Create and place the widgets
celsius_label = ttk.Label(root, text="Celsius:")
celsius_label.grid(column=0, row=0, padx=10, pady=10)

celsius_entry = ttk.Entry(root)
celsius_entry.grid(column=1, row=0, padx=10, pady=10)

fahrenheit_label = ttk.Label(root, text="Fahrenheit:")
fahrenheit_label.grid(column=0, row=1, padx=10, pady=10)

fahrenheit_entry = ttk.Entry(root)
fahrenheit_entry.grid(column=1, row=1, padx=10, pady=10)

convert_to_fahrenheit_button = ttk.Button(root, text="Convert to Fahrenheit", command=convert_to_fahrenheit)
convert_to_fahrenheit_button.grid(column=0, row=2, padx=10, pady=10)

convert_to_celsius_button = ttk.Button(root, text="Convert to Celsius", command=convert_to_celsius)
convert_to_celsius_button.grid(column=1, row=2, padx=10, pady=10)

result_label = ttk.Label(root, text="Result: ")
result_label.grid(column=0, row=3, columnspan=2, padx=10, pady=10)

# Run the main event loop
root.mainloop()
