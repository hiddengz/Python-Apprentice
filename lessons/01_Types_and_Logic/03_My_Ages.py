
"""
Am I Big Yet?

Ask the user's age then use an if-elif-else statement to 
tell the user what age groups the user is in. The groups are:

0-2: Baby
3-5: Toddler
6-12: Child
13-19: Teen
20-64: Adult
65+: Senior

Except, if the user is the same age as you, print "You are pretty awesome!"

Here is how you ask the user's age in integer format.  The first argument is 
the title of the window, the second is the message to the user.

age = simpledialog.askinteger("Your Age", "How old are you?") 

Or, you could ask the user for a float with simpledialog.askfloat() 

age =  simpledialog.askfloat("Your Age", "How old are you?")


Here is how you show the user a message window. The first parameter is the title of the window, 
the second is the message to show the user.

messagebox.showinfo('What you are', "You are a baby.")

"""

# Try to write your program so you only need to use one messagebox.showinfo() function.

from tkinter import messagebox, simpledialog, Tk  # Import required modules


window = Tk()
window.withdraw()  


age = simpledialog.askinteger("Your Age", "How old are you?")


if age is not None:  
    if age == 13:  
        message = "yo same age!"
    elif 0 <= age <= 2:
        message = "hUh."
    elif 3 <= age <= 5:
        message = "bros addicted to his ipad."
    elif 6 <= age <= 12:
        message = "ok."
    elif 13 <= age <= 19:
        message = "dang you old."
    elif 20 <= age <= 64:
        message = "dang your super old."
    else:  # they old ig
        message = "walking fossil over here!"
    
    
    messagebox.showinfo("What you are", message)

