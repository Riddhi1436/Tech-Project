#[project]

"""
a) Build a Temperature Conversion Application
Build a temperature conversion application that converts temperature from
degree Fahrenheit to degree Celcius and vice versa, using the python tkinter module.

"""
import tkinter as tk

def convert_to_celsius():
    fahrenheit = float(entry.get())
    celsius = (fahrenheit - 32) * 5/9
    result_label.config(text=f"{fahrenheit}°F is {celsius:.2f}°C")
def convert_to_fahrenheit():
    celsius = float(entry.get())
    fahrenheit = celsius * 9/5 + 32
    result_label.config(text=f"{celsius}°C is {fahrenheit:.2f}°F")
    
root = tk.Tk()
root.title("Temperature Converter")
entry = tk.Entry(root, width=10)
entry.grid(row=0, column=0, padx=5, pady=5)
to_celsius_btn = tk.Button(root, text="Fahrenheit to Celsius", command=convert_to_celsius)
to_celsius_btn.grid(row=1, column=0, padx=5, pady=5)
to_fahrenheit_btn = tk.Button(root, text="Celsius to Fahrenheit", command=convert_to_fahrenheit)
to_fahrenheit_btn.grid(row=1, column=1, padx=5, pady=5)
result_label = tk.Label(root, text="")
result_label.grid(row=2, column=0, columnspan=2, padx=5, pady=5)
root.mainloop()
