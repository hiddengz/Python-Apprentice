"""
Write a Python program that asks the user for two numbers. The program should
display the sum of the two numbers.

In this program we will just give you the comments for what you need to do. Look
at the comments and the code snippets in the previous lessons, like
03_My_Ages.py, to figure out how to complete the program.


"""

# Import the required modules

# Create a window object

# Hide the window, hint: use the withdraw method

# Ask the user for the first number   

# Ask the user for the second number

# Display the sum of the two numbers 

# Keep the window open

from tkinter import Tk, simpledialog, messagebox


window = Tk()

window.withdraw()

#first number
num1 = simpledialog.askinteger("Input", "do the first number:")

#its the second number
num2 = simpledialog.askinteger("Input", "put in the second number:")


if num1 is not None and num2 is not None:
    total = num1 + num2
    messagebox.showinfo("Result", f"adding {num1} and {num2} gets you {total}")
else:
    messagebox.showerror("uh", "these aint numbers. Please enter valid numbers.")

# Keepin the window open (not needed since messagebox will hold execution)
window.mainloop()
