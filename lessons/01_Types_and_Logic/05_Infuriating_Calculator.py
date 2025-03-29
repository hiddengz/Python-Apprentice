"""
Infuriating Calculator

Let's write a calculator that's really hard to use, not because we want it to be
hard, but just because we haven't learned how to make it easy yet.

Ask the user for three things: 

1. A number
2. A second number
3. A math operation (add, subtract, multiply, divide)
4. Use if-elif-else statements to provide the desired math operation on the
   numbers and display the result.

If the user enters an unknown operation, display an error message. ( use
messagebox.showerror() 

For the number, you can ask for a float or an integer with
simpledialog.askfloat() or simpledialog.askinteger(), and for the math operation
you can ask for a string with simpledialog.askstring().

"""

# Import the required modules

# Create a window object

# Hide the window, hint: use the withdraw method

# Ask the user for the first number   

# Ask the user for the second number

# Ask the user for the math operation

# Use if-elif-else statements to provide the desired math operation on the numbers and display the result.

# If the user enters an unknown operation, display an error message. ( use messagebox.showerror()

# Keep the window open

import tkinter as tk
from tkinter import simpledialog, messagebox

root = tk.Tk()

root.withdraw()
#this is da first number
num1 = simpledialog.askfloat("Input", "Enter the first of the numbers:")
if num1 is None:
    messagebox.showerror("Error", "maybe enter a number!")
    exit()

# and teh second number
num2 = simpledialog.askfloat("Input", "so now enter the second number:")
if num2 is None:
    messagebox.showerror("Error", "bro theres no number entered!")
    exit()

# Askin the user what they want
operation = simpledialog.askstring("Input", "Enter operation (add, subtract, multiply, divide):")
if operation is None:
    messagebox.showerror("Error", "bro theres no operation entered.")
    exit()

# all of the operations
if operation.lower() == "add":
    result = num1 + num2
elif operation.lower() == "subtract":
    result = num1 - num2
elif operation.lower() == "multiply":
    result = num1 * num2
elif operation.lower() == "divide":
    if num2 == 0:
        messagebox.showerror("Error", "like dude you cant divide with zero!")
        exit()
    result = num1 / num2
else:
    messagebox.showerror("Error", "Unknown operation!")
    exit()

# showing the result
messagebox.showinfo("Result", f"The result is: {result}")

# Keepin the window open. (i hope)
root.mainloop()
