import sys
from tkinter import Tk, simpledialog, messagebox

# Create a Tkinter root window
root = Tk()
root.withdraw()

while True:

    # Get the length and width of the rectangle from the user
    length = simpledialog.askfloat("Length", "Enter the length of the rectangle: ")
    width = simpledialog.askfloat("Width", "Enter the width of the rectangle: ")
    
    # Calculate the area of the rectangle
    area = length * width

    # Display the area of the rectangle to the user
    messagebox.showinfo("Area", "The area of the rectangle is " + str(area))

    # Ask the user if they want to continue
    result = messagebox.askyesno("Continue", "Do you want to calculate the area of another rectangle?")

    # If the user does not want to continue, break out of the loop
    if not result:
        break
# Close the Tkinter root window
root.destroy()

