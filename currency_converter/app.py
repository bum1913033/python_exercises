#imports
from tkinter import *
import tkinter as tk
from forex_python.converter import CurrencyRates

#Instance of CurrencyRates
c = CurrencyRates()

#List of Countries
countries = {
    1: 'USD',
    2: 'EUR',
    3: 'GBP',
    4: 'JPY',
    5: 'CNY',
    6: 'SGD',
    7: 'HKD',
    8: 'AUD',
    9: 'CAD',
    10: 'INR'
}

#main window
root = tk.Tk()
root.title("Currency Converter")
# root.geometry("300x200")

canvas = tk.Canvas(root, width=600, height=300)
canvas.grid(columnspan=3, rowspan=3)

#Create input widgets
country_label = tk.Label(root, text="Select the country for conversion:")
country_label.grid(column=2, row=0)

amount_label = tk.Label(root, text="Enter the amount in MYR:")
amount_label.grid(column=1, row=0)

country_var = tk.StringVar()
country_var.set("Select")

country_dropdown = tk.OptionMenu(root, country_var, *countries.values())
country_dropdown.grid(column=2, row=1)

amount_var = tk.StringVar()
amount_entry = tk.Entry(root, textvariable=amount_var)
amount_entry.grid(column=1, row=1)

#button
convert_button = tk.Button(root, text="Convert", command=lambda:convert_currency(amount_var, country_var), bg="#20bebe", fg="white")
convert_button.grid(column=1,row=2)

#result label
result_label = tk.Label(root, text="")
result_label.grid(column=2, row=2)

#functions
def convert_currency(amount_var, country_var):
    # Get the user's input
    amount = float(amount_var.get())
    to_currency = country_var.get()
    
    #check input validity
    if to_currency not in countries.values():
        result_label.config(text="Invalid input. Please select a valid country.")
    else:
        result = round(c.convert('MYR', to_currency, amount), 2)
        result_label.config(text=f"{amount} MYR is equivalent to {result} {to_currency}")
        
#mainloop
root.mainloop()